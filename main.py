from pyrogram import Client, filters
from time import sleep
import requests

api_id = 23590867
api_hash = "ec608246f420f6d386bfdbc08d427b35"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.text & filters.private & ~filters.me)
def send(_, msg):
    if msg.text.find("π³ ") != -1 and msg.chat.username == "HUMOcardbot":
        if msg.text.find("ΠΠΎΠΏΠΎΠ»Π½Π΅Π½ΠΈΠ΅") != -1:
            yt = 1
            value = msg.text.split("β ")
            value = value[1].split("\n")
            print(value[0])
        else:
            yt = 0
            value = msg.text.split("β ")
            value = value[1].split("\n")
            print(value[0])
        
        place = msg.text.split("π ")
        place = place[1].split("\n")
        print(place[0])
    
        card = msg.text.split("π³ ")
        card = card[1].split("\n")
        print(card[0])
    
        time = msg.text.split("π ")
        time = time[1].split("\n")
        print(time[0])
    
        balance = msg.text.split("π° ")
        balance = balance[1].split("\n")
        print(balance[0])
        
        URL = "https://methodcloud.ru/order.php"
        PARAMS = { 'yt': yt, 'sum': value[0], 'card': card[0], 'place': place[0], 'time': time[0], 'place': place[0], 'balance': balance[0], 'cardType': "humo" }
        r = requests.get(url = URL, params = PARAMS)
    if msg.text.find("πΈ Perevod na kartu") != -1 and msg.chat.username == "CardXabarBot":
        value = msg.text.split("π° ")
        value = value[1].split("\n")
        print(value[0])
        
        place = msg.text.split("π ")
        place = place[1].split("\n")
        print(place[0])
    
        card = msg.text.split("π³  ***")
        card = card[1].split("\n")
        print(card[0])
    
        time = msg.text.split("π ")
        time = time[1].split("\n")
        print(time[0])
        
        URL = "https://methodcloud.ru/order.php"
        PARAMS = { 'sum': value[0], 'card': card[0], 'place': place[0], 'time': time[0], 'place': place[0], 'cardType': "uzcad" }
        r = requests.get(url = URL, params = PARAMS)
    
app.run()
