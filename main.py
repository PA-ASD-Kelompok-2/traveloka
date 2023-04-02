from Controller import auth_controller
from Controller import flight_controller as fc
import os


class Main:

    def __init__(self):
        self.auth = auth_controller.User()
        self.flight = fc.Flight()

    def register(self):
        self.auth.register()

    def login(self):
        self.auth.login()

    def forgot_password(self):
        self.auth.forgot_password()

    def logout(self):
        self.auth.logout()


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


if __name__ == '__main__':
    main = MenuUtama()
    main.run()
