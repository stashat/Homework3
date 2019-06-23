lista = [
    {
      'country': "GB",
      'spent': 100
    },
    {
      'country': "RU",
      'spent': 200
    }
]

my_dict = {}
for i in lista:
    my_dict[i['country']] = i['spent']
    # my_dict.update({i['country']:i['spent']})
print(my_dict)
    