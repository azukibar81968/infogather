import requests
import time
import datetime
import json
import pprint
import InfoGetterIF
import Weather

if __name__ == "__main__":
    getterList = [
        Weather.weatherGetter()
    ]

    while True:
        for getter in getterList:
            getter.GatherAndUpload()

        # 適当に待つ
        time.sleep(3600*23)
