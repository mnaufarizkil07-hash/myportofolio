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

### Tugas 2

1. **Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser.**
   - Pengguna memasukkan URL halaman proyek di browser. *Request* dikirim ke server Django.
   - **`urls.py` proyek** menerima *request* dan meneruskannya ke **`urls.py` aplikasi** (`main`).
   - Django mencocokkan pola URL (routing) dan memanggil fungsi **`view`** (`project_list`).
   - Di dalam *view*, Django meminta data ke **`model`** (`Project.objects.all()`) untuk mengambil kumpulan data dari database.
   - *View* memasukkan data tersebut ke dalam variabel *context* dan menyatukannya dengan **`template`** (`project_list.html`).
   - *Template engine* mengubah kode-kode tag Django menjadi dokumen HTML utuh dan mengirimkannya kembali sebagai *HTTP Response* ke browser pengguna.

2. **Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template?**
   - Menyimpan data di Model memisahkan antara data/konten dengan tampilan. Hal ini membuat aplikasi menjadi **dinamis**. Kita bisa menambah, mengedit, atau menghapus data proyek ke depannya melalui database tanpa harus mengubah kode HTML sama sekali. Ini sangat memudahkan pemeliharaan (*maintenance*) karena kita tidak perlu melakukan *hard-coding*.

3. **Apa perbedaan fungsi `makemigrations` dan `migrate` pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.**
   - **`makemigrations`**: Berfungsi untuk membaca perubahan pada file `models.py` dan membuat file instruksi (migrasi) yang mencatat perubahan tersebut (ibarat membuat cetak biru pembentukan database).
   - **`migrate`**: Berfungsi untuk mengeksekusi file instruksi migrasi tersebut ke dalam database sungguhan agar tabel atau kolomnya benar-benar terbuat/berubah secara fisik.
   - **Contoh**: Ketika kita membuat class model `Project` baru, atau ketika suatu saat nanti kita ingin menambahkan *field* baru (seperti `image = models.ImageField()`) pada model `Project` yang sudah ada. Kita harus menjalankan kedua perintah tersebut secara berurutan.