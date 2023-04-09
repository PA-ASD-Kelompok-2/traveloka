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

    def display(self, offset=0, limit=10):
        data = []
        for d in self.db.find({}).skip(offset).limit(limit):
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
            airline = str(input("> Nama Pesawat: "))
            origin = str(input("> Kota Asal: "))
            destination = str(input("> Kota Tujuan: "))
            departureTime = str(input("> Waktu Keberangkatan (hh:mm):"))
            arrivalTime = str(input("> Waktu Kedatangan (hh:mm): "))
            dateTime = str(input("> Tanggal Keberangkatan (yyyy-mm-dd): "))
            price = int(input("> Harga tiket: "))

            def idFlight():
                if "garuda indonesia" in airline.lower():
                    return "GA" + str(random.randint(100, 999))
                elif "lion air" in airline.lower():
                    return "JT" + str(random.randint(100, 999))
                elif "sriwijaya air" in airline.lower():
                    return "SJ" + str(random.randint(100, 999))
                elif "citilink" in airline.lower():
                    return "QG" + str(random.randint(100, 999))
                elif "air asia" in airline.lower():
                    return "QZ" + str(random.randint(100, 999))
                elif "batik air" in airline.lower():
                    return "ID" + str(random.randint(100, 999))
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
            self.db.update_one({"idFlight": idFlight}, {"$set": {"origin": newData}})
            print("Data berhasil di update!\n")

        elif update == '2':
            newData = str.capitalize(input("> Masukkan kota tujuan baru: "))
            self.db.update_one({"idFlight": idFlight}, {"$set": {"destination": newData}})
            print("Data berhasil di update!\n")

        elif update == '3':
            newData = str(input("> Masukkan waktu keberangkatan baru (hh:mm): "))
            self.db.update_one({"idFlight": idFlight}, {"$set": {"departureTime": newData}})
            print("Data berhasil di update!\n")

        elif update == '4':
            newData = str(input("> Masukkan waktu kedatangan baru (hh:mm): "))
            self.db.update_one({"idFlight": idFlight}, {"$set": {"arrivalTime": newData}})
            print("Data berhasil di update!\n")

        elif update == '5':
            newData = str(input("> Masukkan tanggal keberangkatan baru (yyyy-mm-dd): "))
            self.db.update_one({"idFlight": idFlight}, {"$set": {"dateTime": newData}})
            print("Data berhasil di update!\n")

        elif update == '6':
            newData = int(input("> Masukkan harga baru: "))
            self.db.update_one({"idFlight": idFlight}, {"$set": {"price": newData}})
            print("Data berhasil di update!\n")

        elif update == '7':
            return os.system('cls')

        else:
            print("Pilihan tidak tersedia!\n") 


    # def merge_sort(self, key):
    #     data = []

    #     for i in self.db.find({}):
    #         data.append(i)

    #     if not data:
    #         print("Data kosong!\n")
    #         return
            
    #     if len(data) > 1:
    #         mid = len(data) // 2
    #         left = data[:mid]
    #         right = data[mid:]

    #         self.merge_sort(left)
    #         self.merge_sort(right)

    #         i = j = k = 0

    #         while i < len(left) and j < len(right):
    #             if left[i][key] < right[j][key]:
    #                 data[k] = left[i]
    #                 i += 1
    #             else:
    #                 data[k] = right[j]
    #                 j += 1
    #             k += 1

    #         while i < len(left):
    #             data[k] = left[i]
    #             i += 1
    #             k += 1

    #         while j < len(right):
    #             data[k] = right[j]
    #             j += 1
    #             k += 1

        
    # def sort(self):
    #     print('=================================')
    #     print('|   Apa yang ingin di sort?     |')
    #     print('=================================')
    #     print('|>>>>> Silahkan pilih opsi <<<<<|')
    #     print('|                               |')
    #     print('|   1. Harga                    |')
    #     print('|   2. Waktu Keberangkatan      |')
    #     print('|   3. Waktu Kedatangan         |')
    #     print('|   4. Kembali                  |')
    #     print('|                               |')
    #     print('=================================')
    #     sort = str(input('Pilih data yang ingin di sort: '))

    #     if sort == '1':
    #         self.merge_sort("price")
    #         self.display()

    #     elif sort == '2':
    #         self.merge_sort("departureTime")
    #         self.display()

    #     elif sort == '3':
    #         self.merge_sort("arrivalTime")
    #         self.display()

    #     elif sort == '4':
    #         return os.system('cls')

    #     else:
    #         print("Pilihan tidak tersedia!\n")
        



