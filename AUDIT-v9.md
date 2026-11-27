# AUDIT v9 — news-image-20261126 (27 Nov 2026 ~08:20 WIB)
# Perubahan dari v8: perataan angka di lingkaran pin peta + PIN INDEX saja

## Status
- BELUM disubmit. Entri aktif tetap v5.
  Kandidat final sekarang v9 (menggantikan v8 sebagai kandidat).
- File: entry-v9.png, dibuat dari build_v9.py (turunan build_v8.py).
- TIDAK ada perintah git yang dijalankan di repo/. TIDAK ada file repo/ yang diubah.
- Susunan thumbnail item 1,2,3 di kolom bawah dipertahankan (v7).
- Posisi pin dan label peta dari v8 dipertahankan (tidak ada koordinat yang diubah).

## Pengukuran v8 yang membenarkan revisi
Metode: centroid piksel putih angka di dalam radius 7,5 px dari pusat lingkaran.
- Pin peta v8: angka duduk +2,0 s/d +3,6 px TERLALU RENDAH (pin 2 Bogor +3,6).
  Horizontal -0,2 s/d +0,7 px (sudah baik).
- PIN INDEX v8: angka duduk -1,3 s/d -2,0 px ke KIRI dan +1,1 s/d +1,8 px ke BAWAH.
  Penyebab: peta memakai rumus y - size*0,75; PIN INDEX memakai hitung
  manual 688-tw/2 dan ry+3, bukan pusat lingkaran (689, ry+8).

## Perubahan vs v8 (kode perataan saja; isi cerita TIDAK berubah)
- Teks pin SVG: y = pusat lingkaran (dulu pusat+4,5), ditambah atribut
  dominant-baseline="central"; render_svg menggambar teks seperti itu
  dengan anchor="mm" (tengah-tengah PIL). Teks SVG lain (ikon %) memakai
  jalur lama, tidak berubah.
- Angka PIN INDEX: digambar di pusat lingkaran persis (689, ry+8) dengan
  anchor="mm" (dulu hitung manual 688-tw/2, ry+3).
- Teks tempat + kejadian PIN INDEX: diratakan ke tengah lingkaran yang sama
  dengan anchor="lm" di (702, ry+8) (dulu ry+1), jadi baris 1-5 konsisten.
- Lingkaran, ukuran font, warna, dan posisi tidak diubah.

## Pengukuran v9 setelah perbaikan (metode yang sama)
- Pin peta: offset vertikal +0,0 s/d +0,7 px (dulu +2,0 s/d +3,6);
  horizontal -0,2 s/d +0,8 px. Sisa <1 px adalah bias bentuk digit
  ("4" massanya lebih ke kanan, "1" lebih ke kiri), bukan kesalahan letak.
- PIN INDEX: offset -0,3 s/d -1,0 px horizontal, -0,2 s/d -0,9 px vertikal
  (dulu -1,3 s/d -2,0 dan +1,1 s/d +1,8). Semua di bawah 1 px.

## Kepatuhan file v9 — cek lokal 27 Nov ~08:20 WIB
- entry-v9.png: 1024x1024 PNG, RGB, 533.805 byte (< 1 MiB).
- Deterministik: tiga run build_v9.py menghasilkan SHA256 sama
  7169c004f8ead6b06c9400f48667221c226ed5072c23c499556f249adde9db83.
- Build lokal tanpa network: PIL + aset webp yang sama dengan v5-v8.
- Guard di make_v9.py lolos: baris PIN INDEX 1-5, koordinat pin v8,
  urutan thumbnail v7, dan 30 string khas cerita hadir identik di v8 dan v9.
- Cek visual (dilihat langsung, penuh + crop peta 2x): angka 1-5 duduk
  di tengah lingkaran pin peta dan lingkaran PIN INDEX; kelima baris
  PIN INDEX sejajar rapi; thumbnail kolom bawah tetap di item 1,2,3;
  semua teks tajam, tidak ada yang terpotong atau tumpang tindih,
  tidak ada typo baru.

## Audit fakta
- TIDAK ADA cerita baru di v9 — semua 37 cerita sama dengan v3-v8,
  audit fakta v3 (AUDIT-v3.md) berlaku penuh.

## BELUM TERVERIFIKASI saat audit ini ditulis
- Hasil pengecekan live make.fun (rate/rank v5, garis #50, kuota tersisa):
  browser task masih berjalan, belum ada hasil masuk. Jangan submit
  sebelum hasil live + persetujuan Firt.
