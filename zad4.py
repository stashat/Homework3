import json
from urllib.request import urlopen

with urlopen("https://api.myjson.com/bins/19f6d9") as response:
    data = response.read().decode('utf-8')

data = json.loads(data)

lista_1 = ['timestamp', 'timestamp_utc']
indeksi = [0,2]
for br in indeksi:
    for i in lista_1:
        del data['flight_data']['outgoing'][br]['from'][i]
        del data['flight_data']['outgoing'][br]['to'][i]
        del data['flight_data']['return'][br]['from'][i]
        del data['flight_data']['return'][br]['to'][i]
del data['flight_data']['outgoing'][1]
del data['flight_data']['return'][1]

lista_2 = ['final_date', 'adult_ind', '_type']
for i in lista_2:
    del data['passenger_data'][0][i]

lista_3 = ['_price_change', 'keep_alive']
for i in lista_3:
    del data[i]

new_json = json.dumps(data, indent=2)
print(new_json)