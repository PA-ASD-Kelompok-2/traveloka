from Controller import flight_controller as fc
from Controller import auth_controller as auth

class MenuAdmin:
    
    def __init__(self):
        self.flight = fc.LinkedList()

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
                fc.LinkedList.addFlight(self)
            elif opsi == '2':
                pass    
            elif opsi == '3':
                pass
            elif opsi == '4':
                pass
            elif opsi == '5':
                auth.User.logout(self)
            else:
                print("Opsi tidak tersedia!")

