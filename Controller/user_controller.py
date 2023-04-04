from View import flight_view as fv
from Controller import flight_controller as fc
from Controller import auth_controller as auth
from Model import mongodb as db

class UserController:

    def __init__(self):
        self.flight = fc.Flight()
        self.view = fv.LinkedList()
        self.db = db.dataFlight

    def buyTicket(self):
        user = db.dataAcc.find_one({"name": auth.User.user_session[0]['username']})
        self.view.display()
        idFlight = str.upper(input("Masukkan ID Flight: "))
        self.view.search(idFlight)
        if self.view.search(idFlight):
            sumTicket = int(input("Masukkan jumlah tiket: "))
            if sumTicket > 0:
                for d in self.db.find({"idFlight": idFlight}):
                    price = d['price']
                    total = price * sumTicket
                    if user['saldo'] >= total:
                        db.dataAcc.update_one({"name": user["name"]}, {"$inc": {"saldo": -total}})
                        print(f"Transaksi berhasil! Sisa saldo anda adalah: {user['saldo']}")
            else:
                print("Jumlah tiket tidak boleh kurang dari 1!")     
        else:
            print("Tiket tidak ditemukan")

    def addBalance(self):
        user = db.dataAcc.find_one({"name": auth.User.user_session[0]['username']})
        print("Saldo anda adalah: ", user['saldo'])
        
        add = int(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
        user['saldo'] += add
        db.dataAcc.update_one({"name": user["name"]}, {"$set": {"saldo": user['saldo']}})
        print(f"Saldo berhasil ditambahkan! Saldo sekarang adalah: {user['saldo']}")

    def checkHistory(self):
        pass
    
    