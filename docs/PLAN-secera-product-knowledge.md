# PLAN-secera-product-knowledge.md

Implementation plan for creating a specialized Gemini Skill: `secera-product-knowledge`. This skill equips the AI with deep domain expertise regarding SECERA's product catalog, materials, brand vision, value proposition, and objective advantages/disadvantages sourced from [secera.id/shop](https://secera.id/shop), `https://secera.id/api/products`, and existing brand foundation blueprints.

---

## 1. Overview

SECERA is Indonesia's pioneer in effortless occasion wear—originating as the creator of the Instant Selendang and evolving into a modular Occasion Wear System.

The purpose of this skill is to allow Gemini (and AI agents operating on SECERA projects) to:
- Act as an authoritative **SECERA Product Specialist & Stylist**.
- Provide exact product recommendations, sizing advice, and mix-and-match pairings from the live catalog.
- Explain fabric qualities, care instructions, and material distinctions with precision.
- Articulate the brand vision ("Tampil siap bukan soal waktu yang panjang. Tapi soal pilihan yang tepat") and value proposition without generic marketing buzzwords.
- Accurately state product advantages, care nuances, and limitations (disadvantages/trade-offs) to maintain transparency and customer trust.

---

## 2. Project Type & Agent Assignments

- **Project Type**: Gemini Skill / Knowledge System Architecture
- **Primary Agents**:
  - `project-planner`: Requirements architecture, task sequencing, and verification planning.
  - `backend-specialist`: Catalog extraction script (`sync_products.py`) communicating with `https://secera.id/api/products`.
  - `frontend-specialist`: Formatting the skill knowledge base, visual styling tokens, and persona-guided conversation trees.

---

## 3. Success Criteria & Confirmed User Specifications

Based on the Socratic Gate alignment:
1. **Dual Deployment Format**:
   - **Antigravity IDE Workspace Skill**: Installed at `.agent/skills/secera-product-knowledge/SKILL.md` for AI pair-programming and workspace agents.
   - **Standalone Gemini Gem System Instruction**: Exported at `export/GEMINI_GEM_SYSTEM_INSTRUCTION.md` ready to copy-paste directly into Google Gemini Web / Custom Gems.
2. **Comprehensive Dual-Role Coverage**:
   - **Customer Stylist & Sales Advisor**: Immediate product recommendations, size matching (lingkar dada/pinggang), mix-and-match combos, and transparent objection handling (honest fabric pros/cons).
   - **Brand Editorial & Copywriting Specialist**: Storytelling aligned with SECERA's 6 content pillars, aesthetic guidelines ("Zero Radius", Caslon/Inter), and brand guardrails (no cheap words like "murah" / "kece badai").
3. **Dynamic Catalog Ingestion + Curated Knowledge**:
   - Curated reference markdown files capturing core vision, materials, advantages, and limitations.
   - Reusable sync utility (`scripts/sync_products.py`) that queries `https://secera.id/api/products` (and local DB fallback) to keep product names, SKUs, colors, prices, and size charts synchronized.

---

## 4. File Structure

```
.agent/skills/secera-product-knowledge/
├── SKILL.md                               # Main Gemini Skill entrypoint & instruction contract
├── references/
│   ├── brand_vision_and_value_prop.md     # Vision, positioning, emotional journey, tone of voice
│   ├── materials_and_care_guide.md        # Fabric profiles, breathability, opacity, washing guide
│   ├── product_catalog_matrix.md          # Live product catalog (SKUs, variants, prices, size charts)
│   ├── pros_cons_and_objections.md        # Advantages, limitations, customer objection playbooks
│   └── styling_and_pairing_rules.md       # Occasion system, mix-and-match formulas, color palettes
├── scripts/
│   └── sync_products.py                   # Automated scraper/fetcher from https://secera.id/api/products
└── export/
    └── GEMINI_GEM_SYSTEM_INSTRUCTION.md   # Standalone copy-paste prompt for Google Gemini Web / Gems
```

---

## 5. Architectural & Knowledge Breakdown

### A. Brand Vision & Value Proposition
- **Category**: *Indonesia's Effortless Occasion Wear Brand*
- **Brand Purpose**: Accelerate buying decisions from discovery (TikTok/Instagram) to checkout without friction, while maintaining a high-class, accessible perception.
- **Core Value Proposition**:
  - *Zero-Effort Elegance*: "Tinggal pakai. Langsung terlihat niat."
  - *Instant Preparedness*: Rapid conversion from panic (H-1/H-0 event) to calm confidence.
  - *Modular Occasion System*: Versatile pieces that can be worn across 3+ distinct events (kondangan, bridesmaid, wisuda, kantor) with simple re-styling.
  - *Camera-Friendly Drape*: Soft-drape fabrics designed to look photogenic under flash and natural lighting without tacky sheen.

### B. Materials & Fabric Science
| Material | Products Used In | Characteristics | Advantages | Disadvantages / Care Rules |
| :--- | :--- | :--- | :--- | :--- |
| **Ceruty Babydoll Premium** | AIRA Top, KIRANA Set, Selendang Instant | Grainy georgette texture, exceptional flowing drape, lightweight | Elegant fluid drape, airy, wrinkle-resistant | Requires full inner lining (furing) to avoid transparency; sensitive to high heat ironing (steamer recommended). |
| **Satin Maxmara Premium** | PUSPA Kebaya Kutubaru | Soft matte luster, silky touch, breathable, non-stiff | Luxurious silk-like sheen without looking greasy/cheap; cool on skin | Needs gentle hand wash; iron with silk temperature setting on reverse side. |
| **Songket Tenun Motif** | ARUM Wrap Skirt & Selendang | Textured jacquard weave with metallic/ethnic motifs, structured form | Retains silhouette, instantly elevates simple tops to royal/formal event standard | Stiffer than ceruty, dry-clean or gentle soak only, cannot be machine wrung. |

### C. Advantages vs. Disadvantages (Objective Analysis)
- **Advantages**:
  - Pre-styled / Instant draping removes need for safety pins (jarum pentul) and tailor visits.
  - Flexible sizing (All-Size wrap skirts and adjustable silhouettes fit sizes S through XL).
  - High perceived luxury at accessible direct-to-consumer prices (Rp 70.000 – Rp 230.000).
- **Disadvantages & Operational Nuances**:
  - Color calibration: Screen vs. physical fabric has a natural 5–10% variance depending on indoor lighting.
  - Care requirements: Delicate fabrics must be steamed rather than hot-pressed.
  - Seasonal scope: Tailored specifically for tropical occasion/formal wear, not winter or sports-casual wear.

---

## 6. Detailed Task Breakdown

### Task 1: Product Catalog Data Extraction
- **Task ID**: `TASK-SPK-01`
- **Agent**: `backend-specialist`
- **Skills**: `nodejs-best-practices`, `clean-code`
- **Priority**: P0
- **Dependencies**: None
- **INPUT**: Live API endpoint `https://secera.id/api/products` + database schema.
- **OUTPUT**: Complete product JSON dump & catalog markdown generator (`sync_products.py`).
- **VERIFY**: Run `python .agent/skills/secera-product-knowledge/scripts/sync_products.py` and verify all active products are saved with variants, prices, and specs.

### Task 2: Brand Vision & Value Proposition Synthesis
- **Task ID**: `TASK-SPK-02`
- **Agent**: `frontend-specialist`
- **Skills**: `clean-code`, `frontend-design`
- **Priority**: P0
- **Dependencies**: None
- **INPUT**: `docs/Brand Strategy/secera_brand_foundation.html`, `PRODUCT.md`, `SECERA_EDITORIAL_SKILL.md`.
- **OUTPUT**: `references/brand_vision_and_value_prop.md`.
- **VERIFY**: Check coverage of 3 personas, emotional journey, tone of voice boundaries (banned words like "murah", "kece badai"), and core manifesto.

### Task 3: Material Science & Fabric Care Guide
- **Task ID**: `TASK-SPK-03`
- **Agent**: `frontend-specialist`
- **Skills**: `clean-code`
- **Priority**: P1
- **Dependencies**: `TASK-SPK-01`
- **INPUT**: Fabric definitions from product catalog and brand guides.
- **OUTPUT**: `references/materials_and_care_guide.md`.
- **VERIFY**: Validate fabric behavior descriptions (Ceruty Babydoll, Satin Maxmara, Songket) and customer washing/steaming guidance.

### Task 4: Product Catalog Matrix with Pros & Cons
- **Task ID**: `TASK-SPK-04`
- **Agent**: `frontend-specialist`
- **Skills**: `clean-code`
- **Priority**: P1
- **Dependencies**: `TASK-SPK-01`, `TASK-SPK-03`
- **OUTPUT**: `references/product_catalog_matrix.md` and `references/pros_cons_and_objections.md`.
- **VERIFY**: Ensure each SKU has defined strengths, limitations, ideal occasions, and customer objection answers.

### Task 5: Master Skill & Standalone Gemini Gem Export
- **Task ID**: `TASK-SPK-05`
- **Agent**: `project-planner`
- **Skills**: `plan-writing`, `clean-code`
- **Priority**: P1
- **Dependencies**: `TASK-SPK-01` through `TASK-SPK-04`
- **OUTPUT**:
  - `.agent/skills/secera-product-knowledge/SKILL.md`
  - `.agent/skills/secera-product-knowledge/export/GEMINI_GEM_SYSTEM_INSTRUCTION.md`
- **VERIFY**: Validate YAML frontmatter, links to references, prompt triggers, and test Q&A responses against sample customer queries.

---

## 7. Phase X: Verification Checklist

- [x] All active products from `https://secera.id/api/products` are indexed in the catalog matrix.
- [x] Brand tone guardrails strictly enforced (no banned words, no cheap phrasing).
- [x] Material care instructions accurate for silk/satin/ceruty.
- [x] Advantages & disadvantages balanced and objective.
- [x] YAML frontmatter valid and adheres to Antigravity / Gemini skill standards.
- [x] Standalone export file tested for Google Gemini Web / Gems compatibility.

## ✅ PHASE X COMPLETE
- **Catalog Sync**: ✅ 21 products ingested & parsed from `https://secera.id/api/products` via `scripts/sync_products.py`
- **Brand Guardrails**: ✅ Tone of voice strictly aligned with "Zero-Radius" aesthetic & non-salesy language
- **Fabric Science**: ✅ Comprehensive coverage of Ceruty Babydoll, Satin Maxmara, and Songket Tenun
- **Artifacts Generated**:
  - [.agent/skills/secera-product-knowledge/SKILL.md](file:///Users/juniobagus/Project/secera%20site/SECERA-Site/.agent/skills/secera-product-knowledge/SKILL.md)
  - [.agent/skills/secera-product-knowledge/references/brand_vision_and_value_prop.md](file:///Users/juniobagus/Project/secera%20site/SECERA-Site/.agent/skills/secera-product-knowledge/references/brand_vision_and_value_prop.md)
  - [.agent/skills/secera-product-knowledge/references/materials_and_care_guide.md](file:///Users/juniobagus/Project/secera%20site/SECERA-Site/.agent/skills/secera-product-knowledge/references/materials_and_care_guide.md)
  - [.agent/skills/secera-product-knowledge/references/product_catalog_matrix.md](file:///Users/juniobagus/Project/secera%20site/SECERA-Site/.agent/skills/secera-product-knowledge/references/product_catalog_matrix.md)
  - [.agent/skills/secera-product-knowledge/references/pros_cons_and_objections.md](file:///Users/juniobagus/Project/secera%20site/SECERA-Site/.agent/skills/secera-product-knowledge/references/pros_cons_and_objections.md)
  - [.agent/skills/secera-product-knowledge/references/styling_and_pairing_rules.md](file:///Users/juniobagus/Project/secera%20site/SECERA-Site/.agent/skills/secera-product-knowledge/references/styling_and_pairing_rules.md)
  - [.agent/skills/secera-product-knowledge/scripts/sync_products.py](file:///Users/juniobagus/Project/secera%20site/SECERA-Site/.agent/skills/secera-product-knowledge/scripts/sync_products.py)
  - [.agent/skills/secera-product-knowledge/export/GEMINI_GEM_SYSTEM_INSTRUCTION.md](file:///Users/juniobagus/Project/secera%20site/SECERA-Site/.agent/skills/secera-product-knowledge/export/GEMINI_GEM_SYSTEM_INSTRUCTION.md)
- **Date**: 2026-11-02
