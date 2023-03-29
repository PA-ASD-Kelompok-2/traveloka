from Model import mongodb as db
import main
import pwinput

class User:
    def __init__(self):
        self.logged_in = False
        self.main = main
        self.username = ""
        self.password = ""
        self.role = ""

    def register(self):
        print("=== Register ===")
        name = str.capitalize(input("Masukkan username: "))
        if db.dataAcc.find_one({"name": name}):
            print("Username sudah digunakan!")
            return False
        else:
            password = str(pwinput.pwinput("Masukkan password: "))
            saldo = int(input("Masukkan saldo awal: "))
            email = str(input("Masukkan email: "))
            db.dataAcc.insert_one({"name": name, "password": password, "saldo": saldo, "email": email, "privilege": "Reguler" ,"role": "user"})
            print("Registrasi berhasil!")
            return True

    def login(self):
        print("=== Login ===")
        name = str.capitalize(input("Masukkan username: "))
        password = str(pwinput.pwinput("Masukkan password: "))
        user = db.dataAcc.find_one({"name": name, "password": password})
        if user["role"] == "admin":
            print("Login berhasil!")
            self.logged_in = True
            self.username = user["name"]
            self.password = user["password"]
            self.role = user["role"]
            self.main.Main.menuAdmin(self)
            return True
        
        elif user["role"] == "user":
            print("Login berhasil!")
            self.logged_in = True
            self.username = user["name"]
            self.password = user["password"]
            self.role = user["role"]
            self.main.Main.menuUser(self)
            return True
        
        else:
            print("Username atau password salah!")
            return False

    def forgot_password(self):
        print("=== Lupa Password ===")
        name = input("Masukkan username: ")
        user = db.dataAcc.find_one({"name": name})
        if user:
            new_password = pwinput.pwinput("Masukkan password baru: ")
            db.dataAcc.update_one({"name": name}, {"$set": {"password": new_password}})
            print("Password berhasil diubah!")
            return True
        else:
            print("Username tidak ditemukan!")
            return False

    def logout(self):
        if self.logged_in:
            print(f"User {self.username} berhasil logout")
            self.logged_in = False
            self.username = ""
            self.password = ""
            self.role = ""
        else:
            print("Tidak ada user yang login saat ini!")

