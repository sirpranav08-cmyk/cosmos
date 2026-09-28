<div align="center">

# 🌌 COSMOS

### Cognitive Observation & Sky-Motion Investigation System

**An AI-driven engine that spots changes in telescope images, weighs competing explanations, and reports how confident it is.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white)
![Astropy](https://img.shields.io/badge/Astropy-FF5D01?logoColor=white)
![NASA](https://img.shields.io/badge/NASA-Hackathon-0B3D91?logo=nasa&logoColor=white)
![Status](https://img.shields.io/badge/status-prototype-orange)

</div>

---

## 🚀 Hackathon

| | |
|---|---|
| 🏆 **Event** | NASA Hackathon — *[add event name & year]* |
| 🎯 **Challenge** | *[add challenge / track name]* |
| 👥 **Team** | *[add team name]* |
| 🏫 **College** | Karpagam College of Engineering, Coimbatore |

---

## 🔭 What is COSMOS?

Sky surveys produce more images than people can review. Most "detections" are noise, camera artifacts, or objects we already know. **COSMOS automates the first look**: it finds what changed between two images of the sky, works out where it is, and decides whether it is a real moving object — without ever overclaiming a discovery.

## ✨ Key Features

- 🖼️ **FITS image pipeline** — load, clean, align, and compare telescope images
- 🔍 **Change detection** — difference imaging finds sources that appear or move
- 📍 **Sky mapping** — pixel positions converted to RA/Dec (WCS)
- 🧠 **Multi-hypothesis reasoning** — moving object vs. stationary vs. artifact vs. transient
- ⚖️ **Evidence-weighted confidence** — every score traces back to named evidence
- 🔁 **Autonomous loop** — finds its own evidence gaps, plans actions, and updates beliefs
- 💾 **Memory** — every investigation is saved for later
- 🛡️ **Cautious reports** — never calls a candidate a confirmed discovery without proof

## 🔄 How It Works

```
🛰️ FITS Images ─► 🧹 Clean & Align ─► 🔍 Detect Changes ─► 📍 Sky Coordinates
                                                               │
        📝 Report ◄─ ✅ Verify ◄─ 🤔 Reflect ◄─ 🧠 Reason ◄────┘
                                                 ▲
                                                 └── 🔁 Plan → Act → New Evidence
```

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| 💻 **Language** | Python 3.10+ |
| 🔢 **Numerics** | NumPy |
| 🧪 **Image processing** | SciPy (`ndimage`), FFT cross-correlation |
| 🔭 **Astronomy** | Astropy (`io.fits`, `wcs`) |
| 💾 **Storage** | JSON file memory |
| 📡 **Data format** | FITS (NASA standard) |

## 📁 Repository Structure

```
cosmos/
├── 🚪 main.py                 # Run the full investigation
├── 🧠 core/                   # Brain + shared data models
├── 🔬 science_engine/         # FITS → align → diff → detect → WCS
├── 👁️ perception/             # Raw data → observations
├── 🗺️ planning/               # Goal → investigation plan
├── 💡 reasoning/              # Hypotheses, evidence, reflection
├── ✅ verification/           # Confidence checks
├── 🤖 agi/                    # Autonomous reflect → plan → act loop
├── 🧰 tools/                  # Motion & spectrum calculations
├── 🌍 world/                  # Object & relationship store
├── 💾 memory/                 # Saved investigations
├── 📝 language/               # Report generation
├── 🌠 data/                   # Sample FITS images
└── 🧪 test_*.py               # Component demos
```

## ⚡ Quick Start

```bash
git clone <repo-url>
cd cosmos
pip install numpy scipy astropy

python main.py              # 🧠 cognitive engine
python test_pipeline.py     # 🔬 image pipeline
python test_autonomous.py   # 🤖 autonomous loop
```

## 📊 Sample Result

```
GOAL: Find unusual moving objects

Moving astronomical object:        0.76  ◄── strongest
Stationary astronomical source:    0.30
Measurement or imaging artifact:   0.20
Transient astronomical event:      0.20

STATUS: SUPPORTED
```

## 🚧 Current Status

| ✅ Working | 🔨 In Progress |
|---|---|
| FITS loading & preprocessing | Real catalog cross-matching |
| Image alignment & differencing | Real artifact detection |
| Source detection & WCS mapping | Connecting image pipeline to reasoning engine |
| Hypothesis reasoning & reflection | Validation on real NASA data |
| Autonomous loop & memory | Automated test suite |

## 🗺️ Roadmap

- [ ] 🔗 Connect image pipeline directly to the reasoning engine
- [ ] 🌌 Catalog matching (SIMBAD / Gaia)
- [ ] 🧹 Artifact detection (cosmic rays, hot pixels)
- [ ] 📈 Multi-epoch trajectory fitting
- [ ] 📊 Visual dashboard

## 👥 Team

| 👤 Name | 🎓 Role | 🏫 College | 🔗 LinkedIn / GitHub |
|---|---|---|---|
| Sriram | *[role]* | Karpagam College of Engineering | *[link]* |
| *[name]* | *[role]* | *[college]* | *[link]* |
| *[name]* | *[role]* | *[college]* | *[link]* |
| *[name]* | *[role]* | *[college]* | *[link]* |

## 🙏 Acknowledgments

🚀 NASA · 🔭 Astropy · 🔢 NumPy · 🧪 SciPy

## 📄 License

*[add license, e.g. MIT]*

---

<div align="center">⭐ Built with curiosity for the cosmos ⭐</div>
