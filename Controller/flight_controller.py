from Model import mongodb as db

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

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def addFlight(self):
        print("Tambah Pesawat\n")
        airline = str(input("Nama Pesawat: "))
        origin = str(input("Kota Asal: "))
        destination = str(input("Kota Tujuan: "))
        departureTime = str(input("Waktu Keberangkatan (hh:mm):"))
        arrivalTime = str(input("Waktu Kedatangan (hh:mm): "))
        dateTime = str(input("Tanggal Keberangkatan (yyyy-mm-dd): "))
        price = int(input("Harga: "))


        new_flight = {
            "airline": airline,
            "origin": origin,
            "destination": destination,
            "departureTime": departureTime,
            "arrivalTime": arrivalTime,
            "dateTime": dateTime,
            "price": price
        }

        db.dataFlight.insert_one(new_flight)

        data = f"{airline} | {origin} | {destination} | {departureTime} | {arrivalTime} | {dateTime} | {price}"
        self.append(data)

        print("Pesawat berhasil ditambahkan!\n")


