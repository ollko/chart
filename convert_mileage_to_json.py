import json


from pyexcel_ods import get_data


test_data = get_data("test_LT.ods")
mileage_sheet = test_data['Пробег']

filials = [
    'Амурский','Восточно-Сибирский','Дальневосточный','Западно-Сибирский','Западный','Московский','Северный','Северо-Западный','Северо-Кавказский','Южный'
]

lokos = [
    'ВЛ65ви','ТЭ10ви','ВЛ85ви','2ЭС5Кви','3ЭС5Кви','ЭП1ви','ВЛ60ви','ВЛ80ви','М62ви','ТЭП70ви','ЧС4ви','ТЭ25ви','ЧС2ви','ЭП2Кви','ЧС7ви','ЧС8ви','ВЛ10ви','ТЭ116ви','ЭС4Кви','ВЛ15ви','ЧС200ви','ЧС6ви','ТЭ70ви'
]

def get_pk(item_list, item):
    return item_list.index(item)+1


x = []
for j in range(2, len(mileage_sheet[0])):
    for row in mileage_sheet:
        if row != [] and row[0] != 'Филиал':
            i = {
                'filial': get_pk(filials, row[0]),
                'loko': get_pk(lokos, row[1]),
                'mileage': row[j],
                'year': mileage_sheet[0][j],
            }
            x.append(i)


data = [
    {
    "model": "page.mileage",
    "pk": x.index(item) + 1,
    'fields': item 
    } for item in x
]
print(len(x))
print(data[55])
print(len(data))


j = json.dumps(data)

with open('mileage.json', 'w') as f:
    f.write(j)


