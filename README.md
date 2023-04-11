# Dokumentasi Proyek Akhir Algoritma dan Struktur Data
## "Implementasi Algoritma dan Struktur Data pada Big Project Traveloka"

### Deskripsi Program

Traveloka adalah program pelayanan kebutuhan perjalanan dan liburan yang telah dikenal di seluruh asia. Traveloka adalah program dengan sistem pelayanan pada pemesanan
tiket pesawat, hotel, dan lain lain. Alasan kami memilih Traveloka karena cocok untuk di implementasikan dengan struktur data dan algoritma yang sedang dipelajari saat ini,
yaitu Linked list, Search, dan Sort. 

#### Implementasi Module

Adapun Module yang digunakan dalam Project ini adalah :

* PyMongo: yaitu module yang menghubungkan antara python dengan Mongodb yang merupakan Database berbasis Hosting/Server Online.
* Clear Screen (cls): yang merupakan modul untuk memberikan efek clear pada screen terminal.
* Time: fungsi yang digunakan ialah sleep() yang berfungsi untuk menghentikan program untuk sementara dalam waktu tertentu, diatur dalam satuan detik.
* PrettyTable: yaitu modul yang digunakan untuk memanipulasi visual data yang akan ditampilkan dalam view.

#### Instalasi module

```bash
pip install pymongo
```

```bash
pip install prettytable
```

```bash
pip install python-time
```
#### Struktur Program

Konsep yang digunakan adalah MVC (Model, view, Controller). MVC adalah arsitektur pengelolaan program menjadi tiga bagian yaitu Model, View, Controller.

* Model Merupakan representasi data atau objek yang menyimpan informasi dan mengelola akses ke data. Model juga bertanggung jawab untuk memproses data, memvalidasi input, dan menyediakan antarmuka untuk mengakses dan memanipulasi data.
* View merupakan komponen antarmuka pengguna yang menampilkan data dan memungkinkan pengguna untuk berinteraksi dengan aplikasi. 
* Controller Merupakan komponen yang menghubungkan Model dan View. Controller bertanggung jawab untuk menerima input dari pengguna, 
memproses input tersebut dengan menggunakan Model, 
dan mengirimkan hasil pemrosesan tersebut ke View untuk ditampilkan.

### Penjelasan Program 
#### Model - database.py
Kode database.py merupakan kepala dari seluruh program Traveloka. 

![image](https://user-images.githubusercontent.com/126738691/231100003-1a25ce9f-03d9-4ac6-88a0-8eaf58374d48.png) 

Didalam kode ini, kita menggunakan Pymongo sebagai alat penghubung antara Python dengan MongoDB (MongoClient), kemudian kita melakukan import dotenv yang berfungsi sebagai environtment bagi .env. 
Kemudian load_dotenv() berfungsi untuk menarik key - value dari cluster MongoClient (getenv("MONGO_URI")) dan menyimpannya didalam dotenv. 
Lalu db = cluster["traveloka"] berfungsi untuk menghubungkan program Database.py dengan MongoClient yang terdapat cluster "Traveloka" didalamnya, lalu baris-baris selanjutnya berfungsi sebagai variabel pemanggil setiap bagian data program traveloka, yaitu akun, tiket pesawat, tiket hotel, dan transaksi.

#### Model - main_view.py

#### Model - admin_view.py
Kode ini sebagai tampilan menu utama / display bagi administrator.

![image](https://user-images.githubusercontent.com/126738691/231103225-fb1cd0ed-3aad-4451-8a3c-251da80fa0d2.png)

Kode ini berisi menu tambah pesawat, lihat pesawat, edit pesawat, hapus pesawat, dan sign out. Admin_view.py terhubung dengan main_view.py, flight_controller.py, dan auth_controller.py.

![image](https://user-images.githubusercontent.com/126738691/231104731-ce9bb993-148d-4828-9ea8-bb27d675cbab.png)

Setiap menu terhubung dengan beberapa kode program yang telah disebutkan diatas. Jika user memilih opsi 1, maka user akan menuju flight_controller.py yang berada
didalam Controller (MVC), didalam menu ini, user dapat admin dapat menambah data pesawat.
Selanjutnya adalah opsi ke 2, yaitu "Lihat pesawat", opsi ini juga akan mengarahkan user kedalam flight_controller.py didalam Controller (MVC).







