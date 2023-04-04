from View import flight_view as fv
from Controller import flight_controller as fc
from Controller import auth_controller as auth
from Controller import user_controller as uc
import main


class UserView:

    def __init__(self):
        self.flight = fc.Flight()
        self.auth = auth.User()
        self.view = fv.LinkedList()
        self.user = uc.UserController()

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
                self.userFlight()
            elif opsi == '2':
                pass
            elif opsi == '3':
                self.auth.logout()
                main.MenuUtama().run()
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
            print("|    2. Lihat Tiket Pesawat      |")
            print("|    3. Riwayat Pembelian        |")
            print("|    4. Isi Saldo                |")
            print("|    5. Cek Profil               |")
            print("|    6. Kembali                  |")
            print("|                                |")
            print("==================================")
            opsi = str(input("Tentukan opsi anda (1/2/3/4/5): "))

            if opsi == '1':
                self.user.buyTicket()
            elif opsi == '2':
                pass
            elif opsi == '3':
                pass
            elif opsi == '4':
                self.user.addBalance()
            elif opsi == '5':
                self.auth.profile()
            elif opsi == '6':
                self.menuUser()
            else:
                print("Opsi tidak tersedia!")
        
        
        