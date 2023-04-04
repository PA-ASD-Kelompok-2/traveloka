from Model import mongodb as db
from View import flight_view as fv
import random


class Flight:
    def __init__(self):
        self.db = db.dataFlight

    def addFlight(self):
        print("Tambah Pesawat\n")
        airline = str(input("Nama Pesawat: "))
        origin = str(input("Kota Asal: "))
        destination = str(input("Kota Tujuan: "))
        departureTime = str(input("Waktu Keberangkatan (hh:mm):"))
        arrivalTime = str(input("Waktu Kedatangan (hh:mm): "))
        dateTime = str(input("Tanggal Keberangkatan (yyyy-mm-dd): "))
        price = int(input("Harga: "))

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

        self.db.insert_one(new_flight)
        print("Pesawat berhasil ditambahkan!\n")

    def deleteFlight(self):
        print("Hapus Pesawat\n")
        idFlight = str(input("Masukkan ID Pesawat: "))
        self.db.delete_one({"idFlight": idFlight})
        print("Pesawat berhasil dihapus!\n")

    def updateFlight(self):
        print("Edit Pesawat\n")
        fv.LinkedList().display()
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

        else:
            print("Pilihan tidak tersedia!\n")


