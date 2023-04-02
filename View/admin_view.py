from Controller import flight_controller as fc
from Controller import auth_controller as auth
import flight_view as fv

class MenuAdmin:
    
    def __init__(self):
        self.flight = fc.Flight()
        self.auth = auth.User()
        self.view = fv.LinkedList()

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
                self.auth.logout()
            else:
                print("Opsi tidak tersedia!")

