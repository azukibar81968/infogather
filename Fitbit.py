import InfoGetterIF
import fitbit
import datetime
from ast import literal_eval
import json
import pprint

class fitbitGetter(InfoGetterIF.InfoGetterIF):
    def __init__(self):
        self.IND_DATA = "individualData.json"
        
        token_dict = json.load(open(self.IND_DATA, 'r'))
        self.CLIENT_ID     = token_dict["iriyama"]["fitbit_client_id"]
        self.CLIENT_SECRET = token_dict["iriyama"]["fitbit_client_secret"]
        self.TOKEN = token_dict["iriyama"]["fitbit_token"]
        self.REFRESH_TOKEN = token_dict["iriyama"]["fitbit_refresh_token"]

    def updateToken(self, token):
        f = open(self.IND_DATA, 'w')
        token_dict = json.load(f)
        token_dict["fitbit_token"] = token
        f.write(str(token_dict))
        f.close()
        return

    def pound_to_kg(self, pound):
        kg = pound * 0.454
        return kg

    def _gatherData(self):

        client = fitbit.Fitbit(self.CLIENT_ID, self.CLIENT_SECRET,
            access_token = self.TOKEN, refresh_token = self.REFRESH_TOKEN, refresh_cb = self.updateToken)

        TODAY = datetime.date.today()
        # 睡眠時間を計測
        SLEEP = client.get_sleep(TODAY)["summary"]["totalMinutesAsleep"]
        if __name__ == "__main__":
            print("sleep:{}".format(SLEEP))

        # 心拍数を計測
        data_sec = client.intraday_time_series('activities/heart', TODAY, detail_level='1min')
        HEART_RATE = data_sec["activities-heart-intraday"]["dataset"][-1]["value"]
        if __name__ == "__main__":
            print("heart rate:{}".format(HEART_RATE))


        # 歩数を取得（1分単位）
        dt_now = datetime.datetime.now()
        walk_sec_data = client.intraday_time_series('activities/steps', base_date=TODAY, detail_level="15min", start_time=str(dt_now.hour-1)+":"+str(dt_now.minute), end_time=str(dt_now.hour)+":"+str(dt_now.minute)) ["activities-steps-intraday"]["dataset"]

        STEP = 0
        for batch in walk_sec_data:
            STEP += batch["value"]

        if __name__ == "__main__":
            print("step:{}".format(STEP))

        queryDict = {
            "data" : [
                ["date", "\'" + str(TODAY) + "\'"],
                ["time", "\'" + str(dt_now.hour).zfill(2)+str(dt_now.minute) + "\'"],
                ["checked", "false"],
                ["sleep", str(SLEEP)],
                ["heart", str(HEART_RATE)],
                ["step", str(STEP)]
            ],
            "table" : "fitbit"
        }  
        pprint.pprint(queryDict)
        return queryDict

if __name__ == "__main__":
    fb = fitbitGetter()
    fb._gatherData()