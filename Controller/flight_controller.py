from Model import database as db
from prettytable import PrettyTable
import random
import os

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.data = None
        self.tail = None
        self.db = db.dataFlight


    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        data = []
        for d in self.db.find({}):
            data.append(d)

        if not data:
            print("List kosong")
        else:
            table = PrettyTable(
                ['ID Flight', 'Pesawat', 'Asal', 'Tujuan', 'Waktu Keberangkatan', 'Waktu Kedatangan', 'Tanggal Keberangkatan',
                 'Harga'])
            for d in data:
                table.add_row(
                    [d['idFlight'], d['airline'], d['origin'], d['destination'], d['departureTime'], d['arrivalTime'],
                     d['dateTime'], d['price']])
            print(table)

    def search(self, key):
        data = []
        for d in self.db.find({}):
            data.append(d)

        if not data:
            print("List kosong")
            return

        n = len(data)
        step = int(n ** 0.5)
        prev = 0
        while prev < n and data[prev]['idFlight'] < key:
            prev += step
        prev -= step
        while prev < n:
            if data[prev]['idFlight'] == key:
                return Node(data[prev])
            prev += 1
        return None


    def addFlight(self):
        try:
            print("=====> Masukkan data penerbangan baru <=====")
            airline = str.capitalize(input("> Nama Pesawat: "))
            if not airline:
                print("Nama pesawat tidak boleh kosong!\n")
                return
            
            origin = str.capitalize(input("> Kota Asal: "))
            if not origin:
                print("Kota asal tidak boleh kosong!\n")
                return
            
            destination = str.capitalize(input("> Kota Tujuan: "))
            if not destination:
                print("Kota tujuan tidak boleh kosong!\n")
                return
            
            departureTime = str(input("> Waktu Keberangkatan (hh:mm):"))
            if not departureTime:
                print("Waktu keberangkatan tidak boleh kosong!\n")
                return
            
            arrivalTime = str(input("> Waktu Kedatangan (hh:mm): "))
            if not arrivalTime:
                print("Waktu kedatangan tidak boleh kosong!\n")
                return
            
            dateTime = str(input("> Tanggal Keberangkatan (yyyy-mm-dd): "))
            if not dateTime:
                print("Tanggal keberangkatan tidak boleh kosong!\n")
                return
            
            price = int(input("> Harga tiket: "))
            if not price:
                print("Harga tiket tidak boleh kosong!\n")
                return

            def idFlight():
                if "garuda indonesia" in airline.lower():
                    if "GA" + str(random.randint(100, 999)) == self.search("GA" + str(random.randint(100, 999))):
                        return "GA" + str(random.randint(100, 999))
                    else:
                        return "GA" + str(random.randint(100, 999))
                    
                elif "lion air" in airline.lower():
                    if "JT" + str(random.randint(100, 999)) == self.search("JT" + str(random.randint(100, 999))):
                        return "JT" + str(random.randint(100, 999))
                    else:
                        return "JT" + str(random.randint(100, 999))
                    
                elif "sriwijaya air" in airline.lower():
                    if "SJ" + str(random.randint(100, 999)) == self.search("SJ" + str(random.randint(100, 999))):
                        return "SJ" + str(random.randint(100, 999))
                    else:
                        return "SJ" + str(random.randint(100, 999))
                    
                elif "citilink" in airline.lower():
                    if "QG" + str(random.randint(100, 999)) == self.search("QG" + str(random.randint(100, 999))):
                        return "QG" + str(random.randint(100, 999))
                    else:
                        return "QG" + str(random.randint(100, 999))
                    
                elif "air asia" in airline.lower():
                    if "QZ" + str(random.randint(100, 999)) == self.search("QZ" + str(random.randint(100, 999))):
                        return "QZ" + str(random.randint(100, 999))
                    else:
                        return "QZ" + str(random.randint(100, 999))
                    
                elif "batik air" in airline.lower():
                    if "ID" + str(random.randint(100, 999)) == self.search("ID" + str(random.randint(100, 999))):
                        return "ID" + str(random.randint(100, 999))
                    else:
                        return "ID" + str(random.randint(100, 999))
                    
                else:
                    if "XX" + str(random.randint(100, 999)) == self.search("XX" + str(random.randint(100, 999))):
                        return "XX" + str(random.randint(100, 999))
                    else:
                        return "XX" + str(random.randint(100, 999))

            new_flight = {
                "idFlight": idFlight(),
                "airline": airline,
                "origin": origin,
                "destination": destination,
                "departureTime": departureTime,
                "arrivalTime": arrivalTime,
                "dateTime": dateTime,
                "price": price
            }

            new_node = Node(new_flight)

            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

            self.db.insert_one(new_flight)
            print("Pesawat berhasil ditambahkan!\n")
        except ValueError:
            print("Masukkan data dengan benar!\n")
        except KeyboardInterrupt:
            print("Terjadi Kesalahan!\n")

    def deleteFlight(self):
        try:
            print("Hapus Pesawat\n")
            self.display()
            idFlight = str(input("Masukkan ID Pesawat: "))
            self.search(idFlight)
            if self.search(idFlight):
                self.db.delete_one({"idFlight": idFlight})
                print("Pesawat berhasil dihapus!\n")
            elif not self.search(idFlight):
                print("Pesawat tidak ditemukan!\n")
            else:
                print("Pesawat tidak ditemukan!\n")

        except ValueError:
            print("Masukkan data dengan benar!\n")
        except KeyboardInterrupt:
            print("Terjadi Kesalahan!\n")


    def updateFlight(self):
        print("Edit Pesawat\n")
        self.display()
        idFlight = str(input("Masukkan ID Pesawat yang ingin di update: "))
        self.search(idFlight)
        if self.search(idFlight):
            print('=================================')
            print('|   Apa yang ingin di update?   |')
            print('=================================')
            print('|>>>>> Silahkan pilih opsi <<<<<|')
            print('|                               |')
            print('|   1. Kota Asal                |')
            print('|   2. Kota Tujuan              |')
            print('|   3. Waktu Keberangkatan      |')
            print('|   4. Waktu Kedatangan         |')
            print('|   5. Tanggal Keberangkatan    |')
            print('|   6. Harga                    |')
            print('|   7. Kembali                  |')
            print('|                               |')
            print('=================================')
            update = str(input('Pilih data yang ingin di update: '))

            if update == '1':
                newData = str.capitalize(input("> Masukkan kota asal baru: "))
                if not newData:
                    print("Data tidak boleh kosong!\n")
                else:
                    self.db.update_one({"idFlight": idFlight}, {"$set": {"origin": newData}})
                    print("Data berhasil di update!\n")

            elif update == '2':
                newData = str.capitalize(input("> Masukkan kota tujuan baru: "))
                if not newData:
                    print("Data tidak boleh kosong!\n")
                else:
                    self.db.update_one({"idFlight": idFlight}, {"$set": {"destination": newData}})
                    print("Data berhasil di update!\n")

            elif update == '3':
                newData = str(input("> Masukkan waktu keberangkatan baru (hh:mm): "))
                if not newData:
                    print("Data tidak boleh kosong!\n")
                else:
                    self.db.update_one({"idFlight": idFlight}, {"$set": {"departureTime": newData}})
                    print("Data berhasil di update!\n")

            elif update == '4':
                newData = str(input("> Masukkan waktu kedatangan baru (hh:mm): "))
                if not newData:
                    print("Data tidak boleh kosong!\n")
                else:
                    self.db.update_one({"idFlight": idFlight}, {"$set": {"arrivalTime": newData}})
                    print("Data berhasil di update!\n")

            elif update == '5':
                newData = str(input("> Masukkan tanggal keberangkatan baru (yyyy-mm-dd): "))
                if not newData:
                    print("Data tidak boleh kosong!\n")
                else:
                    self.db.update_one({"idFlight": idFlight}, {"$set": {"dateTime": newData}})
                    print("Data berhasil di update!\n")

            elif update == '6':
                newData = int(input("> Masukkan harga baru: "))
                if newData < 0:
                    print("Harga tidak boleh kurang dari nol!\n")
                else:   
                    self.db.update_one({"idFlight": idFlight}, {"$set": {"price": newData}})
                    print("Data berhasil di update!\n")

            elif update == '7':
                return os.system('cls')

            else:
                print("Pilihan tidak tersedia!\n") 

        elif not self.search(idFlight):
            print("Pesawat tidak ditemukan!\n")
        else:
            print("Pesawat tidak ditemukan!\n")


    def quick_sort(self, data):
        if len(data) <= 1:
            return data

        pivot = data[0]
        left = []
        right = []

        for i in range(1, len(data)):
            if data[i]['airline'] < pivot['airline']:
                left.append(data[i])
            elif data[i]['airline'] > pivot['airline']:
                right.append(data[i])
            else:
                if data[i]['price'] < pivot['price']:
                    left.append(data[i])
                else:
                    right.append(data[i])

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)

    def sort_flights(self):
        data = []
        for i in self.db.find():
            data.append(i)

        sorted_data = self.quick_sort(data)
        
        table = PrettyTable()
        table.title = "Data sortir berdasarkan nama pesawat"
        table.field_names = ['ID Flight', 'Pesawat', 'Asal', 'Tujuan', 'Waktu Keberangkatan', 'Waktu Kedatangan', 'Tanggal Keberangkatan',
                 'Harga']

        for flight in sorted_data:
            table.add_row(
                    [flight['idFlight'], flight['airline'], flight['origin'], flight['destination'], flight['departureTime'], flight['arrivalTime'],
                     flight['dateTime'], flight['price']])

        print(table)


