import requests
import time
import datetime
import json
import pprint
import InfoGetterIF

class weatherGetter(InfoGetterIF.InfoGetterIF):
    def _gatherData(self):
#        url = "https://api.open-meteo.com/v1/forecast?latitude=35.6785&longitude=139.6823&hourly=temperature_2m&hourly=precipitation&timezone=Asia%2FTokyo"
        INDDICT = json.load(open("individualData.json",'r'))
        URLDICT = json.load(open("API.json",'r'))
        url = URLDICT["weather"] + INDDICT["iriyama"]["location_id"]


        res = requests.get(url)
        data = json.loads(res.text)
        city = "Nagoya"
        #pprint.pprint(data)
        temp_hi = data["forecasts"][1]["temperature"]["max"]["celsius"]
        temp_lo = data["forecasts"][1]["temperature"]["min"]["celsius"]
        prcp = str(int(data["forecasts"][1]["chanceOfRain"]["T06_12"].strip("%"))/100)
        date = str(datetime.date.today() + datetime.timedelta(days=1))

        # DBに格納
        queryDict = {
            "data" : [
                ["city", "\'"+city+"\'"],
                ["temp_lo", str(temp_lo)],
                ["temp_hi", str(temp_hi)],
                ["prcp", str(prcp)],
                ["date", "\'"+date+"\'"],
                ["checked", "false"]
            ],
            "table" : "weather"
        }       

#        pprint.pprint(queryDict)
        return queryDict