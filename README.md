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



### Tugas 3

**1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan `{% csrf_token %}` pada form tersebut!**
**Jawaban:** Penggunaan `ModelForm` jauh lebih efisien karena Django secara otomatis membangun form HTML dan menyediakan validasi data berdasarkan *field* yang sudah didefinisikan pada model (*Don't Repeat Yourself*). Ini mengurangi penulisan kode manual yang berulang dan meminimalisir kesalahan. Penambahan `{% csrf_token %}` diwajibkan untuk keamanan, yaitu melindungi aplikasi dari serangan *Cross-Site Request Forgery* (CSRF). Token ini memastikan bahwa *request* POST yang dikirim benar-benar berasal dari form di dalam aplikasi kita, bukan dari situs eksternal yang berniat jahat.

**2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?**
**Jawaban:** JSON lebih disukai karena struktur sintaksnya lebih ringkas dan ringan, sehingga ukuran datanya lebih kecil dan lebih cepat ditransfer melalui jaringan. Selain itu, format JSON sangat mirip dengan struktur objek *native* pada JavaScript. Hal ini membuat aplikasi *frontend* modern dapat langsung membaca dan memproses (parsing) JSON dengan sangat mudah dan cepat tanpa memerlukan *parser* tambahan yang kompleks seperti halnya XML.

**3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?**
**Jawaban:** Alurnya adalah: Client (browser) melakukan *request* ke URL tertentu -> URL mengarahkan ke fungsi *view* -> *View* melakukan *query* ke database menggunakan model (misal: `Project.objects.all()`) dan mendapatkan objek QuerySet Python -> Objek tersebut **diserialisasi** menjadi format JSON -> JSON dikembalikan ke client sebagai `HttpResponse` atau `JsonResponse`.
Proses *serialization* sangat diperlukan karena protokol HTTP dan web browser tidak mengerti tipe data objek Python (QuerySet). Serialisasi berfungsi menerjemahkan objek Python tersebut menjadi format string/teks terstandarisasi (JSON) agar bisa dikirim lewat jaringan dan dimengerti oleh browser.

---

**AI Disclosure:**
Dalam pengerjaan tugas ini, saya menggunakan bantuan AI (Gemini) untuk:
- Membantu *debugging* ketika menemui error `NoReverseMatch` dan `NameError` pada saat mengatur *routing* URL untuk fitur `edit_project` dan `delete_project`.
- Mendapatkan rekomendasi penulisan CSS Grid dan efek *glassmorphism* untuk menyusun *card* proyek agar sejajar horizontal.

**Keterbatasan AI & Perbaikan Manual:**
AI memiliki keterbatasan dalam memahami konteks file statis secara keseluruhan. AI sempat memberikan kode pengganti `base.html` yang justru menghilangkan efek *background* gelombang utama bawaan proyek saya. Oleh karena itu, saya melakukan perbaikan manual dengan mengembalikan file `base.html` ke versi asli dan menyesuaikan sendiri struktur *container grid* di `project_list.html` agar *card* proyek tetap transparan tanpa merusak estetika desain animasi *background* awal.


---

## 🚀 Individual Assignment 4: Authentication, Authorization & Star Feature

### 📌 Ringkasan Implementasi Tugas 4
1. **Manajemen Hak Akses & Peran (Authorization):**
   - Menerapkan pembatasan hak akses di sisi server (*server-side check* menggunakan `HttpResponseForbidden`) serta menyembunyikan tombol kontrol di *template* HTML berdasarkan 4 peran:
     - **Pengunjung Tanpa Login:** Hanya dapat membaca data.
     - **Pengguna Biasa:** Dapat membaca data dan memberi/membatalkan *star*.
     - **Editor (Grup Django Admin):** Memiliki hak pengguna biasa ditambah izin untuk menambah dan mengubah data, tetapi **tidak dapat menghapus** data.
     - **Pemilik Portofolio / Superuser (`nr1411`):** Memiliki hak akses mutlak penuh (CRUD lengkap).
2. **Fitur Interaktif Star:**
   - Menambahkan relasi `ManyToManyField` ke model `User` pada model proyek.
   - Mengimplementasikan view `toggle_star` dengan metode POST dan proteksi `@login_required`.
3. **Refinement API JSON:**
   - Memastikan endpoint JSON proyek menggunakan `use_natural_foreign_keys=True` agar data relasi terekspos secara bersih dan aman.

---

### 🤖 AI Disclosure & Pertanyaan Reflektif (Tugas 4)

#### 1. Transparansi Penggunaan AI (AI Disclosure)
* **Bagian yang Dibantu AI:** Penulisan fungsi logika otorisasi peran *Editor* (`is_editor_or_superuser`) di `views.py`, pengaturan pengkondisian template HTML untuk tombol CRUD dinamis, serta penyusunan dokumentasi `README.md`.
* **Strategi Prompting:** Menggunakan pendekatan interaktif bertahap (*step-by-step troubleshooting*), mulai dari konfigurasi *Django Groups* di Admin, validasi relasi `ManyToManyField`, hingga penyelarasan respons API JSON.
* **Validasi & Perbaikan Manual:** Seluruh kode yang disarankan diuji langsung melalui *local server* Django (`runserver`) dan diverifikasi melalui *Django Admin Dashboard* untuk memastikan tidak ada celah akses ilegal.

#### 2. Pertanyaan Reflektif
* **Apa tantangan terbesar selama mengimplementasikan autentikasi dan otorisasi pada tugas ini?**  
  Memastikan bahwa keamanan tidak hanya mengandalkan penyembunyian tombol di sisi tampilan (*front-end*), melainkan wajib divalidasi secara ketat di sisi *back-end* menggunakan `HttpResponseForbidden` agar pengguna iseng tidak bisa bypass lewat URL langsung. Selain itu, membedakan hak khusus *Editor* (bisa ubah tapi dilarang hapus) memerlukan pengecualian *conditional check* yang presisi.
* **Bagaimana pemahaman Anda mengenai perbedaan peran antara Pengguna Biasa, Editor, dan Superuser setelah menyelesaikan tugas ini?**  
  Menjadi paham bahwa pembagian peran (*Role-Based Access Control*) sangat krusial dalam pembuatan aplikasi nyata agar tanggung jawab pengelolaan data terstruktur dengan aman sesuai tingkat privilese masing-masing akun.

  # My Portofolio - Tugas 5 PBP

## Deskripsi Proyek
Aplikasi web portofolio pribadi yang dikembangkan untuk memenuhi Tugas Pemrograman Berbasis Platform (PBP). Pada Tugas 5 ini, aplikasi ditingkatkan dengan mengimplementasikan fungsionalitas asinkron menggunakan **AJAX** (GET dan POST), form modal interaktif, fitur pencarian/sorting, serta penanganan keamanan data secara asinkron.

---

## 📝 Pertanyaan Reflektif (Tugas 5)

### 1. Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!
* **Debouncing** adalah sebuah teknik pemrograman yang digunakan untuk membatasi seberapa sering sebuah fungsi (dalam hal ini fungsi pencarian atau *request* AJAX ke server) dieksekusi dalam rentang waktu tertentu. Teknik ini memastikan bahwa *event handler* tidak langsung berjalan setiap kali pengguna mengetik satu huruf, melainkan menunggu hingga pengguna berhenti mengetik selama jeda waktu tertentu (misalnya 300-500ms).
* **Mengapa penting?** Jika tanpa *debouncing*, setiap kali pengguna mengetik satu karakter pada kolom pencarian, browser akan langsung mengirimkan *request* HTTP ke server secara bersamaan (*on-every-keystroke*). Hal ini dapat menyebabkan lonjakan beban yang tidak perlu pada server (*server overhead*), potensi *race condition* (respons yang datang tidak berurutan), serta membuat performa aplikasi terasa lambat atau *laggy*. Dengan *debouncing*, *request* ke server menjadi jauh lebih efisien karena hanya dikirimkan saat pengguna selesai mengetik kata kunci yang diinginkan.

---

### 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
* **Fungsi `await`**: Perintah `await` digunakan di dalam fungsi `async` JavaScript untuk menunggu hingga sebuah *Promise* diselesaikan (*resolved*) atau dikembalikan sebelum mengeksekusi baris kode berikutnya. Pada pemanggilan `fetch()`, `await` memastikan bahwa program menunggu proses pengambilan data jaringan selesai dan objek respons berhasil diterima sebelum kita mencoba menguraikannya (misalnya menjadi format `.json()`).
* **Apa yang terjadi jika tidak menggunakan `await`?** Jika kita tidak menggunakan `await` (dan tidak menangani *Promise* dengan `.then()`), JavaScript akan langsung mengeksekusi baris kode berikutnya secara asinkron sebelum data dari server benar-benar tiba. Akibatnya, variabel yang menampung hasil `fetch()` bukanlah data JSON yang kita inginkan, melainkan sebuah objek *Pending Promise*, yang akan menyebabkan *error* saat kita mencoba mengakses atau merender data tersebut di antarmuka web.

---

### 3. Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JS lebih rentan daripada data yang ditampilkan langsung melalui template Django!
* **Serangan XSS (Cross-Site Scripting)** adalah jenis kerentanan keamanan di mana penyerang berhasil menyisipkan skrip berbahaya (biasanya berupa kode JavaScript/HTML) ke dalam situs web yang nantinya akan dieksekusi oleh peramban pengguna lain yang mengunjungi situs tersebut.
* **Mengapa AJAX/JS lebih rentan?** 
  * Ketika menggunakan **template HTML Django standar**, Django secara otomatis melakukan *auto-escaping* pada variabel yang dirender di server, sehingga karakter khusus seperti `<script>` akan dinetralkan menjadi teks biasa yang aman.
  * Sebaliknya, ketika menggunakan **AJAX dan JavaScript**, data JSON yang diterima dari server seringkali langsung disuntikkan ke dalam DOM menggunakan properti seperti `innerHTML` atau dimanipulasi secara manual di sisi klien. Jika data dari *input* pengguna tidak dibersihkan (*sanitize*) atau lolos dari validasi, skrip berbahaya yang dikirimkan oleh penyerang dapat tereksekusi secara langsung di browser pengguna lain, mencuri *cookie*, atau membajak sesi login. Oleh karena itu, diperlukan sanitasi tambahan (seperti escape HTML atau penggunaan `DOMPurify` / `strip_tags`) pada data yang masuk maupun keluar.

---

## 🚀 Fitur Ekstensi (Opsional / Nilai Tambah)
* **Fitur Sorting Data Proyek**: Mengimplementasikan opsi pengurutan daftar proyek berdasarkan kriteria tertentu (seperti berdasarkan tanggal terbaru atau abjad judul) untuk meningkatkan kemudahan navigasi pengguna.
* **Pembersihan Input (Sanitasi)**: Penambahan validasi ketat untuk memastikan tidak ada injeksi skrip berbahaya pada data yang dikirimkan lewat form AJAX.

---

## 🤖 AI Disclosure
Dalam pengerjaan Tugas 5 ini, pemanfaatan AI (Gemini) digunakan secara transparan dengan cakupan sebagai berikut:
* **Bagian yang dibantu oleh AI**: 
  * Diskusi konseptual terkait perbedaan alur *asynchronous* dan *synchronous*.
  * Membantu proses *debugging* pesan *error* pada penyesuaian atribut model Django (`technology_used` dan relasi *many-to-many*).
  * Memberikan referensi struktur penulisan kode JavaScript untuk *fetch* API dan penanganan *event listener* modal.
* **Strategi Prompting**: Menggunakan *error-driven prompting* (menyertakan log error terminal dan cuplikan kode aktual) untuk mendapatkan solusi perbaikan bug secara spesifik dan terarah.
* **Verifikasi Manual**: Seluruh kode perbaikan, logika tampilan AJAX, serta jawaban pertanyaan reflektif di atas telah dipahami secara mandiri dan diuji secara langsung pada lingkungan lokal (*local development*) sebelum di-*commit* ke repositori Git.