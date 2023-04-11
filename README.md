# Dokumentasi Proyek Akhir Algoritma dan Struktur Data
## "Implementasi Algoritma dan Struktur Data pada Big Project Traveloka"

### Deskripsi Program

Traveloka adalah program pelayanan kebutuhan perjalanan dan liburan yang telah dikenal di seluruh asia. Traveloka adalah program dengan sistem pelayanan pada pemesanan
tiket pesawat, hotel, dan lain lain. Alasan kami memilih Traveloka karena cocok untuk di implementasikan dengan struktur data dan algoritma yang sedang dipelajari saat ini,
yaitu Linked list, Search, dan Sort. 

#### Implementasi Modul

Adapun Modul yang digunakan dalam Project ini adalah :

* PyMongo: yaitu modul yang menghubungkan antara python dengan Mongodb yang merupakan Database berbasis Hosting/Server Online.
* Clear Screen (cls): yang merupakan modul untuk memberikan efek clear pada screen terminal.
* Time: fungsi yang digunakan ialah sleep() yang berfungsi untuk menghentikan program untuk sementara dalam waktu tertentu, diatur dalam satuan detik.
* PrettyTable: yaitu modul yang digunakan untuk memanipulasi visual data yang akan ditampilkan dalam view.

#### Instalasi modul

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
#### Struktur Program

Konsep yang digunakan adalah MVC (Model, view, Controller). MVC adalah arsitektur pengelolaan program menjadi tiga bagian yaitu Model, View, Controller.

* Model Merupakan representasi data atau objek yang menyimpan informasi dan mengelola akses ke data. Model juga bertanggung jawab untuk memproses data, memvalidasi input, dan menyediakan antarmuka untuk mengakses dan memanipulasi data.
* View merupakan komponen antarmuka pengguna yang menampilkan data dan memungkinkan pengguna untuk berinteraksi dengan aplikasi. 
* Controller Merupakan komponen yang menghubungkan Model dan View. Controller bertanggung jawab untuk menerima input dari pengguna, 
memproses input tersebut dengan menggunakan Model, 
dan mengirimkan hasil pemrosesan tersebut ke View untuk ditampilkan.

### Penjelasan Program 
#### Model - database.py
Modul database.py merupakan kepala dari seluruh program Traveloka. 

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

Didalam modul ini, kita menggunakan modul Pymongo sebagai alat penghubung antara Python dengan MongoDB (MongoClient), kemudian kita melakukan import dotenv yang berfungsi sebagai penghubung antara program dengan file .env yang berisi key - value dari MongoClient.

Kemudian load_dotenv() berfungsi untuk menarik key - value dari cluster MongoClient (getenv("MONGO_URI")) dan menyimpannya didalam dotenv. 

Lalu db = cluster["traveloka"] berfungsi untuk menghubungkan program Database.py dengan MongoClient yang terdapat cluster "Traveloka" didalamnya, lalu baris-baris selanjutnya berfungsi sebagai variabel pemanggil setiap bagian data program traveloka, yaitu akun, tiket pesawat, tiket hotel, dan transaksi.

#### View - main_view.py
Modul ini merupakan tampilan menu awal program Traveloka.

![image](https://user-images.githubusercontent.com/126738691/231107335-02c9fa7a-4d00-4a63-8ebc-0364f816aa85.png)

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

Modul ini sendiri terdiri dari beberapa menu yaitu registrasi, login, lupa password, dan keluar. Jika user memilih opsi ke-1 yaitu registrasi aku, maka modul 
akan merujuk ke modul auth_controller.py yaitu pada bagian register, yang dimana, fungsi register tersebut akan merujuk kedalam folder MODEL (MVC) yang berisi
database.py, yang telah terhubung kedalam MongoClient. Jika user memilih opsi ke-2, yaitu login akun, maka cara kerjanya sama, yaitu modul akan merujuk ke modul
auth_controller.py dimana terdapat fungsi login. Opsi ke-3 pun sama, yaitu merujuk kedalam auth_controller.py. Jika user memilih opsi keluar, maka program akan stop.

```python
 except KeyboardInterrupt:
            print('Terjadi kesalahan!')
            exit()
```
Source code diatas berfungsi sebagai penanganan / penyelesain jika terjadi error KeyboardInterrupt.

#### View - admin_view.py
Modul ini sebagai tampilan menu utama / display bagi administrator.

![image](https://user-images.githubusercontent.com/126738691/231103225-fb1cd0ed-3aad-4451-8a3c-251da80fa0d2.png)

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
didalam Controller (MVC), didalam fungsi ini, user dapat admin dapat menambah data pesawat, dan fungsi ini sendiri terhubung dengan modul database.py. Selanjutnya
adalah opsi ke-2, yaitu "Lihat pesawat", opsi ini juga akan mengarahkan user kedalam flight_controller.py didalam Controller (MVC). Opsi ke-3 juga memiliki cara kerja
yang sama, yaitu modul akan merujuk ke flight_controller.py. Lalu opsi ke-4, maka modul akan merujuk kedalam Auth_controller.py didalam folder Controller (MVC).

#### Controller - auth_controller.py
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
Source code diatas akan melakuan import database.py dari dalam folder Model, lalu admin_view.py dan user_view.py dari dalam folder View (MVC).
Selanjutnya adalah import main.......###.
```python
class User:

    user_session = []
``` 

Didalam class User, terdapat list yaitu user_session, list ini berfungsi sebagai tempat penyimpanan sementara.

##### Fungsi Register

```python
fdef register(self):
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

Kode "if db.dataAcc.find({"name": name})" yaitu jika username telah ada didalam db.dataAcc (MongoClient) dengan cara mencari "name" (Key), maka
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
        elif re.search("[^A-Za-z0-9@.]", email):
            print("Email hanya boleh terdiri dari huruf, angka, dan karakter simbol seperti @ dan .!")
            return False
        elif re.search("[^@]", email):
            db.dataAcc.insert_one(
                {"name": name, "password": password, "saldo": saldo, "email": email, "privilege": "Reguler",
                "role": "user"})
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

Jika seluruh kriteria diatas terpenuhi (username, password, email, dan saldo) maka program akan melakukan "insert" data kedalam dataAcc di
dalam MongoClient. User sekarang dapat menggunakan akun yang telah dibuatnya.

##### Fungsi Login 

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
didalam MongoClient, kode yang bekerja adalah "user = db.dataAcc
find_one({"name": name, "password": password})" dimana, jika username
serta password sama dengan data yang ada didalam database MongoClient,
maka user akan secara otomatis login. 

Akan tetapi sebelum itu, program akan melakukan pencocokan role dari
masing-masing akun, jika akun yang di input adalah akun admin
(Ditandai dengan role "admin") maka user akan secara otomatis login
sebagai admin, dan akan dirujuk kedalam admin_view.py yang ada didalam folder View (MVC). 

#### User_Controller.py


```python
from Controller import flight_controller as fc
from Controller import auth_controller as auth
from Controller import email_controller as email
from Model import database as db
from datetime import datetime
from prettytable import PrettyTable
``` 

"from controller import flight_controller as fc" adalah perintah untuk mengimport modul "flight_controller" yang merepresentasikan suatu class yang akan diimport dari file bernama "Controller" dan diberikan alias "fc". Hal ini juga berlaku hingga baris ke empat. 

"from datetime import datetime" Dalam baris kode ini, modul datetime dari library bawaan Python diimpor ke dalam program. Modul ini berisi kelas datetime yang digunakan untuk memanipulasi tanggal dan waktu dalam Python.

"from prettytable import PrettyTable" Baris kode tersebut merupakan contoh penggunaan statement import pada Python untuk mengimpor modul PrettyTable ke dalam sebuah program. 

```python
class Node:
    def __init__(self, data=None, time=None):
        self.data = data
        self.time = time
        self.next = None
``` 

Node didefinisikan sebagai suatu Implementasi dari struktur data Linked List untuk merepresentasikan sebuah node atau simpul dalam linked list.

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
            # print(curr_node.data)
            print (f"{curr_node.time}: {curr_node.data}") 
            curr_node = curr_node.next


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

Class Linked List adalah suatu implementasi salah satu fundamental struktur data yaitu Linked List. Linked List yang dipakai ialah singly linked list. Dalam class linked list terdapat dua method yaitu "append" yang berfungsi untuk menambahkan data melalui "node" atau simpul linked list, dan method "display" yang berfungsi untuk mencetak data yang ada didalam struktur data linked list. 

Class User Controller adalah Class yang berfungsi sebagai pengontrol alur kerja user, dan menghubungkannya ke struktur data yang lain. didalamnya terdapat beberapa method yaitu __init__ yang merupakan penginisialisasian atribut - atribut yang dimiliki seperti self.flight yang merepresentasikan penerbangan yang di inisialisasi sebagai linkedlist, self.db sebagai database flight dari model, dan self.history untuk riwayat yang diinisialisasikan sebagai linked list.

method buy ticket Kode ini mendefinisikan sebuah metode buyTicket(), yang memungkinkan pengguna untuk membeli tiket penerbangan. Proses pembelian tiket melibatkan pencarian tiket berdasarkan ID penerbangan, mengambil harga tiket dari database, memeriksa saldo pengguna, dan memperbarui saldo pengguna serta mengirim email konfirmasi pembelian kepada pengguna. Jika saldo pengguna mencukupi, transaksi akan berhasil dan informasi transaksi akan ditambahkan ke riwayat transaksi. Namun, jika saldo pengguna tidak mencukupi atau tiket tidak ditemukan, maka pesan kesalahan akan ditampilkan.

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

#### Controller - email_controller.py
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


#### Controller - flight_controller.py

