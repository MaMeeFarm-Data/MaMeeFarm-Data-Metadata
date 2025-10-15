import os, json, requests, pathlib

API_KEY = os.environ["OPENSEA_API_KEY"]
SLUGS = [s.strip() for s in os.environ.get("COLLECTION_SLUGS","").split(",") if s.strip()]
CONTRACTS = [c.strip() for c in os.environ.get("CONTRACT_ADDRESSES","").split(",") if c.strip()]
CHAIN = "matic"

OUT = pathlib.Path("data"); OUT.mkdir(exist_ok=True)

S = requests.Session()
S.headers.update({"accept":"application/json","x-api-key":API_KEY})

def save(nft):
    contract = nft.get("contract",{}).get("address","unknown")
    token_id = nft.get("identifier","unknown")
    path = OUT / contract / f"{token_id}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path,"w",encoding="utf-8") as f:
        json.dump(nft,f,ensure_ascii=False,indent=2)

def fetch_slug(slug):
    url = f"https://api.opensea.io/api/v2/collection/{slug}/nfts"
    r = S.get(url, params={"limit":50})
    if r.status_code == 404:
        print(f"[404] slug not found: {slug}")
        return
    r.raise_for_status()
    for nft in r.json().get("nfts", []):
        save(nft)

def fetch_contract(addr):
    url = f"https://api.opensea.io/api/v2/chain/{CHAIN}/contract/{addr}/nfts"
    r = S.get(url, params={"limit":50})
    if r.status_code == 404:
        print(f"[404] contract not found: {addr}")
        return
    r.raise_for_status()
    for nft in r.json().get("nfts", []):
        save(nft)

for s in SLUGS: fetch_slug(s)
for c in CONTRACTS: fetch_contract(c)
