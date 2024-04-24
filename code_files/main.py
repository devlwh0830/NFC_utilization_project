import nfcs, show, pymongo, system_db, datetime

client = pymongo.MongoClient("MongoDB URL")
db = client["COLLECTION_NAME"]
collection = db["DB_NAME"]

while(True):
    try:
        reader = nfcs.Reader()
        a = reader.get_uid()
        a = f"{a[0]}{a[1]}{a[2]}{a[3]}"
        result = collection.find_one({"NFC":f"{a}"})
        if result != None:
            system_db.checking(a)
        else:
            show.TagSystem(int(1111111111))
    except:
        pass