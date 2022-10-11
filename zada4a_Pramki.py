from datetime import datetime
import time
count=int(input())
event_x=[]   #(x1, 1, i) (x2,-1, i)  400 000*3 = 1 200 000 цифр
event_y=[]   #(y1, 1, i) (xy,-1, i)
result=[]

for i in range(0,count):
    x1,y1,x2,y2=(list(map(int, input().split())))
    event_x.append((x1, 1, i))
    event_x.append((x2,-1, i))
    event_y.append((y1, 1, i))
    event_y.append((y2,-1, i))
start_time1 = datetime.now()

def search_cross(event):
    event.sort()
    result = []
    starts = []
    ends = []
    coordinate_pos = []
    coordinate_st  = []
    coordinate_end = []
    pos = event[0][0]  # стартовая координата равна координате первого события
    for i in range(len(event)):         # идем по всем событиям
        if event[i][0]!=pos:            # если перешли на следующую координату
            coordinate_pos.append(pos)
            coordinate_st.append(len(starts))  # запомнили где начало этой координаты в началах и концах
            coordinate_end.append(len(ends))
            pos = event[i][0]
        if event[i][1] == 1:            # если начался
            starts.append(event[i][2])  # добавляем номер в стартовые события
        elif event[i][1] == -1:         # если кончился
            ends.append(event[i][2])    # добавляем номер в концевые события
    coordinate_pos.append(pos)
    coordinate_st. append(len(starts))
    coordinate_end.append(len(ends))
    sum = set
    event.sort(key=lambda x: (x[2], x[1])) # сортируем по номеру потом сначала "кончился", потом "начался"
    for i in range(0,len(event),2):         # ищем индекс нужных координат начальная+1 и конечная
        index_cor_end   =(coordinate_pos.index(event[i+1][0]))   # сколько закончилось на начальной прямоугольника
        index_cor_start = coordinate_pos.index(event[i][0]) -1   # сколько началось до конечной прямоугольника
        mass1 = set(starts[:coordinate_st[index_cor_start]])      # сколько началось до конечной прямоугольника
        mass2 = set(ends  [:coordinate_end[index_cor_end]])       # сколько закончилось на начальной прямоугольника
        result.append(mass1.difference(mass2))
    return result

cross_x=search_cross(event_x)
cross_y=search_cross(event_y)
for i in range(len(cross_x)):
    result.append(len (cross_x[i].intersection(cross_y[i]) )-1 )
print('конец прог.  =', datetime.now()-start_time1)
print('res=',result)
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