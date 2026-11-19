#!/usr/bin/env python3
"""
Week 4 audit checks for the Product Compare Assistant (Topic 4 lab).

Reproduces the evidence used in docs/week4_data_quality_report.md.
It is a read-only check: it does not change or write any data file.

Default run (uses only files that are committed to the repository):
  python docs/week4_audit_checks.py

Optional full run (needs the full prepared S01 and S02 files, which are NOT committed):
  python docs/week4_audit_checks.py --full-meta data/processed/prepared_meta.jsonl \
                                    --full-reviews data/processed/prepared_reviews.jsonl
The full run turns the "Not Verified" items into results: reference integrity, review coverage
per product, duplicates, contact details in review text, and accessory-like titles.
"""
import argparse
import collections
import hashlib
import json
import re
import statistics
import unicodedata
from pathlib import Path

HEADPHONE_WORDS = re.compile(r"headphone|earphone|earbud|ear bud|headset|in-ear|in ear|iem|airpods|buds|monitors?", re.I)
ACCESSORY_WORDS = re.compile(r"\b(cable|case|cover|skin|adapter|adaptor|replacement|ear ?pads?|cushions?|stand|holder|wallet|splitter|extension|dongle|decal)\b", re.I)
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE = re.compile(r"(?<!\d)(?:\+?\d[\s().-]?){9,14}\d(?!\d)")
HTML_TAG = re.compile(r"<[^>]+>")
LIGATURES = re.compile("[\ufb00-\ufb06]")


def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def iter_jsonl(path):
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def not_blank(value):
    return isinstance(value, str) and value.strip() not in ("", "None")


def title(text):
    print("\n" + "=" * 8, text, "=" * 8)


def norm(text):
    return unicodedata.normalize("NFKC", text.replace("\xa0", " ")).lower()


def check_manifest(text_path, manifest_path):
    title("Provenance: file hash against the lineage manifest")
    manifest = json.load(open(manifest_path, encoding="utf-8"))
    actual = sha256(text_path)
    expected = {r["prepared_sha256"] for r in manifest["records"] if r["source_id"] in ("S03", "S04", "S05")}
    print("prepared_text.jsonl SHA-256:", actual)
    print("matches manifest (S03, S04, S05):", expected == {actual})
    return {r["source_id"]: r["source_sha256"] for r in manifest["records"]}


def check_v1(text_rows, meta_rows, review_rows, source_sha):
    title("V1 (FR4): every record has a usable source reference")
    bad_text = [r["record_id"] for r in text_rows if not (
        not_blank(r.get("source_id")) and not_blank(r.get("doi")) and not_blank(r.get("title"))
        and not_blank(r.get("licence")) and not_blank(r.get("text"))
        and isinstance(r.get("page"), int) and r["page"] >= 1
        and r.get("source_sha256") == source_sha.get(r.get("source_id")))]
    bad_meta = [r.get("record_id") for r in meta_rows if not (
        not_blank(r.get("record_id")) and not_blank(r.get("parent_asin")) and r.get("source_id") == "S01" and not_blank(r.get("title")))]
    bad_rev = [r.get("record_id") for r in review_rows if not (
        not_blank(r.get("record_id")) and not_blank(r.get("parent_asin")) and r.get("source_id") == "S02" and not_blank(r.get("text")))]
    print(f"text chunks: {len(text_rows) - len(bad_text)} pass / {len(text_rows)} tested; fails: {bad_text}")
    print(f"product records: {len(meta_rows) - len(bad_meta)} pass / {len(meta_rows)} tested; fails: {bad_meta}")
    print(f"review records: {len(review_rows) - len(bad_rev)} pass / {len(review_rows)} tested; fails: {bad_rev}")


def screen_titles(rows):
    """Keyword screen for non-headphone products. It only nominates items for manual review."""
    flagged = []
    for r in rows:
        t = r.get("title") or ""
        if ACCESSORY_WORDS.search(t) or not HEADPHONE_WORDS.search(t):
            flagged.append(r)
    return flagged


def check_v2(meta_rows):
    title("V2 (FR1): each prepared product is a headphone product (screen, then manual review)")
    flagged = screen_titles(meta_rows)
    print(f"keyword screen nominated {len(flagged)} of {len(meta_rows)} product titles for manual review:")
    for r in flagged:
        print(f"  {r['parent_asin']} [{r.get('subtype')}] {r['title'][:90]}")
    print("Manual judgement is needed: the screen also nominates real headphones (for example, titles that mention a charging case).")
    no_text = [r["parent_asin"] for r in meta_rows if not (r.get("has_features") or r.get("has_description"))]
    print(f"products with neither features nor description: {len(no_text)} of {len(meta_rows)}: {no_text}")


def check_text(text_rows):
    title("Text corpus: duplicates, noise, ligatures, term coverage")
    ids = [r["record_id"] for r in text_rows]
    texts = [r["text"].strip().lower() for r in text_rows]
    print("duplicate record_id:", len(ids) - len(set(ids)), "| duplicate chunk text:", len(texts) - len(set(texts)))
    per_source = collections.Counter(r["source_id"] for r in text_rows)
    print("chunks per source:", dict(per_source))
    lens = [len(r["text"]) for r in text_rows]
    print("chunk length min/median/max:", min(lens), statistics.median(lens), max(lens), "| under 200 chars:", sum(n < 200 for n in lens))

    lig_chunks = [r for r in text_rows if LIGATURES.search(r["text"])]
    lig_chars = sum(len(LIGATURES.findall(r["text"])) for r in text_rows)
    print(f"chunks with ligature characters: {len(lig_chunks)} of {len(text_rows)} ({lig_chars} characters)",
          dict(collections.Counter(r["source_id"] for r in lig_chunks)))
    print("  chunks containing 'filter':", sum("filter" in r["text"].lower() for r in text_rows),
          "| containing the ligature spelling:", sum("\ufb01lter" in r["text"].lower() for r in text_rows))

    emails = [r["record_id"] for r in text_rows if EMAIL.search(r["text"])]
    phones = [r["record_id"] for r in text_rows if re.search(r"(Tel\.?:|Phone:)", r["text"])]
    print("chunks with an email address:", emails, "| with a phone label:", phones)

    def nonletter(t):
        return 1 - sum(c.isalpha() for c in t) / max(len(t), 1)
    noisy = [(r["record_id"], round(nonletter(r["text"]), 2)) for r in text_rows if nonletter(r["text"]) >= 0.4]
    print("chunks with at least 40% non-letter characters (figure or table text):", noisy)
    back = [r["record_id"] for r in text_rows if re.search(r"Conflicts? of Interest|Conflicts? of interest|Author Contributions|Abbreviations", r["text"])]
    print("back-matter chunks:", back)

    terms = {
        "frequency response": r"frequency response", "distortion": r"distortion", "noise cancelling": r"noise[- ]cancel|active noise",
        "impedance": r"impedance", "driver": r"\bdrivers?\b", "bass": r"\bbass\b", "treble": r"\btreble\b",
        "equalization": r"equali[sz]", "open/closed-back": r"open[- ]back|closed[- ]back|closed headphones|open headphones",
        "bluetooth / codec": r"bluetooth|codec",
    }
    print("term coverage (chunks, after Unicode normalisation):")
    for name, rx in terms.items():
        per = {s: sum(bool(re.search(rx, norm(r["text"]))) for r in text_rows if r["source_id"] == s) for s in ("S03", "S04", "S05")}
        print(f"  {name:20s} total {sum(per.values()):3d} {per}")
    health = [r["record_id"] for r in text_rows if r["source_id"] == "S03" and re.search(r"health|radiation|cancer|hearing|tinnitus", norm(r["text"]))]
    print(f"S03 chunks with health-related words: {len(health)} of {per_source.get('S03', 0)}")


def check_samples(meta_rows, review_rows):
    title("Samples: completeness, consistency, hygiene")
    n = len(meta_rows)
    print(f"product sample n={n}: has_features {sum(r['has_features'] for r in meta_rows)}, has_description {sum(r['has_description'] for r in meta_rows)}, "
          f"has_price {sum(r['has_price'] for r in meta_rows)}, details parsed {sum(r['details_parsed'] for r in meta_rows)}")
    print("  subtype:", dict(collections.Counter(r["subtype"] for r in meta_rows)))
    print("  distinct parent_asin:", len({r["parent_asin"] for r in meta_rows}), "| distinct stores:", len({r["store"] for r in meta_rows}))
    counts = [r["rating_number"] for r in meta_rows]
    print("  rating_number min/median/max:", min(counts), statistics.median(counts), max(counts))
    print(f"review sample n={len(review_rows)}: user_id present {sum('user_id' in r for r in review_rows)}, "
          f"HTML tags left {sum(bool(HTML_TAG.search(r['text'])) for r in review_rows)}, empty text {sum(not r['text'].strip() for r in review_rows)}")
    print("  rating distribution:", dict(sorted(collections.Counter(r["rating"] for r in review_rows).items())))
    dates = [r["review_date_utc"] for r in review_rows if r.get("review_date_utc")]
    print("  review dates:", min(dates), "to", max(dates))
    print("  asin differs from parent_asin:", sum(r["asin"] != r["parent_asin"] for r in review_rows), "of", len(review_rows))
    shared = {r["parent_asin"] for r in review_rows} & {r["parent_asin"] for r in meta_rows}
    print("  review products found in the product sample:", len(shared), "(the two samples are the first rows of different files, so this is not a join test)")


def check_full(meta_path, review_path):
    title("FULL FILES: reference integrity, review coverage, duplicates, contact details")
    products = {}
    accessory_like = 0
    total = 0
    for rec in iter_jsonl(meta_path):
        total += 1
        products[rec["parent_asin"]] = rec
        if rec.get("title") and (ACCESSORY_WORDS.search(rec["title"]) or not HEADPHONE_WORDS.search(rec["title"])):
            accessory_like += 1
    print(f"products: {total} records, {len(products)} distinct parent_asin")
    print(f"titles nominated by the accessory screen: {accessory_like} ({accessory_like / max(total, 1):.1%}); confirm a random 50 by hand")

    reviews = 0
    orphans = 0
    per_product = collections.Counter()
    text_seen = collections.Counter()
    html_left = emails = phones = 0
    ratings = collections.Counter()
    for rec in iter_jsonl(review_path):
        reviews += 1
        pid = rec["parent_asin"]
        if pid not in products:
            orphans += 1
        else:
            per_product[pid] += 1
        text_seen[(pid, rec["text"])] += 1
        html_left += bool(HTML_TAG.search(rec["text"]))
        emails += bool(EMAIL.search(rec["text"]))
        phones += bool(PHONE.search(rec["text"]))
        ratings[rec["rating"]] += 1
    print(f"reviews: {reviews}; orphan reviews (parent_asin not in products): {orphans}")
    with_reviews = len(per_product)
    print(f"products with at least one review: {with_reviews} of {len(products)} ({with_reviews / max(len(products), 1):.1%}); without: {len(products) - with_reviews}")
    dup = sum(c - 1 for c in text_seen.values() if c > 1)
    print(f"duplicate reviews (same product and same text): {dup}")
    print(f"reviews with HTML tags left: {html_left} | with an email address: {emails} | with a phone-like number: {phones}")
    print("rating distribution:", {k: f"{v / max(reviews, 1):.1%}" for k, v in sorted(ratings.items())})
    groups = {"1-9 ratings": 0, "10-99 ratings": 0, "100+ ratings": 0}
    seen = {k: {"n": 0, "with": 0} for k in groups}
    for pid, rec in products.items():
        rn = rec.get("rating_number") or 0
        key = "1-9 ratings" if rn < 10 else "10-99 ratings" if rn < 100 else "100+ ratings"
        seen[key]["n"] += 1
        seen[key]["with"] += pid in per_product
    for key, v in seen.items():
        print(f"  review coverage, products with {key}: {v['with']} of {v['n']} ({v['with'] / max(v['n'], 1):.1%})")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--text", default="data/processed/prepared_text.jsonl")
    parser.add_argument("--meta", default="data/samples/prepared_meta_sample.jsonl")
    parser.add_argument("--reviews", default="data/samples/prepared_reviews_sample.jsonl")
    parser.add_argument("--manifest", default="data/week3_manifest.json")
    parser.add_argument("--full-meta")
    parser.add_argument("--full-reviews")
    args = parser.parse_args()

    text_rows, meta_rows, review_rows = read_jsonl(args.text), read_jsonl(args.meta), read_jsonl(args.reviews)
    source_sha = check_manifest(args.text, args.manifest)
    check_v1(text_rows, meta_rows, review_rows, source_sha)
    check_v2(meta_rows)
    check_text(text_rows)
    check_samples(meta_rows, review_rows)
    if args.full_meta and args.full_reviews:
        check_full(args.full_meta, args.full_reviews)
    else:
        print("\n(Full-file checks skipped. Pass --full-meta and --full-reviews to run them.)")


if __name__ == "__main__":
    main()
