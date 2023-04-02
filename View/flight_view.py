from prettytable import PrettyTable
from Model import mongodb as db


class FligthView:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.db = db.dataFlight

    def append(self, data):
        new_node = FligthView(data)
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
                ['ID Flight', 'Airline', 'Origin', 'Destination', 'Departure Time', 'Arrival Time', 'Date Time',
                 'Price'])
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
                return FligthView(data[prev])
            prev += 1
        return None
