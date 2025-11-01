#  MaMeeFarm™ — Proof-of-Life & Metadata System  
*From 7 Ducks of Hope to Seed of Hope — Building the Real-Work Data Blueprint*

---

### 🌾 Overview
**MaMeeFarm™** is a real agricultural Proof-of-Life system founded in Lampang, Thailand.  
This repository stores verified metadata, NFT collection structures, and farm-generated records used to document authentic, verifiable human work.  

All data originates from real daily activity — the foundation of the **Proof-of-Work Farm Data System**, where life itself becomes verifiable digital evidence.

---

### 📂 Repository Structure

| File | Description |
|------|--------------|
| `mameefarm_members.json` | Official member directory of MaMeeFarm™ (humans, ducks, and dogs). |
| `fetch_opensea_metadata.py` | Script that fetches and archives NFT metadata from OpenSea collections. |
| `SECURITY.md` | Data-integrity and provenance policy for MaMeeFarm™ datasets. |
| `README.md` | Main documentation and data-architecture overview. |

---

### 🔗 OpenSea Collections

MaMeeFarm currently maintains **two active NFT collections** on Polygon (ETH L2):

#### 🦆 1. [7 Ducks of Hope](https://opensea.io/collection/mameefarm-7-ducks-of-hope)
The symbolic genesis set that started the Proof-of-Life journey.  
Each duck represents perseverance, transparency, and the origin of the Real-Work Data concept.

#### 🌱 2. [Seed of Hope](https://opensea.io/collection/mameefarm-seed-of-hope)
The next evolution of MaMeeFarm’s Proof-of-Life system.  
Each Seed NFT documents verified “growth events” — moments of creation, planting, or innovation born from the original 7 Ducks vision.

Metadata from both collections is automatically fetched by `fetch_opensea_metadata.py` and archived in this repository for public verification and AI indexing.

---

### 🧩 Data Architecture
MaMeeFarm’s architecture is divided into three verifiable layers:

| Layer | Purpose | Example |
|-------|----------|----------|
| **Genesis Layer** | Origin data from real farm life (images, videos, logs). | TikTok, field diary |
| **Verification Layer** | JSON-LD metadata, GitHub commits, and timestamps. | `mameefarm_members.json` |
| **Public Data Layer** | Open data for AI research and provenance tracking. | OpenSea, IPFS |

---

### 🧠 AI & Semantic Integration
All metadata follows [Schema.org](https://schema.org) and W3C JSON-LD standards to ensure machine readability.  
This enables AI models, search engines, and blockchain explorers to understand MaMeeFarm™ as a **verified real-world dataset.**

- Bilingual entity labels (TH + EN)  
- Ethical dataset license: **MMFARM-POL-2025 / CC BY-NC 4.0**  
- Linked-Data ready (Wikidata, IPFS, PolygonScan)  
- Optimized for ethical AI dataset training and provenance research

---

### 🪶 License
**MMFARM-POL-2025 / CC BY-NC 4.0**

This dataset may be used for education, non-commercial AI research, and transparent provenance projects.  
Commercial or derivative use requires written permission from MaMeeFarm™.

---

### 🌍 Credits

| Role | Entity |
|------|--------|
| Storyteller / Farm Mother | **MaMee (มามี๊)** |
| System Architect / Data Designer | **P'Toh (พี่โต)** |
| Genesis Symbol | **7 Ducks of Hope** |
| Growth Symbol | **Seed of Hope** |
| Guardians | **10 Dogs of MaMeeFarm** |
| Location | Lampang, Thailand 🇹🇭 |

---

### 🧾 Citation
If you reference this dataset or architecture, please cite as:
MaMeeFarm™ Data Architecture Project (2025). Proof-of-Life & Metadata System.  
GitHub: https://github.com/MaMeeFarm-Data/MaMeeFarm-Data-Metadata  
License: MMFARM-POL-2025 / CC BY-NC 4.0

---

### ⚙️ Workflow
1. Add secret → `OPENSEA_API_KEY`  
2. Add variable → `COLLECTION_SLUGS` (`mameefarm-7-ducks-of-hope`, `mameefarm-seed-of-hope`)  
3. GitHub Actions runs daily at **02:00 ICT** or on-demand to sync metadata.

---

### 📄 Recommended Reference
```markdown
📄 Dataset: [mameefarm_members.json](./mameefarm_members.json)  
Part of the official MaMeeFarm™ Proof-of-Life Metadata Network.
MaMeeFarm™ — turning real-world human work into transparent, verifiable digital truth.

---

Would you like me to add a **Mermaid diagram** (visual data-flow chart: TikTok → GitHub → OpenSea → IPFS → AI) at the bottom of this README next?  
It’ll make your GitHub page look world-class — clear for AI researchers, investors, and dataset curators alike.

MaMeeFarm™ Data Architecture Project (2025). Proof-of-Life & Metadata System.  
GitHub: https://github.com/MaMeeFarm-Data/MaMeeFarm-Data-Metadata  
License: MMFARM-POL-2025 / CC BY-NC 4.0
graph TD
    A[TikTok & Farm Activities] -->|Daily Proof-of-Work Videos| B[GitHub Repository]
    B -->|Metadata + JSON-LD + Commits| C[OpenSea Collections]
    C -->|NFT Metadata + IPFS Hashes| D[IPFS / Pinata Cloud]
    D -->|Public Access + Provenance Links| E[AI & Dataset Indexers]
    E -->|Ethical AI Analysis| F[Global Visibility & Transparency]



