from Model import mongodb as db
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
            if "garuda" in airline.lower():
                return "GA" + str(random.randint(100, 999))
            elif "lion" in airline.lower():
                return "JT" + str(random.randint(100, 999))
            elif "sriwijaya" in airline.lower():
                return "SJ" + str(random.randint(100, 999))
            elif "citilink" in airline.lower():
                return "QG" + str(random.randint(100, 999))
            elif "airasia" in airline.lower():
                return "QZ" + str(random.randint(100, 999))
            elif "batik" in airline.lower():
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
        idFlight = str(input("Masukkan ID Pesawat yang ingin di update: "))

        update = str(input('''
        1. Nama Pesawat
        2. Kota Asal
        3. Kota Tujuan
        4. Waktu Keberangkatan
        5. Waktu Kedatangan
        6. Tanggal Keberangkatan
        7. Harga
        
        Pilih data yang ingin di update: '''))

        if update == '1':
            newData = str(input("Masukkan nama pesawat baru: "))
            self.db.update_one({"idFlight": idFlight}, {"$set": {"airline": newData}})
            print("Data berhasil di update!\n")

        elif update == '2':
            newData = str(input("Masukkan kota asal baru: "))
            self.db.update_one({"idFlight": idFlight}, {"$set": {"origin": newData}})
            print("Data berhasil di update!\n")

        elif update == '3':
            newData = str(input("Masukkan kota tujuan baru: "))
            self.db.update_one({"idFlight": idFlight}, {"$set": {"destination": newData}})
            print("Data berhasil di update!\n")

        elif update == '4':
            newData = str(input("Masukkan waktu keberangkatan baru: "))
            self.db.update_one({"idFlight": idFlight}, {"$set": {"departureTime": newData}})
            print("Data berhasil di update!\n")

        elif update == '5':
            newData = str(input("Masukkan waktu kedatangan baru: "))
            self.db.update_one({"idFlight": idFlight}, {"$set": {"arrivalTime": newData}})
            print("Data berhasil di update!\n")

        elif update == '6':
            newData = str(input("Masukkan tanggal keberangkatan baru: "))
            self.db.update_one({"idFlight": idFlight}, {"$set": {"dateTime": newData}})
            print("Data berhasil di update!\n")

        elif update == '7':
            newData = int(input("Masukkan harga baru: "))
            self.db.update_one({"idFlight": idFlight}, {"$set": {"price": newData}})
            print("Data berhasil di update!\n")

        else:
            print("Pilihan tidak tersedia!\n")
