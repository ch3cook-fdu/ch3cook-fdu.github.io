---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am currently an AI researcher working on **embodied AI** with Dr. [Tao Kong](https://www.taokong.org/) at **<font color="#3559b0">ByteDance Research</font>**.

I received my Master's degree in Artificial Intelligence from **Fudan University** (Sep. 2021 - Jun. 2024), where Prof. [Tao Chen](https://eetchen.github.io/) is my advisor. I am fortunate to work closely with Dr. [Hongyuan Zhu](https://hongyuanzhu.github.io/) from A*STAR, Singapore, and Dr. [Gang Yu](https://www.skicyyu.org/), Dr. [Xin Chen](https://chenxin.tech/), and Dr. [Chi Zhang](https://icoz69.github.io/) from Tencent. Before this, I obtained my Bachelor's degree in Data Science and Big Data Technology also from **Fudan University** (Sep. 2017 - Jun. 2021).

My long-term research goal is to develop robust and generalized multi-modality systems that can **perceive**, **understand**, and **interact** with the physical world.

📣 If you are interested in my previous projects, feel free to check out my resume [here](resume/chensijin_resume_20250425.pdf).

# 🔥 News

- *Apr. 2025*. &nbsp;🎉🎉 We release [OmniSVG](https://arxiv.org/abs/2504.06263) [![](https://img.shields.io/github/stars/OmniSVG/OmniSVG?style=social)](https://github.com/OmniSVG/OmniSVG), a family of VLMs that progressively generate SVGs spanning from simple icons to intricate anime characters.
- *Jan. 2025*. &nbsp;🎉🎉 Our [MeshAnything](https://arxiv.org/abs/2406.10163) [![](https://img.shields.io/github/stars/buaacyw/MeshAnything?style=social)](https://github.com/buaacyw/MeshAnything) is accepted to <font color="#dd0000">ICLR 2025</font>.
- *Sep. 2024*. &nbsp;🎉🎉 Two papers accepted to <font color="#dd0000">NeurIPS 2024</font>, one focuses on foundational 3D generative models ([MeshXL](https://arxiv.org/abs/2405.20853) [![](https://img.shields.io/github/stars/OpenMeshLab/MeshXL?style=social)](https://github.com/OpenMeshLab/MeshXL)), and another one explores Mamba architecture for 3D detection ([3DET-Mamba](https://proceedings.neurips.cc/paper_files/paper/2024/file/547108084f0c2af39b956f8eadb75d1b-Paper-Conference.pdf)).
- *Jul. 2024*. &nbsp;🎉🎉 Our [M3DBench](https://arxiv.org/abs/2312.10763) [![](https://img.shields.io/github/stars/OpenM3D/M3DBench?style=social)](https://github.com/OpenM3D/M3DBench), a dataset querying 3D LLMs with multi-modal prompts, is accepted to <font color="#dd0000">ECCV 2024</font>.
- *May. 2024*. &nbsp;🎉🎉 We release [MeshXL](https://arxiv.org/abs/2405.20853) [![](https://img.shields.io/github/stars/OpenMeshLab/MeshXL?style=social)](https://github.com/OpenMeshLab/MeshXL), a family of generative 3D foundation models for 3D meshes.
- *May. 2024*. &nbsp;🎉🎉 I successfully defended my master's thesis! \[[defense slides](presentation/Sijin_Chen_master_thesis_defense.pdf)\]
- *Apr. 2024*. &nbsp;🎉🎉 Our state-of-the-art 3D dense captioning method [Vote2Cap-DETR++](https://arxiv.org/abs/2309.02999) [![](https://img.shields.io/github/stars/ch3cook-fdu/Vote2Cap-DETR?style=social)](https://github.com/ch3cook-fdu/Vote2Cap-DETR), is accepted to <font color="#dd0000">T-PAMI 2024</font>. 
- *Feb. 2024*. &nbsp;🎉🎉 Our Large Language 3D Assistant, [LL3DA](https://arxiv.org/abs/2311.18651) [![](https://img.shields.io/github/stars/Open3DA/LL3DA?style=social)](https://github.com/Open3DA/LL3DA), is accepted to <font color="#dd0000">CVPR 2024</font>. 
- *Jan. 2024*. &nbsp;🐧🐧 Join Tencent as a research intern, working on 3D generation. 
- *Oct. 2023*. &nbsp;🥇🥇 Win the Scan2Cap Challenge at <font color="#dd0000">ICCV 2023</font>. 
- *Feb. 2023*. &nbsp;🎉🎉 Our [Vote2Cap-DETR](https://arxiv.org/abs/2301.02508) [![](https://img.shields.io/github/stars/ch3cook-fdu/Vote2Cap-DETR?style=social)](https://github.com/ch3cook-fdu/Vote2Cap-DETR) is accepted to <font color="#dd0000">CVPR 2023</font>. 




# 📝 Selected Publications 

I started my research from exploring <font color="#dd0000">how to use language for better 3D scene understanding</font> ([Vote2Cap-DETR](https://arxiv.org/abs/2301.02508) and [Vote2Cap-DETR++](https://arxiv.org/abs/2309.02999)).
Then, as large language models exhibits tremendous generalist potentials, I also explored <font color="#dd0000">whether LLMs can understand 3D</font> ([LL3DA](https://arxiv.org/abs/2311.18651) and [M3DBench](https://arxiv.org/abs/2312.10763)).
After that, I spent a wonderful half year exploring <font color="#dd0000">whether LLMs can speak 3D</font> ([MeshXL](https://arxiv.org/abs/2405.20853)).
Currently, I am working on both <font color="#dd0000">embodied AI</font> and <font color="#dd0000">AIGC</font>.


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ArXiv Pre-print</div><img src='images/omnisvg.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**<font size=4>OmniSVG: A Unified Scalable Vector Graphics Generation Model</font>**](https://arxiv.org/abs/2504.06263) \\
**<font color="#dd0000">ArXiv Pre-print</font>** | [![](https://img.shields.io/github/stars/OmniSVG/OmniSVG?style=social)](https://github.com/OmniSVG/OmniSVG) \\
[Yiying Yang](https://yiyingyang12.github.io/yiyingyang.github.io/)$^\star$, [Wei Cheng](https://wchengad.github.io/)$^\star$, **<u>Sijin Chen</u>**, [Xianfang Zeng](https://april.zju.edu.cn/team/xianfang-zeng/), [Jiaxu Zhang](https://kebii.github.io/), [Liao Wang](https://aoliao12138.github.io/), [Gang Yu](https://www.skicyyu.org/), [Xinjun Ma](http://xingjunma.com/), [Yu-Gang Jiang](https://fvl.fudan.edu.cn/)

[project](https://omnisvg.github.io/) \| [arXiv](https://arxiv.org/abs/2504.06263) \| [github](https://github.com/OmniSVG/OmniSVG)

- OmniSVG progressively generates SVGs spanning from simple icons to intricate anime characters.
</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/meshxl.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**<font size=4>MeshXL: Neural Coordinate Field for Generative 3D Foundation Models</font>**](https://arxiv.org/abs/2405.20853) \\
**<font color="#dd0000">NeurIPS 2024</font>** | [![](https://img.shields.io/github/stars/OpenMeshLab/MeshXL?style=social)](https://github.com/OpenMeshLab/MeshXL) \\
**<u>Sijin Chen</u>**, [Xin Chen](https://chenxin.tech/)$^{\dagger}$, Anqi Pang, [Xianfang Zeng](https://april.zju.edu.cn/team/xianfang-zeng/), [Wei Cheng](https://wchengad.github.io/), Yijun Fu, [Fukun Yin](https://fukunyin.github.io/), Yanru Wang, Zhibin Wang, [Chi Zhang](https://icoz69.github.io/), [Jingyi Yu](http://www.yu-jingyi.com/cv/), [Gang Yu](https://www.skicyyu.org/), Bin Fu, [Tao Chen](https://eetchen.github.io/)$^{\ddagger}$

[project](https://meshxl.github.io/) \| [arXiv](https://arxiv.org/abs/2405.20853) \| [github](https://github.com/OpenMeshLab/MeshXL)

- MeshXL turns a 3D mesh into one unique coordinate sequence, facilitating an end-to-end training pipeline for large-scale 3D mesh data.
- 🎉 Please also see our [MeshAnything](https://arxiv.org/abs/2406.10163) [![](https://img.shields.io/github/stars/buaacyw/MeshAnything?style=social)](https://github.com/buaacyw/MeshAnything), a model that mimics human artists in extracting meshes from any 3D representation, which is accepted to <font color="#dd0000">ICLR 2025</font>
</div>
</div>




<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2024</div><img src='images/LL3DA.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**<font size=4>LL3DA: Visual Interactive Instruction Tuning for Omni-3D Understanding, Reasoning, and Planning</font>**](https://arxiv.org/abs/2311.18651) \\
**<font color="#dd0000">CVPR 2024</font>** | [![](https://img.shields.io/github/stars/Open3DA/LL3DA?style=social)](https://github.com/Open3DA/LL3DA) \\
**<u>Sijin Chen</u>**, [Xin Chen](https://chenxin.tech/)$^{\dagger}$, [Chi Zhang](https://icoz69.github.io/), Mingsheng Li, [Gang Yu](https://www.skicyyu.org/), [Hao Fei](http://haofei.vip/), [Hongyuan Zhu](https://hongyuanzhu.github.io/), Jiayuan Fan, [Tao Chen](https://eetchen.github.io/)$^{\ddagger}$

[paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_LL3DA_Visual_Interactive_Instruction_Tuning_for_Omni-3D_Understanding_Reasoning_and_CVPR_2024_paper.pdf) \| [project](https://ll3da.github.io/) \| [arXiv](https://arxiv.org/abs/2311.18651) \| [github](https://github.com/Open3DA/LL3DA) \| [youtube](https://www.youtube.com/watch?v=224JzkdHjfg)

- Propose a Large Language 3D Assistant that responds to both visual interactions and textual instructions in complex 3D environments.
- 🎉 Please also see our [M3DBench](https://arxiv.org/abs/2312.10763) [![](https://img.shields.io/github/stars/OpenM3D/M3DBench?style=social)](https://github.com/OpenM3D/M3DBench), a dataset querying 3D LLMs with multi-modal prompts, which is accepted to <font color="#dd0000">ECCV 2024</font>.
</div>
</div>




<div class='paper-box'><div class='paper-box-image'><div><div class="badge">T-PAMI 2024</div><img src='images/vote2cap-detr++ arXiv.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**<font size=4>Vote2Cap-DETR++: Decoupling Localization and Describing for End-to-End 3D Dense Captioning</font>**](https://arxiv.org/abs/2309.02999) \\
**<font color="#dd0000">T-PAMI 2024</font>** | [![](https://img.shields.io/github/stars/ch3cook-fdu/Vote2Cap-DETR?style=social)](https://github.com/ch3cook-fdu/Vote2Cap-DETR) \\
**<u>Sijin Chen</u>**, [Hongyuan Zhu](https://hongyuanzhu.github.io/), Mingsheng Li, [Xin Chen](https://chenxin.tech/), Peng Guo, Yinjie Lei, [Gang Yu](https://www.skicyyu.org/), Taihao Li, [Tao Chen](https://eetchen.github.io/)$^{\dagger}$

[paper](https://ieeexplore.ieee.org/abstract/document/10496863/) \| [arXiv](https://arxiv.org/abs/2309.02999) \| [github](https://github.com/ch3cook-fdu/Vote2Cap-DETR)

- Decoupled feature extraction and task decoding for 3D Dense Captioning.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2023</div><img src='images/vote2cap-detr cvpr2023.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**<font size=4>End-to-End 3D Dense Captioning with Vote2Cap-DETR</font>**](https://openaccess.thecvf.com/content/CVPR2023/html/Chen_End-to-End_3D_Dense_Captioning_With_Vote2Cap-DETR_CVPR_2023_paper.html) \\
**<font color="#dd0000">CVPR 2023</font>** | [![](https://img.shields.io/github/stars/ch3cook-fdu/Vote2Cap-DETR?style=social)](https://github.com/ch3cook-fdu/Vote2Cap-DETR) \\
**<u>Sijin Chen</u>**, [Hongyuan Zhu](https://hongyuanzhu.github.io/), [Xin Chen](https://chenxin.tech/), Yinjie Lei, [Gang Yu](https://www.skicyyu.org/), [Tao Chen](https://eetchen.github.io/)$^{\dagger}$

[paper](https://openaccess.thecvf.com/content/CVPR2023/html/Chen_End-to-End_3D_Dense_Captioning_With_Vote2Cap-DETR_CVPR_2023_paper.html) \| [arXiv](https://arxiv.org/abs/2301.02508) \| [github](https://github.com/ch3cook-fdu/Vote2Cap-DETR) \| [youtube](https://www.youtube.com/watch?v=azR_OvPWYfo)

- We address 3D Dense Captioning as a set prediction problem with parallel decoding.
- The first non-"detect-then-describe" framework for 3D Dense Captioning.
- 🥇 Winner of the Scan2Cap Challenge in the 3rd Language for 3D Scene Workshop at <font color="#dd0000">ICCV 2023</font>. [[talk]](https://www.youtube.com/watch?v=RLrdi-Yhn1o)
</div>
</div>




# 🥇 Awards and Scholarships

- *Apr. 2024*. Award for **Outstanding Graduate Student** (rank 1/24).
- *Oct. 2023*. **1st** place of the Scan2Cap Challenge in the 3rd Language for 3D Scene Workshop at *ICCV 2023*.
- *Sep. 2023*. **National Scholarship** (rank 1/46).
- *Sep. 2022*. **2nd** prize of the Scholarship for Outstanding Students of Master's Degrees.
- *Sep. 2021*. Award for the Scholarship for Outstanding Students of Master's Degrees.
- *Jun. 2021*. **2nd** prize of the Scholarship for Outstanding Students.




# 📖 Educations

- *Sep. 2021 - Jun. 2024*. Master student at Fudan University. 
- *Sep. 2017 - Jun. 2021*. Bachelor student at Fudan University. 



# 💬 Oral Presentations

- *Jul. 2024*. "**MeshXL**: Neural Coordinate Field for Generative 3D Foundation Models".
    MeshXL paves the way for scaling up training on large-scale 3D mesh data. Our mesh representation turns a 3D mesh into one unique coordinate sequence, which enables us to simplify our architecture design into a decoder-only transformer model, facilitating an end-to-end training pipeline for large-scale 3D mesh data.
    A technical report at **<font color="#74d8f0">mi</font>****<font color="#4ea4dd">HoYo</font>**.

- *Oct. 2023*. "**Vote2Cap-DETR**: A Set-to-Set Perspective Towards 3D Dense Captioning".
    By treating 3D Dense Captioning as a translation task from a set of object queries into a set of ``box-caption'' pairs, we present a set-to-set perspective towards 3D Dense Captioning. 
    A **<font color="#dd0000">winner presentation</font>** for the Scan2Cap challenge at **<font color="#dd0000">ICCV 2023</font>**. \[[talk](https://www.youtube.com/watch?v=RLrdi-Yhn1o) \| [slides](presentation/[ICCV 2023 workshop talk] Vote2Cap-DETR.pdf)\]

- *Jun. 2023*. "End-to-End 3D Dense Captioning with Vote2Cap-DETR".
    We present an end-to-end transformer model for localizing and describing objects in parallel within diverse 3D environments. A paper presentation at **<font color="#dd0000">VALSE 2023</font>**, Wuxi, China.
