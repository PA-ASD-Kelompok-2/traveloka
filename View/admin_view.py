from View import main_view as main
from Controller import flight_controller as fc
from Controller import auth_controller as auth
import os

class AdminView:

    def __init__(self):
        self.flight = fc.LinkedList()
        self.auth = auth.User()

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
                    main.MenuUtama().run()
                else:
                    print("Opsi tidak tersedia!")

        except KeyboardInterrupt:
            print("\nTerjadi Kesalahan!")
            exit()

