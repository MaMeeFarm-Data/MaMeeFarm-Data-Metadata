# 🦆 MaMeeFarm™ — OpenSea Metadata Sync

Daily job that fetches NFT metadata from MaMeeFarm’s OpenSea collections and archives them in `/data/`.
Part of the **Proof-of-Work Farm Data Architecture**.

## Setup
1) Add secret `OPENSEA_API_KEY`
2) Add variable `COLLECTION_SLUGS` (e.g. `mameefarm` or `mameefarm,seven-ducks-of-hope`)
3) Workflow runs daily (02:00 ICT) or on demand.

© 2025 MaMeeFarm Digital Assets — License: MaMeeFarm™ Proof-of-Work Data License (see `LICENSE`)
