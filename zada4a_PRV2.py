from datetime import datetime
import time

count=int(input())
event_x=[]
event_y=[]
result=[]

for i in range(0,count):
    x1,y1,x2,y2=(list(map(int, input().split())))   #
    event_x.append((x1, 1, i))
    event_x.append((x2,-1, i))
    event_y.append((y1, 1, i))
    event_y.append((y2,-1, i))
start_time1 = datetime.now()

def search_cross(event):
    event.sort()
    result=[1000] * len(base)
    pos=event[0][0]
    temp_sets = set()
    sets_cor = []

    for i in range(len(event)):         # идем по всем событиям
        if event[i][0]!=pos:            # если перешли на следующую координату ?и прошли все закончивающиеся события?
            sets_cor.append((pos,temp_sets))
            pos = event[i][0]
        if event[i][1] ==  1:                # если начался
            temp_sets.add(event[i][2])       # добавляем номер начавшегося
        elif event[i][1] == -1:              # если кончился
            temp_sets.remove(event[i][2])    # удаляем   номер закончившегося
    sets_cor.append((pos, temp_sets))
    sum=set()
    event.sort(key=lambda x: (x[2], x[1]))  # сортируем по номеру потом сначала "кончился", потом "начался"

    for i in range (0,len(event),2):
    # для каждого прямоугольника: какие прямоугольники начались до его последней координаты не включая
    # минус все прямоугольники которые закончились до его начальной координаты включая ее



    return result

cross_x=search_cross(event_x,base_x)
cross_y=search_cross(event_y,base_y)

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