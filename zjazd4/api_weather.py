import json
import urllib.request
import datetime

miasto = input("podaj nazwę miasta: ")
data1=f'''{datetime.datetime.today().year}/{datetime.datetime.today().month}/{datetime.datetime.today().day}'''

with urllib.request.urlopen(f'''https://www.metaweather.com/api/location/search/?query={miasto}''') as link:
    szuk = json.loads(link.read())
    idmiasta = szuk[0]['woeid']

with urllib.request.urlopen(f'''https://www.metaweather.com/api/location/{idmiasta}/{data1}''') as link:
    szuk = json.loads(link.read())
    i=0
    for i,s in enumerate(szuk[0], start=1):
        if i>1:
            try:
                print(s, round(szuk[0][s]*1,2))
            except:
                print(s, szuk[0][s])
input()
