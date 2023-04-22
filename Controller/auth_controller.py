from Model import database as db
from View import admin_view
from View import user_view
import main
import pwinput
import os
import re


class User:

    user_session = []

    def __init__(self):
        self.logged_in = False
        self.main = main
        self.username = ""

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
                        elif re.search("[^@]", email):
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
                            
        except TypeError:
            print("Saldo harus berupa angka!")
            return False
        except ValueError:
            print("Saldo harus berupa angka!")
            return False
        except KeyboardInterrupt:
            print("\nTerjadi Kesalahan")
            return False

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
            else:
                print('Username atau Password Salah!')
                print('Anda Memiliki', count, 'Kali Percobaan')
                if count == 0:
                    print('Anda telah mencapai batas maksimum percobaan login. Silakan coba lagi nanti.')
                    return False
                    

    def forgot_password(self):
        print("----------------------- LUPA PASSWORD -------------------")
        name = str.capitalize(input("> Masukkan username: "))
        user = db.dataAcc.find_one({"name": name})
        if user:
            new_password = str.lower(pwinput.pwinput("> Masukkan password baru: "))
            if not new_password:
                print("Kata sandi tidak boleh kosong!")
                return False
            else:
                db.dataAcc.update_one({"name": name}, {"$set": {"password": new_password}})
                print("Password berhasil diubah!")
                return True
        else:
            print("Username tidak ditemukan!")
            return False
            

    def logout(self):
        User.user_session = []
        print("Tidak ada user yang login saat ini!")


    def profile(self):
        print("----------------------- PROFILE -------------------------")
        data = User.user_session[0]["username"]
        user = db.dataAcc.find_one({"name": data})
        if user:
            print("Nama: ", user["name"])
            print("Saldo: ", user["saldo"])
            print("Email: ", user["email"])
            print("---------------------------------------------------------")
            confirm = input("Tekan [ENTER] jika ingin kembali ke menu utama!")
            if confirm == '':
                user_view.UserView().menu_user()
            else:
                user_view.UserView().menu_user()
        else:
            print("User tidak ditemukan!")
            return False
            
