from View import flight_view as fv
from Controller import flight_controller as fc
from Controller import auth_controller as auth
import main


class AdminView:

    def __init__(self):
        self.flight = fc.Flight()
        self.auth = auth.User()
        self.view = fv.LinkedList()

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
                AdminView.adminFlight(self)
            elif opsi == '2':
                pass
            elif opsi == '3':
                main.MenuUtama().run()
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
                self.flight.addFlight()
            elif opsi == '2':
                self.view.display()
            elif opsi == '3':
                self.flight.updateFlight()
            elif opsi == '4':
                self.flight.deleteFlight()
            elif opsi == '5':
                main.MenuUtama().run()
            else:
                print("Opsi tidak tersedia!")

