#url is https://api.data.gov.sg/v1/environment/2-hour-weather-forecast
#viewer is http://jsonviewer.stack.hu/


import json
import requests

url = "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast"
req=requests.get(url)

data = json.loads(req.text)

name = data['items'][0]['forecasts'][2]["area"]
fc = data['items'][0]['forecasts'][2]["forecast"]
print ("name : %s, forecast : %s" % (name, fc))


for i in range(0, 47):
    name = data['items'][0]['forecasts'][i]["area"]
    fc = data['items'][0]['forecasts'][i]["forecast"]
    print ("name : %s, forecast : %s" % (name, fc))



#------------------------------------------------


url = "https://wttr.in/Singapore?format=j1"
req=requests.get(url)

data = json.loads(req.text)


data = data['current_condition'][0]['weatherDesc'][0]["value"]
print (data)
