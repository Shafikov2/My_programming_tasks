from datetime import datetime
import time

count = int(input())
event_x = []
event_y = []
result = []
base_x = []
base_y = []
for i in range(0,count):
    x1, y1, x2, y2 = (list(map(int, input().split())))   #
    event_x.append((x1,  1, i))
    event_x.append((x2, -1, i))
    event_y.append((y1,  1, i))
    event_y.append((y2, -1, i))
    base_x.append((x1, x2))
    base_y.append((y1, y2))
start_time1 = datetime.now()


def search_cross(event,base):
    event.sort()
    result = [1000] * len(base)     # массив результата
    starts = []      # массив очередности начала прямоугольников
    ends = []        # массив очередности конца прямоугольников
    coordinate = []
    temp_starts = set()
    temp_ends = set()
    pos = event[0][0]  # стартовая координата равна координате первого события

    for i in range(len(event)):         # идем по всем событиям
        if event[i][0] != pos:            # если перешли на следующую координату ?и прошли все закончивающиеся события?
            coordinate.append(pos)
            starts.append(temp_starts)
            ends.append(temp_ends)
            temp_starts = set()
            temp_ends = set()
            pos = event[i][0]
        if event[i][1] == 1:                # если начался
            temp_starts.add(event[i][2])     # добавляем номер начавшегося
        elif event[i][1] == -1:              # если кончился
            temp_ends.add(event[i][2])       # добавляем номер закончившегося
    coordinate.append(pos)
    starts.append(temp_starts)
    ends.append(temp_ends)

    sum = set()

    for i in range(len(base)):
        # для каждого прямоугольника: какие прямоугольники начались до его последней координаты не включая
        # минус все прямоугольники которые закончились до его начальной координаты включая ее
        index_cor_end = coordinate.index(base[i][1])
        index_cor_start = coordinate.index(base[i][0])+1
        mass1 = starts[:index_cor_end]
        mass2 = ends[:index_cor_start]
        mass11 = set()
        mass22 = set()
        for k1 in mass1:
            mass11=mass11.union(k1)
        for k2 in mass2:
            mass22 = mass22.union(k2)
        sum = mass11 - mass22
        result[i] = sum
    return result


cross_x = search_cross(event_x, base_x)
cross_y = search_cross(event_y, base_y)

for i in range(len(cross_x)):
    result.append(len(cross_x[i].intersection(cross_y[i])) - 1)
print('res=', result)

print('конец программы=', datetime.now()-start_time1)
'''
6
-2 -4 2 2
-2 -4 0 -1
-2 -1 0 2
0 -4 2 -1
0 -1 2 2
-1 -2 1 0
#Ответ: 5 2 2 2 2 5 
'''