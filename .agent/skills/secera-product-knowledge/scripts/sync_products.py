#!/usr/bin/env python3
"""
SECERA Product Catalog Sync Utility
Fetches real-time product knowledge, variants, size guides, and materials from
https://secera.id/api/products and updates reference files for the Gemini skill.
"""

import os
import sys
import json
import ssl
import re
import urllib.request
from datetime import datetime

API_URL = "https://secera.id/api/products"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(SKILL_DIR, "data")
REFERENCES_DIR = os.path.join(SKILL_DIR, "references")
RAW_DATA_PATH = os.path.join(DATA_DIR, "products_raw.json")
CATALOG_MD_PATH = os.path.join(REFERENCES_DIR, "product_catalog_matrix.md")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REFERENCES_DIR, exist_ok=True)

def fetch_products():
    print(f"[*] Fetching products from {API_URL}...")
    ctx = ssl._create_unverified_context()
    req = urllib.request.Request(
        API_URL,
        headers={"User-Agent": "SECERA-Knowledge-Sync/1.0 (Gemini Skill Automation)"}
    )
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            content = resp.read().decode("utf-8")
            data = json.loads(content)
            print(f"[+] Successfully fetched {len(data)} products from live API.")
            with open(RAW_DATA_PATH, "w", encoding="utf-8") as f:
                f.write(json.dumps(data, indent=2, ensure_ascii=False))
            return data
    except Exception as e:
        print(f"[-] Failed to fetch from live API: {e}")
        if os.path.exists(RAW_DATA_PATH):
            print("[*] Loading from cached products_raw.json...")
            with open(RAW_DATA_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        raise RuntimeError(f"Unable to fetch live or cached data: {e}")

def clean_html(text):
    if not text:
        return ""
    # Replace paragraphs and linebreaks
    text = re.sub(r'</p>\s*<p>', '\n\n', text)
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<li>', '- ', text)
    text = re.sub(r'</li>', '\n', text)
    # Strip remaining HTML tags
    clean = re.sub(r'<[^>]+>', '', text)
    return clean.strip()

def format_rupiah(val):
    try:
        num = float(val)
        return f"Rp {num:,.0f}".replace(",", ".")
    except (ValueError, TypeError):
        return str(val)

def generate_catalog_markdown(products):
    active_products = [p for p in products if p.get("status") == "active"]
    archived_products = [p for p in products if p.get("status") != "active"]

    now = datetime.now().strftime("%Y-%m-%d %H:%M WIB")

    md = []
    md.append("# SECERA Live Product Catalog Matrix")
    md.append(f"> Auto-generated from `https://secera.id/api/products` on {now}.")
    md.append("> Official reference for Gemini Skill: `secera-product-knowledge`\n")
    md.append("---")
    md.append("\n## 1. Quick Catalog Overview (Active Collection)\n")
    md.append("| Produk | Kategori | Material | Varian / Warna | Rentang Harga | Size Guide | Status |")
    md.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")

    for p in active_products:
        name = p.get("short_name") or p.get("name", "Tanpa Nama")
        cat = p.get("category", "General")
        mat = p.get("material", "N/A")
        variants = p.get("product_variants", [])
        colors = sorted(list(set([v.get("color") for v in variants if v.get("color")])))
        color_str = f"{len(colors)} warna" if colors else f"{len(variants)} varian"

        prices = [float(v["price"]) for v in variants if v.get("price")]
        promo_prices = [float(v["promo_price"]) for v in variants if v.get("promo_price")]

        min_p = min(promo_prices) if promo_prices else (min(prices) if prices else 0)
        max_p = max(prices) if prices else 0
        price_range = f"{format_rupiah(min_p)} - {format_rupiah(max_p)}" if min_p != max_p else format_rupiah(min_p)

        has_sg = bool(p.get("cms_content", {}).get("size_guide", {}).get("rows"))
        sg_badge = "✅ Ada" if has_sg else "—"

        md.append(f"| **{name}** | `{cat}` | {mat} | {color_str} | {price_range} | {sg_badge} | `Active` |")

    md.append("\n---\n")
    md.append("## 2. Deep-Dive Product Knowledge Cards\n")

    for idx, p in enumerate(active_products, 1):
        name = p.get("name")
        short_name = p.get("short_name") or name
        slug = p.get("slug")
        cat = p.get("category")
        mat = p.get("material")
        weight = p.get("weight", "200")
        desc = clean_html(p.get("description", ""))
        variants = p.get("product_variants", [])
        colors = sorted(list(set([v.get("color") for v in variants if v.get("color")])))
        shopee = p.get("shopee_link")
        tiktok = p.get("tiktok_link")

        md.append(f"### {idx}. {name}")
        md.append(f"- **Short Name**: `{short_name}` | **Kategori**: `{cat}` | **Status**: Active")
        md.append(f"- **URL Toko**: [secera.id/shop/{slug}](https://secera.id/shop/{slug})")
        if shopee:
            md.append(f"- **Shopee**: [Link Produk]({shopee})")
        if tiktok and tiktok.startswith("http"):
            md.append(f"- **TikTok Shop**: [Link Produk]({tiktok})")
        md.append(f"- **Material Utama**: **{mat}** (Berat: {weight} gram)")
        md.append(f"- **Pilihan Warna ({len(colors)})**: {', '.join([c.title() for c in colors]) if colors else 'All Variant'}")

        # Variant breakdown table
        if variants:
            md.append("\n**Daftar Varian & Harga:**")
            md.append("| SKU | Opsi / Ukuran | Warna | Harga Normal | Harga Promo | Stok |")
            md.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
            # Limit display to top 15 if too many (e.g. 86 variants)
            display_variants = variants[:15]
            for v in display_variants:
                sku = v.get("sku", "-")
                opt = v.get("option_name", "Standar")
                col = (v.get("color") or "-").title()
                pr = format_rupiah(v.get("price", 0))
                promo = format_rupiah(v.get("promo_price", 0)) if v.get("promo_price") else "-"
                stock = v.get("stock", 0)
                md.append(f"| `{sku}` | {opt} | {col} | {pr} | **{promo}** | {stock} |")
            if len(variants) > 15:
                md.append(f"| *...dan {len(variants) - 15} varian warna lainnya* | | | | | |")

        # Size guide table if present
        sg = p.get("cms_content", {}).get("size_guide", {})
        if sg and sg.get("rows") and sg.get("columns"):
            cols = sg["columns"]
            rows = sg["rows"]
            md.append("\n**Panduan Ukuran (Size Chart):**")
            header = "| Ukuran | " + " | ".join([c["label"] for c in cols]) + " |"
            sep = "| :--- | " + " | ".join([":---:" for _ in cols]) + " |"
            md.append(header)
            md.append(sep)
            for r in rows:
                size_label = r.get("size", "All Size")
                vals = [str(r.get("values", {}).get(c["key"], "-")) for c in cols]
                md.append(f"| **{size_label}** | " + " | ".join(vals) + " |")

        # Material Accordion if present
        acc_mat = p.get("cms_content", {}).get("accordions", {}).get("material")
        if acc_mat:
            clean_acc = clean_html(acc_mat)
            md.append(f"\n**Catatan Material Tambahan:**\n> {clean_acc}")

        # Description excerpt
        if desc:
            # take first 400 chars of description
            desc_snippet = desc[:500].replace("\n\n", " ").strip()
            md.append(f"\n**Deskripsi & Filosofi Produk:**\n> {desc_snippet}...")

        md.append("\n" + "-" * 40 + "\n")

    if archived_products:
        md.append("\n## 3. Koleksi Terdahulu / Arsip (Archived Reference)\n")
        md.append("> Berguna untuk konteks riwayat produk, upgrade siluet, atau pertanyaan pelanggan lama.\n")
        md.append("| Produk | Material | Varian | Alasan Status |")
        md.append("| :--- | :--- | :--- | :--- |")
        for p in archived_products:
            name = p.get("name")
            mat = p.get("material", "N/A")
            v_cnt = len(p.get("product_variants", []))
            md.append(f"| {name} | {mat} | {v_cnt} varian | Arsip / Koleksi Musim Lalu |")

    return "\n".join(md)

def main():
    try:
        products = fetch_products()
        markdown_content = generate_catalog_markdown(products)
        with open(CATALOG_MD_PATH, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"[+] Successfully generated catalog markdown at: {CATALOG_MD_PATH}")
    except Exception as e:
        print(f"[!] Error syncing catalog: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
