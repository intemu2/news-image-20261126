# AUDIT v5 — news-image-20261126 (27 Nov 2026 ~05:20 WIB)
# Perubahan dari v4: 2 baris bawah tiap kolom juga bergambar + semua baris dirapatkan

## Aturan bounty (tidak berubah sejak v3 — dibaca ulang 05:07 WIB)
- Hadiah $100, 50 tempat: 1 $20, 2 $12, 3 $6, 4–10 $2, 11–50 $1,20.
- Deadline Sat 28 Nov 2026 00:00 UTC = 07:00 WIB 28 Nov 2026.
- Gambar utuh PNG/JPEG maks 1 MiB, 1024×1024 px. Program tanpa network,
  dua run harus hasilkan byte sama. Maks 10 submit/hari, 20 total.

## Kepatuhan file v5
- entry-v5.png: 1024×1024 PNG, 522 KB (< 1 MiB). Lolos.
- Deterministik: dua run build_v5.py menghasilkan SHA256 sama
  fd0bd8d852e8e4c2e6ae20429d67aea6fd6d763ff17ab329926cf78894d7e892.
- Build lokal tanpa network: PIL + 17 ilustrasi AI (8 panel + 9 thumbnail).
- BELUM disubmit. Tidak ada repo GitHub dibuat, tidak ada submit.

## Perubahan vs v4 (isi cerita TIDAK berubah — 37 cerita, 0 duplikasi)
- Kini baris 1, 7, DAN 8 tiap kolom bergambar (9 thumbnail total):
  - AMERICAS baris 7: bendera Brazil + China, kontainer, karung gula,
    mesin pesawat, berkas tarif. Baris 8: dokter pegang model ginjal,
    mesin dialisis, matahari terbit.
  - EUROPE baris 7: Union Jack + gembok beku + kapal di Laut Merah
    (sanksi Houthi). Baris 8: peron Tube London, roundel merah tanpa
    huruf, kereta datang.
  - ASIA baris 7: kerumunan protes Irbil, bendera Kurdi, benteng.
    Baris 8: alun-alun Lusaka, pengunjuk rasa spanduk kosong, polisi.
  - 4 gambar baru dibuat sbg 2 gambar + 2 diptych (kiri/kanan), lalu
    diptych dipotong jadi 2 thumbnail per gambar; potongan dicek:
    garis belah bersih, tiap sisi nyambung ke ceritanya.
- Thumbnail diseragamkan 84×54 px (v4: 84×68 untuk baris 1).
- Semua baris dirapatkan: baris bergambar 61 px, baris teks 31 px
  (leading judul 13, badan 12). Blok brief berakhir ~918 px,
  footer 924 px — tidak ada teks terpotong, tidak ada ruang kosong berlebih.

## Cek visual (dilihat langsung, penuh + crop bawah 2x)
- Keenam thumbnail bawah nyambung ke ceritanya dan jelas di ukuran kecil.
- Teks tajam, tidak ada yang tumpang tindih atau terpotong.
- Garis pemisah sejajar di ketiga kolom; baris terakhir berakhir rapi
  di atas footer.
- Catatan kecil: bendera Brazil di thumbnail tarif membawa tulisan
  mungil "Ordem e Progresso" — itu bagian dari desain bendera asli,
  tidak terbaca di ukuran thumbnail.

## Audit fakta
- TIDAK ADA cerita baru di v5 — semua 37 cerita sama dengan v3/v4,
  jadi audit fakta v3 (AUDIT-v3.md) berlaku penuh: Tube strike
  (Times, kuat), Sanaa & Zaporizhia (Daily Summary), pig kidney &
  Sudan (OneTurn, TUNGGAL), F-16 / Eurostar / Pacifica / Hasakah
  tetap DITOLAK, catatan Ibiza / Bogor / mati listrik / peta skematik
  tetap berlaku.
- BELUM TERVERIFIKASI: jumlah submit terpakai akun intemu2, jumlah
  entri/field live dan rank.
