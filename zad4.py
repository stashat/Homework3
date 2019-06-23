from urllib.request import urlopen
import json

def ruta_to_file(ruta):
    SPECIAL_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[',
                     ']', '{', '}', ';', ':', '.', '/', '<', '>', '?', '|',
                     "`", '~', '-', '=', '+', '\\', ' ']
    file_name_l = []
    for char in ruta:
        if char in SPECIAL_CHARS:
            file_name_l.append('_')
        else:
            file_name_l.append(char.lower())
    file_name = ''.join(file_name_l) + '.json'
    return file_name

# potpun - sa return
uri = 'https://api.myjson.com/bins/p08t1'

# nepotpun - bez return
# uri = 'https://api.myjson.com/bins/8ew6d'

with urlopen(uri) as response:
    source = response.read().decode('utf-8')

mydict = json.loads(source)
start_dest = str(input('unijeti pocetnu destinaciju: '))
end_dest   = str(input('unijeti krajnju destinaciju: '))
# start_dest = 'Belgrade'
# end_dest = 'New York City'
ruta = start_dest + "|" + end_dest
file_name = ruta_to_file(ruta)

if ruta == mydict['flight_data']['info']['route']:
    outgoing_len = len(mydict['flight_data']['outgoing'])
    for i in range(0, outgoing_len, 2):
        del mydict['flight_data']['outgoing'][i]['from']['timestamp']
        del mydict['flight_data']['outgoing'][i]['from']['timestamp_utc']
        del mydict['flight_data']['outgoing'][i]['to']['timestamp']
        del mydict['flight_data']['outgoing'][i]['to']['timestamp_utc']
    for i in range(1, outgoing_len, 2):
        del mydict['flight_data']['outgoing'][i]

    try:
        return_len = len(mydict['flight_data']['return'])
        for i in range(0, return_len, 2):
            del mydict['flight_data']['return'][i]['from']['timestamp']
            del mydict['flight_data']['return'][i]['from']['timestamp_utc']
            del mydict['flight_data']['return'][i]['to']['timestamp']
            del mydict['flight_data']['return'][i]['to']['timestamp_utc']
        for i in range(1, return_len, 2):
            del mydict['flight_data']['return'][i]

        passenger_len = len(mydict['passenger_data'])
        for i in range(1, passenger_len):
            del mydict['passenger_data'][i]
        del mydict['passenger_data'][0]['final_date']
        del mydict['passenger_data'][0]['adult_ind']
        del mydict['passenger_data'][0]['_type']
    except KeyError:
        pass

    del mydict['_price_change']
    del mydict['keep_alive']

    # new_json = json.dumps(mydict, indent=2)
    # print(new_json)
else:
    print('nije izabrana postojeca ruta: ', mydict['flight_data']['info']['route'] )

with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(mydict, f, indent=2, ensure_ascii=False)