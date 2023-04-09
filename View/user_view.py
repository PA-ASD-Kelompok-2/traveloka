from Controller import flight_controller as fc
from Controller import auth_controller as auth
from Controller import user_controller as uc
from View import main_view as main
import os


class UserView:

    def __init__(self):
        self.flight = fc.LinkedList()
        self.auth = auth.User()
        self.user = uc.UserController()

    def menu_user(self):
        try:
            os.system('cls')
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
                print("|    6. Urutkan Data Pesawat     |")
                print("|    7. Sign Out                 |")
                print("|                                |")
                print("==================================")
                opsi = str(input("Tentukan opsi anda (1/2/3/4/5): "))

                if opsi == '1':
                    self.user.buyTicket()
                elif opsi == '2':
                    self.flight.display()
                elif opsi == '3':
                    self.user.checkHistory()
                elif opsi == '4':
                    self.user.addBalance()
                elif opsi == '5':
                    self.auth.profile()
                elif opsi == '6':
                    self.flight.sort()
                elif opsi == '7':
                    main.MenuUtama().run()
                else:
                    print("Opsi tidak tersedia!!")

        except KeyboardInterrupt:
            print("\nTerjadi Kesalahan!")
            exit()


