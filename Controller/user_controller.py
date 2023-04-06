from Controller import flight_controller as fc
from Controller import auth_controller as auth
from Controller import email_controller as email
from Model import database as db
import random


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def display(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


class UserController:
    def __init__(self):
        self.flight = fc.LinkedList()
        self.db = db.dataFlight
        self.history = LinkedList()  # create a linked list for the transaction history

    def buyTicket(self):
        user = db.dataAcc.find_one({"name": auth.User.user_session[0]['username']})
        self.flight.display()
        idFlight = str.upper(input("Masukkan ID Flight: "))
        self.flight.search(idFlight)
        if self.flight.search(idFlight):
            sumTicket = int(input("Masukkan jumlah tiket: "))
            if sumTicket > 0:
                for d in self.db.find({"idFlight": idFlight}):
                    price = d['price']
                    total = price * sumTicket
                    if user['saldo'] >= total:
                        db.dataAcc.update_one({"name": user["name"]}, {"$inc": {"saldo": -total}})
                        print(f"Transaksi berhasil! Sisa saldo anda adalah: {user['saldo']}")
                        ticket_code = str(random.randint(10000000, 99999999))
                        email.send_mail(user['email'], '67088001', idFlight, user['name'], d['origin'],
                                        d['destination'], d['airline'], ticket_code)

                        transaction = f"Beli tiket {sumTicket} untuk penerbangan {idFlight} dengan total harga {total}"
                        self.history.append(transaction)

                    else:
                        print("Saldo tidak cukup!")
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

        transaction = f"Menambahkan saldo sebesar {add}"
        self.history.append(transaction)

    def checkHistory(self):
        print("Transaction History:")
        self.history.display()
