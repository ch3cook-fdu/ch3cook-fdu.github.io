from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os
import urllib.request

author: dict = scholarly.search_author_id(os.environ.get('GOOGLE_SCHOLAR_ID') or 'chf7U2cAAAAJ')
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

# ---------------------------------------------------------------------------
# Maintain a daily citation history for the homepage line chart.
# The workflow force-pushes a fresh "results" dir each run, so we first pull
# the previously published history from the google-scholar-stats branch,
# append today's snapshot, and write it back.
# ---------------------------------------------------------------------------
history = []
repo = os.environ.get('GITHUB_REPOSITORY')
if repo:
    history_url = f"https://raw.githubusercontent.com/{repo}/google-scholar-stats/gs_data_history.json"
    try:
        with urllib.request.urlopen(history_url, timeout=30) as resp:
            prev = json.loads(resp.read().decode('utf-8'))
            history = prev.get('history', []) if isinstance(prev, dict) else (prev or [])
    except Exception as e:
        print('No previous citation history found, starting fresh:', e)

today = datetime.now().strftime('%Y-%m-%d')
history = [h for h in history if h.get('date') != today]
history.append({'date': today, 'citations': int(author['citedby'])})
history = sorted(history, key=lambda h: h['date'])

with open('results/gs_data_history.json', 'w') as outfile:
    json.dump({'history': history, 'updated': str(datetime.now())}, outfile, ensure_ascii=False)
