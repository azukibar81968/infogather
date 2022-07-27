import requests
import time
import datetime
import json
import pprint
import InfoGetterIF

class weatherGetter(InfoGetterIF.InfoGetterIF):
    def _gatherData(self):
        url = "https://api.open-meteo.com/v1/forecast?latitude=35.6785&longitude=139.6823&hourly=temperature_2m&hourly=precipitation&timezone=Asia%2FTokyo"
        res = requests.get(url)
        data = json.loads(res.text)
        city = "Tokyo"
        temp_hi = max(data["hourly"]["temperature_2m"][24:48])
        temp_lo = min(data["hourly"]["temperature_2m"][24:48])
        prcp = max(data["hourly"]["precipitation"][:24])
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
        return queryDict