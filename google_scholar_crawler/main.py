"""Fetch Google Scholar citation stats for the homepage.

The profile page already includes the total, h-index, i10-index, yearly
histogram, and per-paper counts, so this script makes one HTML request
instead of using the scholarly package. scholarly 1.5.1 still parses the
page from a normal network, but the scheduled GitHub Action has been
failing on every run since the 2026-09-04 snapshot: Actions runners are
blocked, and the library then errors out in a few seconds.

Direct fetch is tried first. If Google serves a block page, the script
retries through a short list of public proxies.
"""

from __future__ import annotations

import json
import os
import re
import time
import urllib.request
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID") or "chf7U2cAAAAJ"
REPO = os.environ.get("GITHUB_REPOSITORY") or "ch3cook-fdu/ch3cook-fdu.github.io"
RESULTS = Path(__file__).resolve().parent / "results"
PROFILE_URL = (
    "https://scholar.google.com/citations?hl=en&user={user}"
    "&cstart={start}&pagesize=100&view_op=list_works"
)
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
PROXY_LIST_URL = (
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http"
    "&timeout=5000&country=US,DE,JP,SG,FR,NL&ssl=all&anonymity=elite"
)


class ScholarBlocked(RuntimeError):
    pass


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def _int(text: str) -> int:
    digits = re.sub(r"[^\d]", "", text or "")
    return int(digits) if digits else 0


def fetch_html(url: str, proxy: str | None = None, timeout: int = 25) -> str:
    handlers = []
    if proxy:
        handlers.append(urllib.request.ProxyHandler({"http": proxy, "https": proxy}))
    opener = urllib.request.build_opener(*handlers)
    request = urllib.request.Request(url, headers=HEADERS)
    with opener.open(request, timeout=timeout) as response:
        html = response.read().decode("utf-8", "replace")
    if "gsc_rsb_std" not in html or "gsc_a_tr" not in html:
        raise ScholarBlocked("Google Scholar did not return a profile page")
    return html


def load_proxy_candidates(limit: int = 12) -> list[str]:
    try:
        request = urllib.request.Request(PROXY_LIST_URL, headers={"User-Agent": HEADERS["User-Agent"]})
        with urllib.request.urlopen(request, timeout=20) as response:
            text = response.read().decode("utf-8", "replace")
    except Exception as exc:
        print("Could not load proxy list:", exc)
        return []
    proxies = []
    for line in text.splitlines():
        line = line.strip()
        if re.fullmatch(r"\d+\.\d+\.\d+\.\d+:\d+", line):
            proxies.append("http://" + line)
        if len(proxies) >= limit:
            break
    return proxies


def fetch_profile_pages() -> list[str]:
    pages = []
    proxies: list[str | None] | None = None
    for start in range(0, 500, 100):
        url = PROFILE_URL.format(user=SCHOLAR_ID, start=start)
        if proxies is None:
            html = ""
            direct_error: Exception | None = None
            for attempt in range(3):
                try:
                    html = fetch_html(url)
                    print(f"Fetched profile page cstart={start} directly")
                    break
                except Exception as exc:
                    direct_error = exc
                    print(f"Direct fetch attempt {attempt + 1} failed ({type(exc).__name__}: {exc})")
                    time.sleep(2)
            if not html:
                exc = direct_error or ScholarBlocked("direct fetch failed")
                print(f"Direct fetch failed ({type(exc).__name__}: {exc}). Trying proxies...")
                proxies = load_proxy_candidates()
                html = ""
                last_error: Exception | None = exc
                for proxy in proxies:
                    try:
                        html = fetch_html(url, proxy=proxy, timeout=12)
                        print(f"Fetched profile page via {proxy}")
                        proxies = [proxy]
                        break
                    except Exception as proxy_exc:
                        last_error = proxy_exc
                        print(f"Proxy {proxy} failed: {type(proxy_exc).__name__}")
                if not html:
                    raise ScholarBlocked(f"Unable to fetch Google Scholar profile: {last_error}")
        else:
            proxy = proxies[0]
            html = fetch_html(url, proxy=proxy, timeout=12)
            print(f"Fetched profile page cstart={start} via {proxy}")
        pages.append(html)
        button = re.search(r'<button[^>]*id="gsc_bpf_more"[^>]*>', html)
        if not button or "disabled" in button.group(0):
            break
    return pages


def parse_author(pages: list[str]) -> dict:
    first = pages[0]
    stats = [_int(v) for v in re.findall(r'class="gsc_rsb_std"[^>]*>([^<]+)', first)]
    if len(stats) < 6:
        raise RuntimeError(f"Expected 6 citation stats, found {len(stats)}")
    citedby, citedby5y, hindex, hindex5y, i10index, i10index5y = stats[:6]

    years = re.findall(r'class="gsc_g_t"[^>]*>(\d{4})</span>', first)
    year_counts = [_int(v) for v in re.findall(r'class="gsc_g_al"[^>]*>([^<]*)</span>', first)]
    if years and len(years) == len(year_counts):
        cites_per_year = {year: count for year, count in zip(years, year_counts)}
    else:
        cites_per_year = {}
        print(f"Yearly chart mismatch: years={years} counts={year_counts}")

    name_match = re.search(r'id="gsc_prf_in"[^>]*>(.*?)</div>', first, re.S)
    name = unescape(re.sub(r"\s+", " ", name_match.group(1))).strip() if name_match else ""

    publications = {}
    for html in pages:
        for row in re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', html, re.S):
            id_match = re.search(r"citation_for_view=([^\"&]+)", row)
            title_match = re.search(r'class="gsc_a_at"[^>]*>(.*?)</a>', row, re.S)
            if not id_match or not title_match:
                continue
            pub_id = unescape(id_match.group(1))
            title = unescape(re.sub(r"<[^>]+>", "", title_match.group(1)))
            title = re.sub(r"\s+", " ", title).strip()
            cite_match = re.search(r'class="gsc_a_ac[^"]*"[^>]*>([^<]*)', row)
            year_match = re.search(r'class="gsc_a_h[^"]*">(\d{4})</span>', row)
            publications[pub_id] = {
                "container_type": "Publication",
                "source": "AUTHOR_PUBLICATION_ENTRY",
                "bib": {
                    "title": title,
                    "pub_year": year_match.group(1) if year_match else "",
                },
                "filled": False,
                "author_pub_id": pub_id,
                "num_citations": _int(cite_match.group(1)) if cite_match else 0,
            }

    if citedby <= 0 or not publications:
        raise RuntimeError("Parsed profile is missing citations or publications")

    return {
        "container_type": "Author",
        "filled": ["basics", "publications", "indices", "counts"],
        "scholar_id": SCHOLAR_ID,
        "source": "AUTHOR_PROFILE_PAGE",
        "name": name,
        "citedby": citedby,
        "citedby5y": citedby5y,
        "hindex": hindex,
        "hindex5y": hindex5y,
        "i10index": i10index,
        "i10index5y": i10index5y,
        "cites_per_year": cites_per_year,
        "publications": publications,
        "updated": _now(),
    }


def load_history() -> list:
    url = f"https://raw.githubusercontent.com/{REPO}/google-scholar-stats/gs_data_history.json"
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            prev = json.loads(response.read().decode("utf-8"))
        history = prev.get("history", []) if isinstance(prev, dict) else (prev or [])
        return history if isinstance(history, list) else []
    except Exception as exc:
        print("No previous citation history found, starting fresh:", exc)
        return []


def write_results(author: dict) -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    history = [item for item in load_history() if item.get("date") != datetime.now(timezone.utc).strftime("%Y-%m-%d")]
    history.append({"date": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "citations": int(author["citedby"])})
    history.sort(key=lambda item: item.get("date", ""))

    (RESULTS / "gs_data.json").write_text(
        json.dumps(author, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (RESULTS / "gs_data_shieldsio.json").write_text(
        json.dumps({"schemaVersion": 1, "label": "citations", "message": str(author["citedby"])}, ensure_ascii=False),
        encoding="utf-8",
    )
    (RESULTS / "gs_data_history.json").write_text(
        json.dumps({"history": history, "updated": _now()}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(
        f"Wrote {author['citedby']} citations, h-index {author['hindex']}, "
        f"i10-index {author['i10index']}, {len(author['publications'])} papers"
    )


def main() -> None:
    write_results(parse_author(fetch_profile_pages()))


if __name__ == "__main__":
    main()
