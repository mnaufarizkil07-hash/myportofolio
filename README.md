Nama : Muhammad Naufal Rizki Fadhlurrahman
NPM : 2506623490
Kelas : PBP Bini adalah tambahan text untuk latihan branch


### Tugas 1

**1. Penggunaan Elemen Semantik HTML5**
Ya, saya menggunakan elemen semantik HTML5 dalam perancangan struktur website ini. Pada tugas ini, saya menggunakan `<section>` untuk membungkus area utama baru yakni "Experience & Skills", dan menggunakan `<article>` untuk membungkus masing-masing kartu (item) pengalaman di dalamnya. Penggunaan elemen semantik ini sangat membantu karena membuat kode lebih terstruktur, bermakna (meaningful), dan mudah dibaca oleh developer lain maupun oleh mesin (SEO & aksesibilitas), dibandingkan jika hanya menggunakan elemen non-semantik seperti `<div>` secara berlebihan.

**2. Tantangan Mengatur CSS Responsif**
Tantangan utama saat mengatur CSS agar tetap responsif adalah memastikan elemen berupa *card* yang berjejer horizontal di layar desktop tidak terpotong atau menjadi terlalu sempit saat dibuka di perangkat mobile. Evaluasi yang dilakukan adalah memanfaatkan Flexbox. Saat berpindah ke tampilan mobile (dengan batas layar di bawah 768px), saya mengubah arah *layout* dari `flex-direction: row` menjadi `flex-direction: column`. Dengan begitu, elemen yang awalnya tersusun ke samping akan otomatis menyesuaikan diri dan berubah menjadi tumpukan vertikal ke bawah, sehingga ukuran konten tetap terbaca jelas.

**3. Batasan Static Web & Fungsionalitas Dinamis Masa Depan**
Batasan utama dari *static web* murni adalah kekakuan data. Semua informasi bersifat *hardcoded* di dalam file HTML. Jika suatu saat saya ingin menambahkan pengalaman baru atau memperbarui keahlian, saya harus membuka, mengedit, dan melakukan *deploy* ulang source code secara manual. Pada iterasi proyek selanjutnya, fungsionalitas dinamis yang paling ingin saya persiapkan adalah integrasi dengan database menggunakan framework Django. Tujuannya agar saya bisa menambah, mengedit, dan menghapus isi portofolio ini melalui *dashboard* admin yang dinamis tanpa perlu menyentuh file HTML lagi.

**AI Disclosure:**
Dalam pengerjaan tugas ini, saya menggunakan bantuan AI (Gemini) secara transparan. Bantuan yang diberikan berfokus pada:
- **Strategi Pemecahan Masalah:** Mengidentifikasi letak kesalahan saat membuka *directory* proyek di VS Code (perbaikan *pathing* dari *parent folder*).
- **Brainstorming CSS:** Mendapatkan ide untuk implementasi sintaks animasi *hover* yang mulus dan pengaturan tata letak *responsive* menggunakan Flexbox.
- Seluruh logika dasar, pengisian data personal, dan eksekusi struktur utama murni dilakukan secara mandiri sesuai dengan materi tutorial.