from Controller import auth_controller
from Controller import flight_controller as fc
from View import flight_view
import os

class Main:


    def __init__(self):
        self.auth = auth_controller.User()
        self.flight = fc.LinkedList()
        self.flight_view = flight_view.LinkedList()

    def register(self):
        self.auth.register()

    def login(self):
        self.auth.login()
        
    def forgot_password(self):
        self.auth.forgot_password()

    def logout(self):
        self.auth.logout()

    def add_flight(self):
        self.flight.addFlight()

    def view_flight(self):
        self.flight_view.display()


class MenuUtama:


    def __init__(self):
        self.main = Main()


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
                self.main.register()
            elif opsi == '2':
                self.main.login()
            elif opsi == '3':
                self.main.forgot_password()
            elif opsi == '4':
                print('Terima kasih telah menggunakan layanan kami!')
                exit()
            else:
                print('Opsi tidak tersedia!')
        

    def menuAdmin(self):
        while True:
            print("==================================")
            print("|            M E N U             |")
            print("==================================")
            print("|-----> Menu yang tersedia <-----|")
            print("|                                |")
            print("|    1. Halaman Pesawat          |")
            print("|    2. Halaman Hotel            |")
            print("|    3. Sign Out                 |")
            print("|                                |")
            print("==================================")
            opsi = str(input("Tentukan opsi anda (1/2/3/4/5): "))

            if opsi == '1':
                MenuUtama.adminFlight(self)
            elif opsi == '2':
                pass
            elif opsi == '3':
                MenuUtama.run(self)
            else:
                print("Opsi tidak tersedia!")


    def adminFlight(self):
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
                
                Main().add_flight()
            elif opsi == '2':
                Main().view_flight()
            elif opsi == '3':
                pass
            elif opsi == '4':
                pass
            elif opsi == '5':
                MenuUtama.run(self)
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
                MenuUtama.userFlight(self)
            elif opsi == '2':
                pass
                # menuHotel()
            elif opsi == '3':
                MenuUtama.run(self)
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
            print("|    3. Kembali                  |")
            print("|                                |")
            print("==================================")
            opsi = str(input("Tentukan opsi anda (1/2/3/4/5): "))

            if opsi == '1':
                pass
            elif opsi == '2':
                pass
            elif opsi == '3':
                MenuUtama.menuUser(self) 
            else:
                print("Opsi tidak tersedia!")
    


if __name__ == '__main__':
    main = MenuUtama()
    main.run()
