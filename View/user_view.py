from View import flight_view as fv
from Controller import flight_controller as fc
from Controller import auth_controller as auth
import main


class UserView:

    def __init__(self):
        self.flight = fc.Flight()
        self.auth = auth.User()
        self.view = fv.LinkedList()

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
                pass
            elif opsi == '2':
                pass
            elif opsi == '3':
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
                UserView.menuUser(self)
            else:
                print("Opsi tidak tersedia!")
