import pymongo, datetime,show
from discord_webhook import DiscordWebhook

def checking(nfc:str):
    client = pymongo.MongoClient("MongoDB URL")
    now = datetime.datetime.now()
    nowTime = now.strftime('%H:%M:%S')
    db = client["COLLECTION_NAME"]
    postcollection = db["DB_NAME"]
    results = postcollection.find_one({"NFC":f"{nfc}"})
    if results == None:
        show.TagSystem("in")
        collection = db["DB_NAME"]
        result = collection.find_one({"NFC":f"{nfc}"})
        post = {
            "NFC" : f"{nfc}", # str
            "DATE" : f"{datetime.date.today()}", # str
            "INTIME" : f"{nowTime}", # str
            "OUTTIME" : None
        }
        postcollection.insert_one(post)
        content1= [
            {
            "title": "메이커스페이스(5층) 입실이 확인 되었습니다.",
            "color": 5814783,
            "fields": [
                {
                "name": "이름",
                "value": str(result["NAME"]),
                "inline": True
                },
                {
                "name": "학번",
                "value": str(result["STUDENT_CODE"]),
                "inline": True
                },
                {
                "name": "입실시각",
                "value": f"{nowTime}",
                "inline": True
                }
            ]
            }
        ]
        webhook = DiscordWebhook(url='WEBHOOK URL', content=None,embeds=content1)
        response = webhook.execute()
        print(response.status_code)
    else:
        show.TagSystem("out")
        postcollection.update_one({"NFC":f"{nfc}"},{"$set":{"OUTTIME":f"{nowTime}"}})
        a = str(results["INTIME"]).replace(":","")
        b = str(datetime.date.today()).replace("-","")
        past = datetime.datetime.strptime(f"{b}{a}", "%Y%m%d%H%M%S")
        diff = now - past
        ltime = str(diff).split(".")
        ltimes = ltime[0].split(":")
        collection = db["DB_NAME"]
        result = collection.find_one({"NFC":f"{nfc}"})
        content2= [
            {
            "title": "메이커스페이스(5층) 퇴실이 확인 되었습니다.",
            "color": 5814783,
            "fields": [
                {
                "name": "이름",
                "value": str(result["NAME"]),
                "inline": True
                },
                {
                "name": "학번",
                "value": str(result["STUDENT_CODE"]),
                "inline": True
                },
                {
                "name": "날짜",
                "value": f"{datetime.date.today()}",
                "inline": True
                },
                {
                "name": "입실시각 / 퇴실시각",
                "value": str(results["INTIME"])+f" / {nowTime}",
                "inline": False
                },
                {
                "name": "동아라실에서 머문시간",
                "value": f"{ltimes[0]}시간 {ltimes[1]}분 {ltimes[2]}초 동안 있었습니다.",
                "inline": False
                }
            ]
            }
        ]

        webhook = DiscordWebhook(url='WEBHOOK URL', content=None,embeds=content2)
        response = webhook.execute()
        print(response.status_code)
        postcollection.delete_one({"NFC":f"{nfc}"})
