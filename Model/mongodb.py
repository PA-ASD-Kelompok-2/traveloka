from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://fauzan:CPbQN3LiePx39fmNPfssAtYkq3Q7jJACCP7dMNft@sandbox.u1rbk.mongodb.net/?retryWrites=true&w=majority")

db = cluster["traveloka"]

dataAcc = db["account"]
dataFlight = db["flight"]
dataHotel = db["hotel"]
dataTransaction = db["transaction"]
