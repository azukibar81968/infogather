import requests
import time
import datetime
import json
import pprint
import InfoGetterIF
import Weather
import Fitbit

if __name__ == "__main__":
    getterList = [
#        Weather.weatherGetter(),
        Fitbit.fitbitGetter()
    ]

    while True:
        for getter in getterList:
            getter.GatherAndUpload()

        # 適当に待つ
        time.sleep(60)
