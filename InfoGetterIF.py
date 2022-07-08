import requests
import time
import datetime
import json
import pprint

class InfoGetterIF:
    def _gatherData(self):
        return

    def _upload(self, queryDict):

        headers = {'content-type': 'application/json'}

        try:
            postres = requests.post("http://10.0.1.94:5000/insert/", data=json.dumps(queryDict), headers=headers)
            pprint.pprint(queryDict)
            pprint.pprint(postres.text)

            return True
        except Exception as e:
            print( "error:" + str(e))
            return False



    def GatherAndUpload(self):
        queryDict = self._gatherData()
        self._upload(queryDict)
        return