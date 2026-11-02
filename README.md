# SECERA Marketing & AI Brand Ecosystem

> **Official AI Knowledge Base, Brand Guardrails, & Occasion Styling Skills for SECERA (https://secera.id)**  
> Repositori resmi tim pemasaran, penulisan konten editorial, strategi merek, dan integrasi kecerdasan buatan (AI) Google Gemini & Antigravity IDE.

---

## 🏛️ 1. Ikhtisar Repositori (Repository Overview)

Repositori ini memisahkan seluruh pengetahuan merek, aturan gaya bahasa, sistem visual, dan kurasi produk SECERA dari basis kode teknis website (`SECERA-Site`). Tujuannya adalah memberikan satu sumber kebenaran (*single source of truth*) yang rapi bagi tim kreatif, copywriter, agen AI, dan bot percakapan Google Gemini.

```
SECERA Marketing Team/
├── .agents/skills/                        # Format resmi Antigravity IDE Workspace Skills
│   ├── secera-brand-master/               # Skill Pengarah Merek, Tone of Voice, & Strategi
│   └── secera-product-knowledge/          # Skill Spesialis Produk, Bahan Kain, & Size Guide
├── docs/
│   └── Brand Strategy/                    # Arsip cetak biru resmi (Manifesto, Fondasi, & Copywriting)
├── export/                                # Prompt mandiri siap copy-paste ke Google Gemini Gems
│   ├── GEMINI_GEM_BRAND_MASTER.md         # System Instruction untuk Gem: "Brand Guardian & Creative Director"
│   └── GEMINI_GEM_PRODUCT_SPECIALIST.md   # System Instruction untuk Gem: "Occasion Stylist & Product Specialist"
├── scripts/
│   └── sync_products.py                   # Utilitas otomatis sinkronisasi katalog dari secera.id API
└── README.md
```

---

## 💎 2. Dua Skill Utama SECERA

### A. `secera-brand-master` (Brand Guardian & Creative Director)
Mengawal identitas merek, strategi komunikasi, dan standar visual:
- **Esensi Merek:** *"Tampil siap bukan soal waktu yang panjang. Tapi soal pilihan yang tepat."*
- **Filosofi:** *"Elegance is a decision, not a process"* dan *"Tinggal pakai. Langsung terlihat niat."*
- **Tiga Persona Konsumen:**
  1. *The Last-Minute Woman (Hero Audience)* — Panik H-1 kondangan mendadak.
  2. *The Bridesmaid Friend (Group Driver)* — Seragam sahabat satu geng warna serasi tanpa drama ukuran.
  3. *The Polished Professional (Repeat Buyer)* — Transisi mulus dari kantor sore ke dinner malam.
- **Enam Pilar Konten:** *No Time Still Stunning*, *Repeat Without Notice*, *Look Expensive*, *Real Girl Moments*, *The SECERA Effect*, dan *The Occasion System*.
- **Doktrin Visual "Zero Radius":** Sudut arsitektural serba tajam (`border-radius: 0px`), tipografi **Libre Caslon Display + Inter**, dan palet warna wibawa **`Brand Wine #722F38`**.

### B. `secera-product-knowledge` (Product Specialist & Occasion Stylist)
Menyimpan data teknis busana dan kecerdasan konsultasi pelanggan:
- **Katalog Lengkap (21 Produk):** *AIRA Blouse Peplum*, *PUSPA Kebaya Kutubaru*, *ARUM Wrap Skirt Songket*, *LARAS Skirt*, *VERSA Set*, dan rangkaian *Selendang Instant* (Malay Pashmina, Layer Series, Lurus).
- **Ilmu Material Tekstil (Textile Science):** Analisis kejatuhan kain (*flowy drape*), kenyamanan cuaca tropis, opasitas (*full soft furing* anti-menerawang), dan instruksi pencucian/steamer resmi untuk **Ceruty Babydoll**, **Satin Maxmara Premium**, dan **Songket Tenun Jacquard**.
- **Playbook Penanganan Keraguan (Objection Handling):** Jawaban jujur dan terstandarisasi untuk pertanyaan umum (menerawang, muat untuk BB 70kg, toleransi warna foto vs fisik, kecepatan kirim instant H-1).
- **Formula Padu-Padan (The Occasion System):** Paduan busana untuk *The Royal Reception*, *The Modern Bridesmaid*, *The Timeless Graduation*, hingga *Desk-to-Dinner*.

---

## 🚫 3. Gerbang Kata Terlarang (Strict Banned Words Gate)

Seluruh konten yang dihasilkan oleh tim dan AI **DILARANG KERAS** menggunakan kata-kata pasaran berikut:

| Kata Terlarang (DILARANG) | Alasan Pelarangan | Pengganti Resmi SECERA |
| :--- | :--- | :--- |
| **Murah / Banting harga** | Merusak persepsi kemewahan dan craft | *Investasi cerdas, harga terjangkau, value terbaik* |
| **Diskon gila / Cuci gudang** | Berkesan pasar kaget / barang sisa | *Penawaran istimewa, kurasi akhir musim* |
| **Wajib checkout / Gercep** | Agresif, memaksa, tidak berkelas | *Pilihan tepat untuk akhir pekan ini, siap dikirim* |
| **Auto cantik / Auto glowing** | Slang pasaran / tidak bermartabat | *Tampil memukau, siluet anggun seketika* |
| **Viral banget / Racun TikTok** | Klise e-commerce generik yang cepat usang | *Pilihan favorit banyak wanita, terbukti dipercaya* |
| **Anti gagal** | Klise dan terdengar tidak realistis | *Solusi andalan, potongan yang selalu proporsional* |
| **Super mewah / Glam maksimal** | SECERA mengusung keanggunan bersahaja | *Elegan, berkelas, understated luxury* |
| **Princess / Ratu kondangan** | Terlalu salon bridal jadul dan berlebihan | *Anggun, berwibawa, mempesona secara tenang* |
| **Salfok / Kece badai** | Bahasa gaul pasar yang menurunkan kelas | *Mencuri perhatian dengan anggun, memikat* |

---

## 🚀 4. Cara Menggunakan di Google Gemini Web / Gems

Untuk tim pemasaran atau Customer Service yang menggunakan [Google Gemini](https://gemini.google.com/gems):

### Membuat Gem 1: SECERA Brand Guardian & Creative Director
1. Buka [gemini.google.com/gems](https://gemini.google.com/gems) → Klik **New Gem**.
2. Beri nama: `SECERA Brand Guardian & Creative Director`.
3. Buka file: [`export/GEMINI_GEM_BRAND_MASTER.md`](export/GEMINI_GEM_BRAND_MASTER.md).
4. Salin (*copy*) seluruh teks di dalam blok kode, lalu tempel (*paste*) ke kotak **Instructions**.
5. Simpan (Save).

### Membuat Gem 2: SECERA Occasion Stylist & Specialist
1. Buka [gemini.google.com/gems](https://gemini.google.com/gems) → Klik **New Gem**.
2. Beri nama: `SECERA Occasion Stylist & Specialist`.
3. Buka file: [`export/GEMINI_GEM_PRODUCT_SPECIALIST.md`](export/GEMINI_GEM_PRODUCT_SPECIALIST.md).
4. Salin (*copy*) seluruh teks di dalam blok kode, lalu tempel (*paste*) ke kotak **Instructions**.
5. Simpan (Save).

---

## 🔄 5. Sinkronisasi Katalog Otomatis (Live Sync Utility)

Setiap kali ada penambahan produk baru, perubahan harga promo, atau update size chart di website [secera.id/shop](https://secera.id/shop), jalankan perintah berikut:

```bash
python3 scripts/sync_products.py
```

Skrip ini akan:
1. Menghubungi API live `https://secera.id/api/products`.
2. Menyimpan snapshot JSON mentah di `data/products_raw.json`.
3. Memperbarui tabel matriks katalog di `.agents/skills/secera-product-knowledge/references/product_catalog_matrix.md` secara otomatis.

---

## 🌿 6. Doktrin Visual & Warna Resmi

- **Zero-Radius:** Sudut serba tajam 90° arsitektural (`border-radius: 0px`), tanpa tombol membulat (*rounded pills*).
- **Tipografi:** Heading menggunakan **Libre Caslon Display** (Serif ringan, sentence case) dan isi teks menggunakan **Inter** (Sans-serif modern).
- **Palet Warna Inti:**
  - `Brand Wine`: `#722F38` (Aksen utama / tombol signature)
  - `Brand Wine Deep`: `#5A252D` (Hover / penekanan)
  - `Ink`: `#261F1F` (Teks dark charcoal hangat — bukan hitam kaku #000000)
  - `Muted`: `#7B6F6B` (Keterangan sekunder / size chart caption)
  - `Canvas`: Ivory `#FAF7F2`, Cream `#F5F0E8`, Paper `#FFFFFF`

