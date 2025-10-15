#!/usr/bin/env python3
import os, json, time, pathlib, requests

API_KEY = os.environ["OPENSEA_API_KEY"]
SLUGS = [s.strip() for s in os.environ.get("COLLECTION_SLUGS","").split(",") if s.strip()]
OUT = pathlib.Path("data"); OUT.mkdir(exist_ok=True, parents=True)

S = requests.Session()
S.headers.update({"accept":"application/json","x-api-key":API_KEY})

def save(nft):
    contract = (nft.get("contract") or {}).get("address","unknown").lower()
    token_id = nft.get("identifier","unknown")
    p = OUT / contract / f"{token_id}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p,"w",encoding="utf-8") as f:
        json.dump(nft, f, ensure_ascii=False, indent=2)

def fetch(slug):
    url = f"https://api.opensea.io/api/v2/collection/{slug}/nfts"
    nxt, total = None, 0
    while True:
        params = {"limit":100}
        if nxt: params["next"] = nxt
        r = S.get(url, params=params, timeout=45)
        r.raise_for_status()
        data = r.json()
        for nft in data.get("nfts", []):
            save(nft); total += 1
        nxt = data.get("next")
        if not nxt: break
        time.sleep(0.2)
    print(f"[{slug}] saved {total} items")

if __name__ == "__main__":
    for slug in SLUGS: fetch(slug)
