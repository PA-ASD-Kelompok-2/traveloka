from Controller import auth_controller
import os

class MenuUtama:
    def __init__(self):
        self.auth = auth_controller.User()

    def register(self):
        self.auth.register()

    def login(self):
        self.auth.login()

    def forgot_password(self):
        self.auth.forgot_password()

    def logout(self):
        self.auth.logout()

class Main:
    def __init__(self):
        self.menu = MenuUtama()

    def run(self):
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
                self.menu.register()
            elif opsi == '2':
                self.menu.login()
            elif opsi == '3':
                self.menu.forgot_password()
            elif opsi == '4':
                self.menu.logout()
                break
            else:
                print('Opsi tidak tersedia!')

    def menuAdmin(self):
        while True:
            print("==================================")
            print("|            M E N U             |")
            print("==================================")
            print("|-----> Menu yang tersedia <-----|")
            print("|                                |")
            print("|    1. Menu Pesawat             |")
            print("|    2. Menu Hotel               |")
            print("|    3. Sign Out                 |")
            print("|                                |")
            print("==================================")
            opsi = str(input("Tentukan opsi anda (1/2/3/4/5): "))

            if opsi == '1':
                pass
                # menuPesawat()
            elif opsi == '2':
                pass
                # menuHotel()
            elif opsi == '3':
                self.menu.auth.logout()
                break
            else:
                print("Opsi tidak tersedia!")


    def menuUser(self):
        while True:
            print("==================================")
            print("|            M E N U             |")
            print("==================================")
            print("|-----> Menu yang tersedia <-----|")
            print("|                                |")
            print("|    1. Pesan Tiket Pesawat      |")
            print("|    2. Booking Hotel            |")
            print("|    3. Sign Out                 |")
            print("|                                |")
            print("==================================")
            opsi = str(input("Tentukan opsi anda (1/2/3/4/5): "))

            if opsi == '1':
                Main.userFlight(self)
            elif opsi == '2':
                pass
                # menuHotel()
            elif opsi == '3':
                self.menu.auth.logout()
                break
            else:
                print("Opsi tidak tersedia!")


    def userFlight(self):
        while True:
            print("==================================")
            print("|            M E N U             |")
            print("==================================")
            print("|-----> Menu yang tersedia <-----|")
            print("|                                |")
            print("|    1. Cari Tiket Pesawat       |")
            print("|    2. Pemesanan Tiket          |")
            print("|    3. Sign Out                 |")
            print("|                                |")
            print("==================================")
            opsi = str(input("Tentukan opsi anda (1/2/3/4/5): "))

            if opsi == '1':
                pass
            elif opsi == '2':
                pass
            elif opsi == '3':
                self.menu.auth.logout()
                break
            else:
                print("Opsi tidak tersedia!")


if __name__ == '__main__':
    app = Main()
    app.run()
