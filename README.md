# <span style= "color: #1ba0e2"> **Dokumentasi Proyek Akhir Algoritma dan Struktur Data** </span>

## <span style= "color: #1ba0e2">**Implementasi Algoritma dan Struktur Data pada Big Project Traveloka** </span>
## <span style= "color: #1ba0e2">**Anggota Kelompok** </span>
* **Muhammad Irfan Maulana** - 2209116036
* **Muhammad Fauzan Gifari Dzul Fahmi** - 2209116042
* **Abdul Rahman** - 2209116045
------------------
## <span style= "color: #1ba0e2">**Daftar Isi** </span>

* [**Deskripsi Program**](#Deskripsi-Program)
* [**Implementasi Modul**](#Implementasi-Modul)
* [**Instalasi modul**](#Instalasi-modul)
* [**Struktur Program**](#Struktur-Program)
* [**Cara Penggunaan**](#Cara-Penggunaan)
    * [**Opsi Awal**](#Opsi-Awal)
    * [**Tampilan User**](#Tampilan-User)
    * [**Tampilan Admin**](#Menu-Admin)
* [**Penjelasan Program**](#Penjelasan-Program)
    * [**Model**](#Model)
    * [**View**](#View)
    * [**Controller**](#Controller)
------------------
### **Deskripsi Program**

Traveloka adalah program pelayanan kebutuhan perjalanan dan liburan yang telah dikenal di seluruh asia. Traveloka adalah program dengan sistem pelayanan pada pemesanan
tiket pesawat, hotel, dan lain lain. Alasan kami memilih Traveloka karena cocok untuk di implementasikan dengan struktur data dan algoritma yang sedang dipelajari saat ini,
yaitu Linked list, Search, dan Sort. 

-------------------
## **Implementasi Modul**

Adapun Modul yang digunakan dalam Project ini adalah :

* **PyMongo** : yaitu modul yang menghubungkan antara python dengan Mongodb yang merupakan Database berbasis Hosting/Server Online.

* **OS** : yaitu modul bawaan yang menyediakan akses ke fungsionalitads sistem operasi.

* **Time** : fungsi yang digunakan ialah sleep() yang berfungsi untuk menghentikan program untuk sementara dalam waktu tertentu, diatur dalam satuan detik.

* **PrettyTable** : yaitu modul yang digunakan untuk memanipulasi visual data yang akan ditampilkan dalam view.

* **SibApiV3Sdk** : yaitu modul yang digunakan untuk mengambil data dari API yang telah disediakan oleh Sendisblue.

* **Pwinput** : yaitu modul yang digunakan untuk mengambil inputan password tanpa menampilkan password yang diinputkan.

* **Dotenv** : yaitu modul yang digunakan untuk menghubungkan antara program dengan file .env yang berisi key - value dari MongoClient.

* **Random** : yaitu modul yang digunakan untuk mengambil data secara random.

* **DateTime** : yaitu modul yang digunakan untuk mengambil data tanggal dan waktu.
-------------------
## **Instalasi modul**

```bash
pip install pymongo
```

```bash
pip install prettytable
```

```bash
pip install python-time
```

```bash
pip install sib_api_v3_sdk
```

```bash
pip install pwinput
```

```bash
pip install python-dotenv
```

```bash
pip install random
```

```bash
pip install DateTime
```
-------------------
## **Struktur Program**

Konsep yang digunakan adalah MVC (Model, View, Controller). MVC adalah arsitektur pengelolaan program menjadi tiga bagian yaitu Model, View, Controller.

* Model Merupakan representasi data atau objek yang menyimpan informasi dan mengelola akses ke data. Model juga bertanggung jawab untuk memproses data, memvalidasi input, dan menyediakan antarmuka untuk mengakses dan memanipulasi data.

* View merupakan komponen antarmuka pengguna yang menampilkan data dan memungkinkan pengguna untuk berinteraksi dengan aplikasi. 

* Controller Merupakan komponen yang menghubungkan Model dan View. Controller bertanggung jawab untuk menerima input dari pengguna, 
memproses input tersebut dengan menggunakan Model, 
dan mengirimkan hasil pemrosesan tersebut ke View untuk ditampilkan.

## **Cara Penggunaan**

### **Opsi Awal**

![image](https://user-images.githubusercontent.com/121864328/233088413-2dc06c00-cf52-45da-af44-50b3a811c89d.png)

Ketika program pertama kali dijalankan user akan ditampilkan empat opsi awal yaitu "Registrasi Akun", "Login Akun", "Lupa Password", dan "Keluar Registrasi akun adalah opsi untuk mendaftar ke program sebagai pengguna baru. Login akun adalah opsi untuk masuk dengan menggunakan akun yang telah terdaftar. dan Lupa Password untuk membuat password baru apabila lupa dengan password yang lama. dan Opsi keluar untuk menutup program.

##### Registrasi Akun

1. Lakukan Pendaftaran dengan memasukkan username, password, saldo awal yang diinginkan. Kemudian masukkan email (email tidak boleh fiksi dan terdaftar)

![image](https://user-images.githubusercontent.com/121864328/233095033-0eb6920f-820b-4cf9-a9ba-d3feb28050f1.png)

2. Data registrasi akan dikonfirmasi dan tekan enter untuk lanjut

![image](https://user-images.githubusercontent.com/121864328/233095101-5301eb53-046d-4a47-a2eb-2eb73a45c87b.png)

##### Login Akun

Setelah akun telah terdaftar anda dapat login dengan memasukkan username dan password seperti contoh dibawah ini.

![image](https://user-images.githubusercontent.com/121864328/233096081-7196ac1b-f61d-46b1-bea9-548b0a2dd0bf.png)

Anda juga dapat login sebagai admin dengan akun yang telah dimiliki

##### Lupa Password

Masukkan username dan password baru.

![image](https://user-images.githubusercontent.com/121864328/233096757-8ef17533-6da6-48fc-9136-9ce66faec1f1.png)

### **Tampilan User**

![image](https://user-images.githubusercontent.com/121864328/233097666-5ad419e6-dcb6-4208-b0a0-fd10d3dc87e6.png)

Dengan login sebagai user, pengguna akan diarahkan ke beberapa menu regular bagi user.

##### Cari Tiket Pesawat

1. Ketika memilih opsi cari tiket pesawat program akan menampilkan daftar penerbangan penerbangan yang tersedia dan dapat dipesan. Penerbangan terdiri dari Id Flight, Nama pesawat, Asal, Tujuan, Waktu Keberangkatan, Waktu Kedatangan, Tanggal Keberangkatan, Harga. 

![image](https://user-images.githubusercontent.com/121864328/233098475-da425495-d038-456a-9119-900f24da7d7b.png)

2. Untuk memesan tiket pesawat, masukkan ID flight dari penerbangan yang diinginkan.

![image](https://user-images.githubusercontent.com/121864328/233099397-75da86df-7aac-4d18-9eca-379312242f14.png)

3. Setelah memesan, maka akan Invoice akan dikirimkan melalui email yang didaftarkan dengan bentuk receipt

![image](https://user-images.githubusercontent.com/121864328/233099790-227abab0-64f2-49dd-80c9-90f610167744.png)

##### Lihat Tiket Pesawat

Jika memilih Opsi lihat tiket pesawat, program akan menampilkan penerbangan yang tersedia untuk dipesan

![image](https://user-images.githubusercontent.com/121864328/233100305-ce914759-f340-48fa-b385-46539bb561c9.png)

##### Riwayat Pembelian

Sesuai namanya, riwayat pembelian berisi riwayat pemesanan pesawat dan riwayat pengisian saldo 

![image](https://user-images.githubusercontent.com/121864328/233100815-1994c961-d5d8-4c27-90fe-b1dff55e1d8e.png)

##### Isi saldo

isi saldo adalah opsi untuk mengisi saldo pada akun. Saldo yang diisi tidak dapat melebihi sepuluh juta.

![image](https://user-images.githubusercontent.com/121864328/233101378-9e2f027f-f36d-4a08-ae35-d084de869385.png)

##### Cek Profil

Cek profil adalah opsi untuk melihat data profil yaitu username, password, dan jumlah saldo

![image](https://user-images.githubusercontent.com/121864328/233101921-4c2e74e1-bd05-442a-8dea-577bd276ba68.png)

##### Urutkan data pesawat

Opsi ini adalah untuk mengsortir layanan penerbangan berdasarkan huruf abjad

![image](https://user-images.githubusercontent.com/121864328/233102252-7f7c4769-649f-44db-a6b1-08bbb05b0dc4.png)
 
##### Sign Out 
 
Pilih opsi ini untuk keluar dari akun.

### **Menu Admin**

![image](https://user-images.githubusercontent.com/121864328/233102910-a53931ab-80bd-4f13-a301-defe0f600d4e.png)

Ketika login sebagai admin menggunakan akun admin, akan diarahkan ke tampilan khusus admin yaitu "Tambah Pesawat", "Lihat Pesawat", "Edit Pesawat", "Hapus Pesawat", dan "Sign Out".

##### Tambah Pesawat

Opsi tambah pesawat adalah opsi bagi admin untuk menambahkan penerbangan dengan memasukkan beberapa data seperti nama, tujuan, harga, dan lain lain

![image](https://user-images.githubusercontent.com/121864328/233104372-44eebe22-25b1-42e9-902a-5289085c0eba.png)

##### Lihat Pesawat

Sama seperti user, terdapat opsi untuk melihat penerbangan yang tersedia

![image](https://user-images.githubusercontent.com/121864328/233104507-b1a95c83-fc96-4842-bc56-55e111eec1a5.png)

##### Edit Pesawat

Edit pesawat adalah fungsi update yang berfungsi untuk memperbarui data pesawat. Admin perlu memasukkan id pesawat yang ingin diubah dan data yang ingin diubah 

![image](https://user-images.githubusercontent.com/121864328/233105493-a4511243-cc60-4f40-bf44-e1d8d1142cd2.png)

![image](https://user-images.githubusercontent.com/121864328/233105997-4723cef2-dec9-4d31-9e36-6acee1a2f792.png)

##### Hapus Pesawat

Hapus pesawat adalah fungsi yang memunginkan bagi admin untuk menghapus layanan pesawat yang diinginkan dengan memasukkan id pesawat.

![image](https://user-images.githubusercontent.com/121864328/233106473-1875cef5-f2e7-4b25-99db-58e4afddc435.png)







-------------------
## **Penjelasan Program**
-------------------
## **Model**
### [**Model - database.py**](https://github.com/PA-ASD-Kelompok-2/traveloka/blob/main/Model/database.py)

Modul database.py merupakan kepala dari seluruh program Traveloka. 

##### Module Import
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
Pada source code diatas, kita menggunakan modul Pymongo sebagai alat penghubung antara Python dengan MongoDB (MongoClient), kemudian kita melakukan import dotenv yang berfungsi sebagai penghubung antara program dengan file .env yang berisi key - value dari MongoClient.

Kemudian load_dotenv() berfungsi untuk menarik key - value dari cluster MongoClient (getenv("MONGO_URI")) dan menyimpannya didalam dotenv. 

Lalu db = cluster["traveloka"] berfungsi untuk menghubungkan program Database.py dengan MongoClient yang terdapat cluster "Traveloka" didalamnya, lalu baris-baris selanjutnya berfungsi sebagai variabel pemanggil setiap bagian data program traveloka, yaitu akun, tiket pesawat, tiket hotel, dan transaksi.

-------------------
## **View**
### [**View - main_view.py**](https://github.com/PA-ASD-Kelompok-2/traveloka/blob/main/View/main_view.py)
Modul ini merupakan tampilan menu awal program Traveloka.

##### Module Import
```python
from Controller import auth_controller
import os
```

Pada source code diatas, kita akan memanggil folder Controller (MVC) yang
berisi file auth_controller.py yang berfungsi sebagai kontrol (Controller)
autentikasi bagi user, baik itu user biasa maupun user admin seperti login dan
register, dan lupa password.

##### Class MenuUtama
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
                    exit()
                else:
                    print('Opsi tidak tersedia!')
                    os.system('cls')
```
Source code class MenuUtama sendiri terdiri dari beberapa method yaitu methode inisiasi (__init__), dimana method tersebut akan melakukan inisiasi terhadap "auth" yang telah diimport sebelumnya, dan method run yang dimana berisi menu registrasi, login, lupa password, dan keluar. 

Jika user memilih opsi ke-1 yaitu
registrasi akun, maka modul akan merujuk ke modul auth_controller.py yang dimana, terdapat method register tersebut akan merujuk kedalam folder Model (MVC) yang berisi
database.py, yang telah terhubung kedalam MongoDB. 

Jika user memilih opsi ke-2, yaitu login akun, maka cara kerjanya sama,
yaitu modul akan merujuk ke modul auth_controller.py dimana
terdapat method login. Opsi ke-3 pun sama, yaitu merujuk kedalam
auth_controller.py. 

Jika user memilih opsi keluar, maka
program akan stop.

##### Error Handler
```python
 except KeyboardInterrupt:
            print('Terjadi kesalahan!')
            exit()
```
Source code diatas berfungsi sebagai penanganan / penyelesain jika terjadi error KeyboardInterrupt (CTRL + C).

### [**View - user_view.py**](https://github.com/PA-ASD-Kelompok-2/traveloka/blob/main/View/user_view.py)

Modul ini merupakan tampilan menu utama user.

##### Module Import
```python
from Controller import flight_controller as fc
from Controller import auth_controller as auth
from Controller import user_controller as uc
from View import main_view as main
import os
```
Pada source code diatas, kita melakukan import flight_controller.py dari folder Controller (MVC), dan akan dipanggil sebagai "fc". Selain flight_controller.py, kita juga akan melakukan import modul lainnya, yaitu auth_controller.py sebagai "auth", user_controller.py sebagai "uc" dan kita juga akan melakukan import modul main_view.py dari dalam folder View (MVC)

##### Class UserView
```python
class UserView:

    def __init__(self):
        self.flight = fc.LinkedList()
        self.auth = auth.User()
        self.user = uc.UserController()

    def menu_user(self):
        try:
            os.system('cls')
            while True:
                print("==================================")
                print("|            M E N U             |")
                print("==================================")
                print("|-----> Menu yang tersedia <-----|")
                print("|                                |")
                print("|    1. Cari Tiket Pesawat       |")
                print("|    2. Lihat Tiket Pesawat      |")
                print("|    3. Riwayat Pembelian        |")
                print("|    4. Isi Saldo                |")
                print("|    5. Cek Profil               |")
                print("|    6. Urutkan Data Pesawat     |")
                print("|    7. Sign Out                 |")
                print("|                                |")
                print("==================================")
                opsi = str(input("Tentukan opsi anda (1/2/3/4/5): "))

                if opsi == '1':
                    os.system('cls')
                    self.user.buyTicket()
                elif opsi == '2':
                    os.system('cls')
                    self.flight.display()
                elif opsi == '3':
                    os.system('cls')
                    self.user.checkHistory()
                elif opsi == '4':
                    os.system('cls')
                    self.user.addBalance()
                elif opsi == '5':
                    os.system('cls')
                    self.auth.profile()
                elif opsi == '6':
                    self.flight.sort_flights()
                elif opsi == '7':
                    self.auth.logout()
                    main.MenuUtama().run()
                else:
                    print("Opsi tidak tersedia!!")

        except KeyboardInterrupt:
            print("\nTerjadi Kesalahan!")
            exit()
```
Pada source code diatas, Class userview memiliki fungsi sebagai pusat tampilan menu utama bagi user yang dimana terdapat beberapa method seperti init dan menu_user. 

Method __init__ pada kelas diatas digunakan untuk menginisialisasi tiga atribut yaitu flight, auth, dan user. Atribut flight adalah sebuah objek dari kelas LinkedList yang didefinisikan dalam modul flight_controller dan diimport sebelumnya menggunakan alias fc, sedangkan atribut auth dan user adalah objek dari kelas User dan UserController masing-masing. 

Selain itu, kelas UserView juga memiliki method menu_user yang digunakan untuk menampilkan tampilan menu utama aplikasi dan menerima input dari pengguna. Pada method menu_user, terdapat sebuah loop while yang akan berjalan terus menerus hingga pengguna memilih opsi keluar dari aplikasi. Loop ini akan menampilkan tampilan menu utama aplikasi dan meminta pengguna untuk memilih opsi dengan memasukkan nomor opsi yang diinginkan.

Misalnya, jika pengguna memilih opsi untuk mencari tiket pesawat, program akan memanggil method buyTicket dari objek user untuk memulai proses pembelian tiket. Jika pengguna memilih opsi untuk melihat riwayat pembelian, program akan memanggil method checkHistory dari objek user untuk menampilkan riwayat pembelian yang dilakukan oleh pengguna tersebut.

Yang terakhir adalah opsi untuk keluar dari aplikasi, program akan memanggil method logout dari objek auth untuk logout dari aplikasi dan kembali ke menu utama dengan memanggil method run dari kelas MenuUtama yang didefinisikan dalam modul main_view.


### [**View - admin_view.py**](https://github.com/PA-ASD-Kelompok-2/traveloka/blob/main/View/admin_view.py)
Modul ini sebagai tampilan menu utama / display bagi administrator.

```python
from View import main_view as main
from Controller import flight_controller as fc
from Controller import auth_controller as auth
import os
```

Sama halnya dengan modul-modul sebelumnya, source code diatas akan melakukan import modul, yaitu main_view.py dari folder View (MVC) sert, flight_controller.py dan auth_controller.py dari folder Controller (MVC). 

Modul ini sendiri berisi method admin_menu, dimana didalamnya, terdapat menu tambah pesawat, lihat pesawat, edit pesawat, hapus pesawat, dan sign out. Admin_view.py terhubung dengan main_view.py, flight_controller.py, dan auth_controller.py.

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
                    os.system('cls')
                    self.flight.addFlight()
                elif opsi == '2':
                    os.system('cls')
                    self.flight.display()
                elif opsi == '3':
                    os.system('cls')
                    self.flight.updateFlight()
                elif opsi == '4':
                    os.system('cls')
                    self.flight.deleteFlight()
                elif opsi == '5':
                    self.auth.logout()
                    main.MenuUtama().run()
                else:
                    print("Opsi tidak tersedia!")
```
Setiap menu terhubung dengan beberapa kode program yang telah disebutkan diatas. 

Jika user memilih opsi ke-1, maka user akan merujuk flight_controller.py yang berada didalam Controller (MVC).Didalam method ini (menu_admin), user admin dapat menambah data pesawat, dimana fungsi ini sendiri terhubung dengan modul database.py. 

Selanjutnya
adalah opsi ke-2, yaitu "Lihat pesawat", opsi ini juga akan mengarahkan user kedalam flight_controller.py didalam Controller (MVC). Opsi ke-3 juga memiliki cara kerja
yang sama, yaitu modul akan merujuk ke flight_controller.py. Lalu opsi ke-4, maka modul akan merujuk kedalam Auth_controller.py didalam folder Controller (MVC).

-------------------
### [**Controller - auth_controller.py**](https://github.com/PA-ASD-Kelompok-2/traveloka/blob/main/Controller/auth_controller.py)
Modul ini sebagai kontrol autentikasi user.

```python
from Model import database as db
from View import admin_view
from View import user_view
import main
import pwinput
import os
import re
``` 
Sama halnya dengan source code sebelumnya, source code diatas akan melakuan import database.py dari dalam folder Model, dan admin_view.py dan user_view.py dari dalam folder View (MVC).
```python
class User:

    user_session = []
``` 

Didalam class User, terdapat list yaitu user_session, list ini berfungsi sebagai tempat penyimpanan sementara.

#### Fungsi Register

```python
def register(self):
        try:
            os.system('cls')
            print("----------------------- REGISTRASI ----------------------")
            name = str.capitalize(input("Masukkan username: "))
            if db.dataAcc.find_one({"name": name}):
                print("Username sudah digunakan!")
                return False
            if not name:
                print("Nama pengguna tidak boleh kosong!")
                return False
            elif re.search("[^A-Za-z0-9_]", name):
                print("Nama pengguna hanya boleh terdiri dari huruf, angka, dan underscore (_)!")
                return False
            else:
                password = str.lower(pwinput.pwinput("Masukkan password: "))
                if not password:
                    print("Kata sandi tidak boleh kosong!")
                    return False
                elif re.search("[^A-Za-z0-9!@#$%^&*()_+-=]", password):
                    print("Kata sandi hanya boleh terdiri dari huruf, angka, dan karakter simbol seperti !, @, #, $, %, ^, &, *, (, ), _, +, -, =!")
                    return False
``` 
Fungsi register untuk membuat sebuah akun baru bagi user bisa / pengguna, pada source code tersebut, user akan diminta untuk memasukkan 
username, yang dimana dilambangkan oleh variabel "name", username
sendiri akan otomatis menjadi huruf kapital. 

Kode "if db.dataAcc.find({"name": name})" yaitu jika username telah ada didalam db.dataAcc (MongoDB) dengan cara mencari "name" (Key), maka
akan return False dan melakukan print lalu melakukan perulangan. 

Lalu "if not name" yaitu jika input dibiarkan kosong (Null) maka akan return False, dan "re.search" yaitu modul untuk melakukan cek apakah
input username terdapat simbol-simbol "([^A-Za-z0-9!@#$%^&*()_+-=])", 
jika ada, maka program akan return False dan melakukan print lalu melakukan perulangan.
```python
else:
    password = str.lower(pwinput.pwinput("Masukkan password: "))
    if not password:
        print("Kata sandi tidak boleh kosong!")
        return False
    elif re.search("[^A-Za-z0-9!@#$%^&*()_+-=]", password):
        print("Kata sandi hanya boleh terdiri dari huruf, angka, dan karakter simbol seperti !, @, #, $, %, ^, &, *, (, ), _, +, -, =!")
        return False
``` 

Setelah seluruh kriteria pada username terpenuhi, maka user akan diminta untuk
melakukan input password (Input ini menggunakan modul pwinput) sesuai dengan kriteria sebelumnya, yaitu tidak boleh kosong, dan hanya menggunakan simbol -
simbol yang telah ditentukan.

```python
else:
     saldo = int(input("Masukkan saldo awal: "))
     if saldo < 0:
         print("Saldo tidak boleh kurang dari 0!")
         return False
     if saldo > 10000000:
         print("Saldo tidak boleh lebih dari 10.000.000!")
         return False
     else:
         email = str(input("Masukkan email: "))
         if not email:
             print("Email tidak boleh kosong!")
             return False
         elif email.count("@") > 1:
             print("Email hanya boleh satu simbol @!")
             return False
         elif email == db.dataAcc.find_one({"email": email}):
             print("Email sudah digunakan!")
             return False
         elif re.search("[^A-Za-z0-9@.]", email):
             print("Email hanya boleh terdiri dari huruf, angka, dan karakter simbol seperti @ dan .!")
             return False
``` 

Selanjutnya jika user telah memenuhi semua kriteria (username dan password), maka program akan berlanjut. Pada source kode diatas,
user akan diminta untuk mengisi saldo, jika saldo yang diinput adalah 0 / kosong, maka akan return False. Akan 
tetapi jika user melakukan pengisian melebihi ketentuan dalam
hal ini Rp.10.000.000, maka program akan return False.

Jika kriteria isi saldo telah terpenuhi, maka program akan
berlanjut ke tahap berikutnya, yaitu melakukan pengisian
email. Sama halnya dengan username, email juga tidak boleh kosong, serta hanya menggunakan simbol-simbol berdasarkan
ketentuan. 

```python
db.dataAcc.insert_one(
    {"name": name, "password": password, "saldo": saldo, "email": email, "privilege": "Reguler",
    "role": "user"})
print("\n--------------- DATA TELAH DIKONFRIMASI ---------------")
print("> Username: ", name)
print("> Password: ", password)
print("> Saldo: ", saldo)
print("> Email: ", email)
print("---------------------------------------------------------")
confirm = input("Tekan [ENTER] jika sesuai dengan anda input!")
if confirm == '':
    print("\nRegistrasi Berhasil!")
    return True
else:
    return True
``` 

Jika seluruh kriteria diatas terpenuhi (username, password, email, dan saldo) maka program akan melakukan "insert" data kedalam dataAcc didalam MongoDB. User sekarang dapat menggunakan akun yang telah dibuatnya.

#### Fungsi Login 

```python
def login(self):
        os.system('cls')
        print("----------------------- LOGIN ---------------------------")
        count = 3
        while count >= 0:
            count -= 1
            name = str.capitalize(input("> Masukkan username anda: "))
            password = str.lower(pwinput.pwinput("> Masukkan password anda: "))
            user = db.dataAcc.find_one({"name": name, "password": password})
            if user and user["name"] == name and user["password"] == password:
                if user:
                    if user.get("role") == "admin":
                        print("Login berhasil!")
                        self.logged_in = True
                        self.username = user["name"]
                        admin_view.AdminView().menu_admin()
                        return True
                    elif user.get("role") == "user":
                        print("Login berhasil!")
                        self.logged_in = True
                        self.username = user["name"]
                        session_data = {"username": self.username}
                        User.user_session.append(session_data)
                        user_view.UserView().menu_user()
                        return True
``` 

Kode "Count = 3" berfungsi sebagai jumlah penghitung jika user
melakukan salah input, baik itu username maupun password, dan "While
count" sebagai hitung mundur. Setelah user melakukan input pertama
kali, maka program akan melakukan pencocokan dengan data yang ada
didalam MongoDB, kode yang bekerja adalah "user = db.dataAcc
find_one({"name": name, "password": password})" dimana, jika username
serta password sama dengan data yang ada didalam database MongoDB,
maka user akan secara otomatis login. 

Akan tetapi sebelum itu, program akan melakukan pencocokan role dari
masing-masing akun, jika akun yang di input adalah akun admin
(Ditandai dengan role "admin") maka user akan secara otomatis login sebagai admin, dan akan dirujuk kedalam admin_view.py yang ada didalam folder View (MVC). 

-------------------
## **Controller**
### [**Controller - User_Controller.py**](https://github.com/PA-ASD-Kelompok-2/traveloka/blob/main/Controller/user_controller.py)

Modul ini berfungsi sebagai kontrol pengguna / user.

```python
from Controller import flight_controller as fc
from Controller import auth_controller as auth
from Controller import email_controller as email
from Model import database as db
from datetime import datetime
from prettytable import PrettyTable
``` 

"from controller import flight_controller as fc" : perintah untuk mengimport file "flight_controller.py" yang merepresentasikan suatu class yang akan diimport dari file bernama "Controller" dan diberikan alias "fc". Hal ini juga berlaku hingga baris ke empat. 

"from datetime import datetime" : Dalam baris kode ini, modul datetime dari library bawaan Python diimpor ke dalam program. Modul ini berisi kelas datetime yang digunakan untuk memanipulasi tanggal dan waktu dalam Python.

"from prettytable import PrettyTable" : Baris kode tersebut merupakan contoh penggunaan statement import pada Python untuk mengimpor modul PrettyTable ke dalam sebuah program. 

```python
class Node:
    def __init__(self, data=None, time=None):
        self.data = data
        self.time = time
        self.next = None
``` 

Class Node didefinisikan sebagai suatu Implementasi dari struktur data Linked List untuk merepresentasikan sebuah node atau simpul dalam linked list.

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data, time):
        new_node = Node(data, time) 
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def display(self):
        curr_node = self.head
        while curr_node:
            print (f"{curr_node.time}: {curr_node.data}") 
            curr_node = curr_node.next

```

Class Linked List adalah suatu implementasi salah satu fundamental struktur data yaitu Linked List. Linked List yang dipakai ialah singly linked list. Dalam class linked list terdapat dua method yaitu "append" yang berfungsi untuk menambahkan data melalui "node" atau simpul linked list, dan method "display" yang berfungsi untuk mencetak data yang ada didalam struktur data linked list. 

```python
class UserController:
    def __init__(self):
        self.flight = fc.LinkedList()
        self.db = db.dataFlight
        self.history = LinkedList()

    def buyTicket(self):
        try:
            user = db.dataAcc.find_one({"name": auth.User.user_session[0]['username']})
            self.flight.display()
            idFlight = str.upper(input("Masukkan ID Flight: "))
            self.flight.search(idFlight)
            if self.flight.search(idFlight):
                for d in self.db.find({"idFlight": idFlight}):
                    price = d['price']
                    total = price
                    if user['saldo'] >= total:
                        db.dataAcc.update_one({"name": user["name"]}, {"$inc": {"saldo": -total}})
                        print(f"Transaksi berhasil! Sisa saldo anda adalah: {user['saldo']}")
                        email.send_email(user['email'], d['idFlight'], user['name'], d['origin'], d['destination'], d['airline'], d['dateTime'], d['departureTime'], d['arrivalTime'], d['price'])

                        transaction = f"Beli tiket {total} untuk penerbangan {idFlight} dengan total harga {total}"
                        self.history.append(transaction, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

                    else:
                        print("Saldo tidak cukup!")
            else:
                print("Tiket tidak ditemukan")
                
        except KeyboardInterrupt:
            print("Terjadi Kesalahan!")

```

Class User Controller adalah Class yang berfungsi sebagai pengontrol alur kerja user, dan menghubungkannya ke struktur data yang lain. didalamnya terdapat beberapa method yaitu __init__ yang merupakan penginisialisasian atribut - atribut yang dimiliki seperti self.flight yang merepresentasikan penerbangan yang di inisialisasi sebagai linkedlist, self.db sebagai database flight dari model, dan self.history untuk riwayat yang diinisialisasikan sebagai linked list.

Method buy ticket Kode ini mendefinisikan sebuah metode buyTicket(), yang memungkinkan pengguna untuk membeli tiket penerbangan. Proses pembelian tiket melibatkan pencarian tiket berdasarkan ID penerbangan, mengambil harga tiket dari database, memeriksa saldo pengguna, dan memperbarui saldo pengguna serta mengirim email konfirmasi pembelian kepada pengguna. Jika saldo pengguna mencukupi, transaksi akan berhasil dan informasi transaksi akan ditambahkan ke riwayat transaksi. Namun, jika saldo pengguna tidak mencukupi atau tiket tidak ditemukan, maka pesan kesalahan akan ditampilkan.

```python
def addBalance(self):
        try:
            user = db.dataAcc.find_one({"name": auth.User.user_session[0]['username']})
            print("Saldo anda adalah: ", user['saldo'])

            add = int(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
            if add < 0:
                print("Jumlah saldo tidak boleh kurang dari 0")
                return
            if add > 10000000:
                print("Jumlah saldo tidak boleh lebih dari 10.000.000")
                return
            else:
                user['saldo'] += add
                db.dataAcc.update_one({"name": user["name"]}, {"$set": {"saldo": user['saldo']}})
                print(f"Saldo berhasil ditambahkan! Saldo sekarang adalah: {user['saldo']}")

                transaction = f"Menambahkan saldo sebesar {add}"
                self.history.append(transaction, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        except ValueError:
            print("Saldo harus berupa angka!")
        except KeyboardInterrupt:
            print("Terjadi Kesalahan!")
``` 

Kode ini mendefinisikan sebuah metode addBalance(), yang memungkinkan pengguna untuk menambahkan saldo ke akun mereka. Saat metode ini dijalankan, program akan mencari pengguna di database berdasarkan username yang sedang login, kemudian menampilkan saldo saat ini dari akun pengguna tersebut. Selanjutnya, program akan meminta pengguna untuk memasukkan jumlah saldo yang ingin ditambahkan, dan melakukan validasi jumlah saldo apakah lebih dari 0 dan tidak melebihi 10.000.000.

```python
def checkHistory(self):
        try:
            print("Transaction History:")
            table = PrettyTable()
            table.field_names = ["Tanggal", "Transaksi"]
            curr_node = self.history.head
            while curr_node:
                table.add_row([curr_node.time, curr_node.data])
                curr_node = curr_node.next
            
            print(table)

        except KeyboardInterrupt:
            print("Terjadi Kesalahan!")
``` 

Kode ini mendefinisikan sebuah metode checkHistory(), yang digunakan untuk menampilkan riwayat transaksi pengguna. Metode ini akan mencetak tabel yang menampilkan tanggal dan detail transaksi dari setiap elemen dalam riwayat transaksi. Data transaksi akan diambil dari setiap simpul pada struktur data linked list yang menyimpan riwayat transaksi. Setiap simpul pada linked list memiliki atribut data yang menyimpan detail transaksi dan atribut time yang menyimpan tanggal dan waktu transaksi terjadi.

-------------------
### [**Controller - email_controller.py**](https://github.com/PA-ASD-Kelompok-2/traveloka/blob/main/Controller/email_controller.py)
Modul ini sebagai kontrol email pengguna.
```python
from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv
import random
import os

load_dotenv()

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = os.getenv('SENDINBLUE_API_KEY')
```

Kode tersebut mendefinisikan sebuah fungsi send_email yang bertujuan untuk mengirim email transaksional melalui API Sendinblue. Fungsi ini memerlukan beberapa parameter, yaitu email, id_flight, name, asal, tujuan, pesawat, tanggal, waktu_keberangkatan, waktu_kedatangan, dan harga. Fungsi send_email menggunakan klien API Sendinblue untuk membuat objek email dengan menggunakan parameter yang diberikan, seperti to, params, dan template_id. Objek email kemudian dikirim menggunakan metode send_transac_email dari klien API Sendinblue. Jika terjadi kesalahan saat mengirim email, maka fungsi akan menampilkan pesan kesalahan menggunakan pernyataan print. Jika tidak ada kesalahan, maka hasil respons dari API Sendinblue akan dicetak menggunakan fungsi pprint.

```python
def send_email(email, id_flight, name, asal, tujuan, pesawat, tanggal, waktu_keberangkatan, waktu_kedatangan, harga):
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    receipt = str(random.randint(100000, 999999))
    ticket_code = str(random.randint(100000, 999999))
    to = [{"email": email, "name": name}]
    params = {
        "RECEIPT":receipt,
        "ID_FLIGHT": id_flight,
        "NAMA": name,
        "ASAL": asal,
        "TUJUAN": tujuan,
        "NAMA_PESAWAT": pesawat,
        "TANGGAL": tanggal,
        "WAKTU_KEBERANGKATAN": waktu_keberangkatan,
        "WAKTU_KEDATANGAN": waktu_kedatangan,
        "KODE_TIKET": ticket_code,
        "HARGA": harga
    }
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, params=params, template_id=1)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
```

Fungsi send_email menggunakan klien API Sendinblue untuk membuat objek email dengan menggunakan parameter yang diberikan, seperti to, params, dan template_id. Objek email kemudian dikirim menggunakan metode send_transac_email dari klien API Sendinblue.

-------------------
### [**Controller - flight_controller.py**](https://github.com/PA-ASD-Kelompok-2/traveloka/blob/main/Controller/flight_controller.py)
Modul berfungsi sebagai kontrol sistem tiket penerbangan traveloka.

```python
from Model import database as db
from prettytable import PrettyTable
import random
import os
import re
```
Pada kode diatas, kita melakukan import database dari folder
Model, dimana, database.py memiliki informasi-informasi
mengenai penerbangan seperti tiket, jadwal, harga dan lain
sebagainya.

#### Fungsi Append
```python
def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
```
Pada source code diatas, kita menggunakan fungsi append.....

#### Fungsi Display
```python
 def display(self):
        data = []
        for d in self.db.find({}):
            data.append(d)

        if not data:
                print("List kosong")
            else:
                table = PrettyTable(
                    ['ID Flight', 'Pesawat', 'Asal', 'Tujuan', 'Waktu Keberangkatan', 'Waktu Kedatangan', 'Tanggal Keberangkatan',
                    'Harga'])
                for d in data:
                    table.add_row(
                        [d['idFlight'], d['airline'], d['origin'], d['destination'], d['departureTime'], d['arrivalTime'],
                        d['dateTime'], d['price']])
                print(table)
```
Source code diatas berfungsi untuk menampilkan tiket yang dipilih oleh
user. Variabel "data" adalah sebuah list yang berfungsi sebagai 
penyimpanan sementara, dimana saat user mencari

#### Fungsi Search
```python
def search(self, key):
        data = []
        for d in self.db.find({}):
            data.append(d)

        if not data:
            print("List kosong")
            return

        n = len(data)
        step = int(n ** 0.5)
        prev = 0
        while prev < n and data[prev]['idFlight'] < key:
            prev += step
        prev -= step
        while prev < n:
            if data[prev]['idFlight'] == key:
                return Node(data[prev])
            prev += 1
        return None
```
Jenis search yang digunakan pada fungsi search diatas adalah
jump search. Digunakan untuk mencari data mengenai tiket
pesawat yang tersedia. Search menerima sebuah parameter key
lalu
melakukan pencarian pada data yang disimpan dalam database
dengan
berdasarkan "idFlight".

"for d in self.db.find({})" berfungsi sebagai iterasi data,
dengan
melakukan iterasi pada MongoDB yang ditandai dengan
variabel "db"
jika ketemu, maka source code akan melakukan append / menambah data
kedalam list sementara (variabel "data"). Jika data MongoDB kosong
maka akan return print "List Kosong".

Kemudian, jika data telah ditambah, maka search / pencarian akan 
dilakukan, dimulai dengan mencari panjang list yang ditandai dengan
variabel "n". Kode "step = int(n ** 0.5)" akan menghitung nilai dari
step. 

Kode "while prev < n and data[prev]['idFlight'] < key" akan
melakukan 
loop yang dimulai dari nilai variabel "prev" yaitu "0" yaitu
hingga
mencapai nilai "n" dalam hal ini panjang / seluruh data dari
database 
tiket pesawat (ditandai dengan variabel "db"). Loop akan terus
berlanjut hingga "prev" mencapai seluruh isi variabel n = "db".

Jika data menemukan kesamaan dengan key yang dicara (idFlight),
kode "return Node(data[prev])" akan mengembalikan item / objek
yang dicari dari dalam variabel "data" yang berisi list yang
telah di append sebelumnya.

Namun jika, key (idFlight) tidak sesuai dengan isi dari
variabel "data", maka program akan "return None".

#### Fungsi AddFlight
```python
 def addFlight(self):
        try:
            print("=====> Masukkan data penerbangan baru <=====")
            airline = str.capitalize(input("> Nama Pesawat: "))
            if not airline:
                print("Nama pesawat tidak boleh kosong!\n")
                return
            
            origin = str.capitalize(input("> Kota Asal: "))
            if not origin:
                print("Kota asal tidak boleh kosong!\n")
                return
            
            destination = str.capitalize(input("> Kota Tujuan: "))
            if not destination:
                print("Kota tujuan tidak boleh kosong!\n")
                return
            
            departureTime = str(input("> Waktu Keberangkatan (hh:mm):"))
            if not departureTime:
                print("Waktu keberangkatan tidak boleh kosong!\n")
                return
            elif re.match(r"([01]?[0-9]|2[0-3]):[0-5][0-9]", departureTime) is None:
                print("Format waktu keberangkatan salah!\n")
                return
            
            arrivalTime = str(input("> Waktu Kedatangan (hh:mm): "))
            if not arrivalTime:
                print("Waktu kedatangan tidak boleh kosong!\n")
                return
            elif re.match(r"([01]?[0-9]|2[0-3]):[0-5][0-9]", arrivalTime) is None:
                print("Format waktu kedatangan salah!\n")
                return
            
            dateTime = str(input("> Tanggal Keberangkatan (yyyy-mm-dd): "))
            if not dateTime:
                print("Tanggal keberangkatan tidak boleh kosong!\n")
                return
            elif len(dateTime) != 10:
                print("Format tanggal salah!\n")
                return
            elif re.match(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", dateTime) is None:
                print("Format tanggal salah!\n")
                return
            
            price = int(input("> Harga tiket: "))
            if not price:
                print("Harga tiket tidak boleh kosong!\n")
                return
            elif price < 0:
                print("Harga tiket tidak boleh kurang dari 0!\n")
                return
```
Source code diatas berkerja untuk menambah data baru kedalam
MongoDB, kode "try" berfungsi sebagai looping.

#### Fungsi idFlight
```python
def idFlight():
       if "garuda indonesia" in airline.lower():
           if "GA" + str(random.randint(100, 999)) == self.search("GA" + str(random.randint(100, 999))):
               return "GA" + str(random.randint(100, 999))
           else:
               return "GA" + str(random.randint(100, 999))

       elif "lion air" in airline.lower():
           if "JT" + str(random.randint(100, 999)) == self.search("JT" + str(random.randint(100, 999))):
               return "JT" + str(random.randint(100, 999))
           else:
               return "JT" + str(random.randint(100, 999))

       elif "sriwijaya air" in airline.lower():
           if "SJ" + str(random.randint(100, 999)) == self.search("SJ" + str(random.randint(100, 999))):
               return "SJ" + str(random.randint(100, 999))
           else:
               return "SJ" + str(random.randint(100, 999))

       elif "citilink" in airline.lower():
           if "QG" + str(random.randint(100, 999)) == self.search("QG" + str(random.randint(100, 999))):
               return "QG" + str(random.randint(100, 999))
           else:
               return "QG" + str(random.randint(100, 999))

       elif "air asia" in airline.lower():
           if "QZ" + str(random.randint(100, 999)) == self.search("QZ" + str(random.randint(100, 999))):
               return "QZ" + str(random.randint(100, 999))
           else:
               return "QZ" + str(random.randint(100, 999))

       elif "batik air" in airline.lower():
           if "ID" + str(random.randint(100, 999)) == self.search("ID" + str(random.randint(100, 999))):
               return "ID" + str(random.randint(100, 999))
           else:
               return "ID" + str(random.randint(100, 999))

       else:
           if "XX" + str(random.randint(100, 999)) == self.search("XX" + str(random.randint(100, 999))):
               return "XX" + str(random.randint(100, 999))
           else:
               return "XX" + str(random.randint(100, 999))
```
Lalu didalam fungsi addFlight, terdapat fungsi yang telah
dinested yaitu idFlight. idFlight berfungsi sebagai generator
nama bagi penerbangan, yaitu dengan menggunakan modul random
randint. Pada contoh diatas, garuda indonesia akan disingkat
menjadi GA lalu ditambah angka random dibelakangnya. Nama ini
nantinya akan menjadi idFlgiht (key utama dari penerbangan).

```python
new_flight = {
                "idFlight": idFlight(),
                "airline": airline,
                "origin": origin,
                "destination": destination,
                "departureTime": departureTime,
                "arrivalTime": arrivalTime,
                "dateTime": dateTime,
                "price": price
            }

            new_node = Node(new_flight)

            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

            self.db.insert_one(new_flight)
            print("Pesawat berhasil ditambahkan!\n")
        except ValueError:
            print("Masukkan data dengan benar!\n")
        except KeyboardInterrupt:
            print("Terjadi Kesalahan!\n")
```

Setelah user admin melakukan input, melengkapi semua data dari
fungsi-fungsi sebelumnya (addFlight). Maka kode diatas yaitu
variabel dictionary "new_flight" akan menambah data baru
kedalam Node. 

Jika node kosong, maka akan menambah node / head baru, namun
jika telah terdapat node dengan data yang sama dengan
new_flight, maka node akan berlanjut bagian selanjutnya.
Setelah menambah kedalam node baru, kode kemudian menambah
data baru kedalam database MongoDB.

#### Fungsi deleteFlight
```python   
def deleteFlight(self):
        try:
            print("Hapus Pesawat\n")
            self.display()
            idFlight = str(input("Masukkan ID Pesawat: "))
            self.search(idFlight)
            if self.search(idFlight):
                self.db.delete_one({"idFlight": idFlight})
                print("Pesawat berhasil dihapus!\n")
            elif not self.search(idFlight):
                print("Pesawat tidak ditemukan!\n")
            else:
                print("Pesawat tidak ditemukan!\n")

        except ValueError:
            print("Masukkan data dengan benar!\n")
        except KeyboardInterrupt:
            print("Terjadi Kesalahan!\n")

```
deleteFlight berfungsi untuk menghapus data pesawat, adapun key
untuk menghapus data pesawat adalah idFlight (id unik pesawat).
Dimana pada fungsi ini, kita juga akan menggunakan fungsi
jump search. 

#### Fungsi updateFlight
```python
  def updateFlight(self):
        print("Edit Pesawat\n")
        self.display()
        idFlight = str(input("Masukkan ID Pesawat yang ingin di update: "))
        self.search(idFlight)
        if self.search(idFlight):
            print('=================================')
            print('|   Apa yang ingin di update?   |')
            print('=================================')
            print('|>>>>> Silahkan pilih opsi <<<<<|')
            print('|                               |')
            print('|   1. Kota Asal                |')
            print('|   2. Kota Tujuan              |')
            print('|   3. Waktu Keberangkatan      |')
            print('|   4. Waktu Kedatangan         |')
            print('|   5. Tanggal Keberangkatan    |')
            print('|   6. Harga                    |')
            print('|   7. Kembali                  |')
            print('|                               |')
            print('=================================')
            update = str(input('Pilih data yang ingin di update: '))

            if update == '1':
                newData = str.capitalize(input("> Masukkan kota asal baru: "))
                if not newData:
                    print("Data tidak boleh kosong!\n")
                else:
                    self.db.update_one({"idFlight": idFlight}, {"$set": {"origin": newData}})
                    print("Data berhasil di update!\n")

            elif update == '2':
                newData = str.capitalize(input("> Masukkan kota tujuan baru: "))
                if not newData:
                    print("Data tidak boleh kosong!\n")
                else:
                    self.db.update_one({"idFlight": idFlight}, {"$set": {"destination": newData}})
                    print("Data berhasil di update!\n")

            elif update == '3':
                newData = str(input("> Masukkan waktu keberangkatan baru (hh:mm): "))
                if not newData:
                    print("Data tidak boleh kosong!\n")
                else:
                    self.db.update_one({"idFlight": idFlight}, {"$set": {"departureTime": newData}})
                    print("Data berhasil di update!\n")

            elif update == '4':
                newData = str(input("> Masukkan waktu kedatangan baru (hh:mm): "))
                if not newData:
                    print("Data tidak boleh kosong!\n")
                else:
                    self.db.update_one({"idFlight": idFlight}, {"$set": {"arrivalTime": newData}})
                    print("Data berhasil di update!\n")

            elif update == '5':
                newData = str(input("> Masukkan tanggal keberangkatan baru (yyyy-mm-dd): "))
                if not newData:
                    print("Data tidak boleh kosong!\n")
                else:
                    self.db.update_one({"idFlight": idFlight}, {"$set": {"dateTime": newData}})
                    print("Data berhasil di update!\n")

            elif update == '6':
                newData = int(input("> Masukkan harga baru: "))
                if newData < 0:
                    print("Harga tidak boleh kurang dari nol!\n")
                else:   
                    self.db.update_one({"idFlight": idFlight}, {"$set": {"price": newData}})
                    print("Data berhasil di update!\n")

            elif update == '7':
                return os.system('cls')

            else:
                print("Pilihan tidak tersedia!\n") 

        elif not self.search(idFlight):
            print("Pesawat tidak ditemukan!\n")
        else:
            print("Pesawat tidak ditemukan!\n")
```
Source code ini berfungsi untuk melakukan update pada data
penerbangan / maskapai pesawat yang hanya dapat dilakukan
oleh admininistrator. Pada contoh diatas, user dapat mencari
data pesawat yang ingin diganti / diubah dengan menggunakan
key (idFlight) dari masing-masing jenis maskapai penerbangan 
yang tersedia. 

Setelah user memilih opsi yang ingin di update / diubah, dalam contoh kasus ini adalah
kota asal penerbangan, maka program akan melakukan update data baru pada MongoDB, dengan 
kode "self.db.update_one({"idFlight": idFlight}, {"$set": {"origin": newData}})". Kode 
"$set" akan berkerja dan melakukan set / mengganti origin dengan key / origin baru dari
newData (input user).

#### Fungsi quick_sort
```python
 def quick_sort(self, data):
        if len(data) <= 1:
            return data

        pivot = data[0]
        left = []
        right = []

        for i in range(1, len(data)):
            if data[i]['airline'] < pivot['airline']:
                left.append(data[i])
            elif data[i]['airline'] > pivot['airline']:
                right.append(data[i])
            else:
                if data[i]['price'] < pivot['price']:
                    left.append(data[i])
                else:
                    right.append(data[i])
```
Fungsi quick_sort untuk melakukan sorting data. Pada source code diatas, terdapat "pivot", yaitu sebagai pembagi, dimana data akan dibagi menjadi dua bagian lalu variabel "left" dan "right" merupakan penyimpanan sementara, yang akan diappend / ditambah nantinya dari loop. 

Jika
len(data) <= 1 (data kurang dari 1), maka artinya data tersebut telah
terurut / tersorting, sehingga tidak perlu lagi dilakukan pengurutan. 

Variabel
pivot merupakan awal mula dari proses sorting, yaitu 0, pivot sendiri akan membagi data menjadi dua bagian. Jika data lebih dari 1, maka source
code quicksort diatas akan melakukan loop, dimana loop akan melakukan iterasi "[i]" beberapa kali sebanyak isi dari list data. 

Jika "airline" / data yang dicari kurang dari "airline", maka data akan di append / ditambah ke bagian variabel "left", jika "airline" lebih besar dari nilai "airline", maka data akan di append ke bagian variabel "right". 

Maksudnya adalah, "airline" akan melakukan perbandingan, dimana dalam kasus ini adalah huruf dan angka, contohnya QA dan QB, maka akan dilakukan perbandingan, dimana QA lebih dahulu daripada QB, karena A lebih kecil dari B. 

Namun jika nama sama, maka akan dilakukan perbandingan pada harga "data[i]['price'] < pivot['price']", dimana jika "price" pada "airline" yang diurutkan kurang dari "price" yang disamakan, maka akan di append ke variabel "left", sebaliknya akan di append ke variabel "right".

Dalam contoh kasus, QA dan QA memiliki nama sama, namun dengan harga berbeda, contohnya QA Rp.500,000 dengan QA Rp.700,000. Maka QA dengan harga Rp.500,000 akan diurutkan lebih dulu, tergantung diurut sebagai apa, bisa ascending maupun descending.

```python
        return self.quick_sort(left) + [pivot] + self quick_sort(right)
```
Setelah melakukan pengurutan tadi, maka nilai akan dikembalikan. Dan modul akan berlanjut ke source code berikutnya.

#### Fungsi quick_sort
```python
 def sort_flights(self):
        data = []
        for i in self.db.find():
            data.append(i)

        sorted_data = self.quick_sort(data)
        
        table = PrettyTable()
        table.title = "Data sortir berdasarkan nama pesawat"
        table.field_names = ['ID Flight', 'Pesawat', 'Asal', 'Tujuan', 'Waktu Keberangkatan', 'Waktu Kedatangan', 'Tanggal Keberangkatan',
                 'Harga']

        for flight in sorted_data:
            table.add_row(
                    [flight['idFlight'], flight['airline'], flight['origin'], flight['destination'], flight['departureTime'], flight['arrivalTime'],
                     flight['dateTime'], flight['price']])

        print(table)
```
Source code diatas merupakan lanjutan dari quick sort sebelumnya, kode akan mencari data penerbangan didalam MongoDB, lalu setelah itu akan dilakukan append kedalam variabel data list.

Setelah itu, modul akan menjalankan fungsi sebelumnya, yaitu quick sort, dan melakukan sorting data. Jika sudah, maka fungsi akan melakukan print tabel.
