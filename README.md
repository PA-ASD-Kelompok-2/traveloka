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
Module database.py merupakan kepala dari seluruh program Traveloka. 

```python
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

cluster = MongoClient(os.getenv("MONGO_URI"))

db = cluster["traveloka"]

dataAcc = db["account"]
dataFlight = db["flight"]
dataHotel = db["hotel"]
dataTransaction = db["transaction"]
``` 

Didalam module ini, kita menggunakan module Pymongo sebagai alat penghubung antara Python dengan MongoDB (MongoClient), kemudian kita melakukan import dotenv yang berfungsi sebagai environtment bagi .env. 
Kemudian load_dotenv() berfungsi untuk menarik key - value dari cluster MongoClient (getenv("MONGO_URI")) dan menyimpannya didalam dotenv. 
Lalu db = cluster["traveloka"] berfungsi untuk menghubungkan program Database.py dengan MongoClient yang terdapat cluster "Traveloka" didalamnya, lalu baris-baris selanjutnya berfungsi sebagai variabel pemanggil setiap bagian data program traveloka, yaitu akun, tiket pesawat, tiket hotel, dan transaksi.

#### View - main_view.py
Module ini merupakan tampilan menu awal program Traveloka.

```python
from Controller import auth_controller
import os
```
Dalam source code tersebut, kita akan memanggil folder CONTROLLER (MVC) yang berisi module Auth_controller.py. Module auth_controller.py sendiri berfungsi sebagai 
kontrol (Controller) autentikasi bagi user, baik itu user biasa maupun user admin seperti login dan register, dan lupa password.

```python
class MenuUtama:
    def __init__(self):
        self.auth = auth_controller.User()

    def run(self):
        try:
            os.system('cls')
            while True:
                print('=================================')
                print('|            Welcome            |')
                print('|           Traveloka           |')
                print('=================================')
                print('|>>>>> Silahkan pilih opsi <<<<<|')
                print('|                               |')
                print('|   1. Registrasi Akun          |')
                print('|   2. Login Akun               |')
                print('|   3. Lupa Password            |')
                print('|   4. Keluar                   |')
                print('|                               |')
                print('=================================')

                opsi = str(input('Tentukan opsi anda (1/2/3/4): '))

                if opsi == '1':
                    self.auth.register()
                elif opsi == '2':
                    self.auth.login()
                elif opsi == '3':
                    self.auth.forgot_password()
                elif opsi == '4':
                    print('Terima kasih telah menggunakan layanan kami!')
```

Module ini sendiri terdiri dari beberapa menu yaitu registrasi, login, lupa password, dan keluar. Jika user memilih opsi ke-1 yaitu registrasi aku, maka module 
akan merujuk ke module auth_controller.py yaitu pada bagian register, yang dimana, fungsi register tersebut akan merujuk kedalam folder MODEL (MVC) yang berisi
database.py, yang telah terhubung kedalam MongoClient. Jika user memilih opsi ke-2, yaitu login akun, maka cara kerjanya sama, yaitu module akan merujuk ke module
auth_controller.py dimana terdapat fungsi login. Opsi ke-3 pun sama, yaitu merujuk kedalam auth_controller.py. Jika user memilih opsi keluar, maka program akan stop.

```python
 except KeyboardInterrupt:
            print('Terjadi kesalahan!')
            exit()
```
Source code diatas berfungsi sebagai penanganan / penyelesain jika terjadi error KeyboardInterrupt.

#### View - admin_view.py
Module ini sebagai tampilan menu utama / display bagi administrator.

```python
from View import main_view as main
from Controller import flight_controller as fc
from Controller import auth_controller as auth
import os
```
Module ini berisi menu tambah pesawat, lihat pesawat, edit pesawat, hapus pesawat, dan sign out. Admin_view.py terhubung dengan main_view.py, flight_controller.py, dan auth_controller.py.

```python
def menu_admin(self):
        try:
            os.system('cls')
            while True:
                print("==================================")
                print("|            M E N U             |")
                print("==================================")
                print("|-----> Menu yang tersedia <-----|")
                print("|                                |")
                print("|    1. Tambah Pesawat           |")
                print("|    2. Lihat Pesawat            |")
                print("|    3. Edit Pesawat             |")
                print("|    4. Hapus Pesawat            |")
                print("|    5. Sign Out                 |")
                print("|                                |")
                print("==================================")
                opsi = str(input("Tentukan opsi anda (1/2/3/4/5): "))

                if opsi == '1':
                    self.flight.addFlight()
                elif opsi == '2':
                    self.flight.display()
                elif opsi == '3':
                    self.flight.updateFlight()
                elif opsi == '4':
                    self.flight.deleteFlight()
                elif opsi == '5':
                    self.auth.logout()
                    main.MenuUtama().run()
                else:
                    print("Opsi tidak tersedia!")
```
Setiap menu terhubung dengan beberapa kode program yang telah disebutkan diatas. Jika user memilih opsi ke-1, maka user akan menuju flight_controller.py yang berada
didalam Controller (MVC), didalam fungsi ini, user dapat admin dapat menambah data pesawat, dan fungsi ini sendiri terhubung dengan module database.py. Selanjutnya
adalah opsi ke-2, yaitu "Lihat pesawat", opsi ini juga akan mengarahkan user kedalam flight_controller.py didalam Controller (MVC). Opsi ke-3 juga memiliki cara kerja
yang sama, yaitu module akan merujuk ke flight_controller.py. Lalu opsi ke-4, maka module akan merujuk kedalam Auth_controller.py didalam folder Controller (MVC).

#### Controller - 





