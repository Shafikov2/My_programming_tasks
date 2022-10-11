import json
import datetime as dt
fil = {}
string = input()
templates = json.loads(string)
for i in range(5):
    a,b=input().split()
    fil[a]=b

def my_filter(d):                        # функция сортировки
    data = dt.datetime.strptime(d['date'], '%d.%m.%Y')
    data_before = dt.datetime.strptime(fil['DATE_BEFORE'], '%d.%m.%Y')
    data_after = dt.datetime.strptime(fil['DATE_AFTER'], '%d.%m.%Y')
    if (fil['NAME_CONTAINS']).lower() in (d['name']).lower() \
        and int(d['price']) >= int(fil['PRICE_GREATER_THAN']) and int(d['price']) <= int(fil['PRICE_LESS_THAN'])  \
        and data <= data_before and data >= data_after:
        return True
    else:
        return False

otvet=list(filter(my_filter, templates)) # фильтруем
otvet.sort(key=lambda x: int(x['id']))   # сортируем по Id
otvet=json.dumps(otvet)                  # переводим в JSON
print(otvet)
# ответ правильный [{"name": "EaRPoDs", "id": 2, "date": "01.01.2022", "price": 2200}, {"date": "23.09.2021", "name": "Airpods", "id": 5, "price": 2300}]