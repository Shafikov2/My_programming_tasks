from datetime import datetime
import time
count=int(input())
event_x=[]   #(x1, 1, i) (x2,-1, i)  400 000*3 = 1 200 000 цифр
event_y=[]   #(y1, 1, i) (xy,-1, i)
result=[20000]*count

for i in range(0,count):
    x1,y1,x2,y2=(list(map(int, input().split())))
    event_x.append((x1, 1, i))
    event_x.append((x2,-1, i))
    event_y.append((y1, 1, i))
    event_y.append((y2,-1, i))
start_time1 = datetime.now()

def search_cross(event1,event2):
    event1.sort()
    starts1 = []
    ends1 = []
    coordinate_pos1 = []
    coordinate_st1  = []
    coordinate_end1 = []
    pos1 = event1[0][0]  # стартовая координата равна координате первого события

    event2.sort()
    starts2 = []
    ends2 = []
    coordinate_pos2 = []
    coordinate_st2 = []
    coordinate_end2 = []
    pos2 = event2[0][0]  # стартовая координата равна координате первого события

    for i in range(len(event1)):          # идем по всем событиям
        if event1[i][0]!=pos1:            # если перешли на следующую координату
            coordinate_pos1.append(pos1)
            coordinate_st1.append(len(starts1))  # запомнили где начало этой координаты в началах и концах
            coordinate_end1.append(len(ends1))
            pos1 = event1[i][0]
        if event1[i][1] == 1:             # если начался
            starts1.append(event1[i][2])  # добавляем номер в стартовые события
        elif event1[i][1] == -1:          # если кончился
            ends1.append(event1[i][2])    # добавляем номер в концевые события
    coordinate_pos1.append(pos1)
    coordinate_st1. append(len(starts1))
    coordinate_end1.append(len(ends1))

    for i in range(len(event2)):          # идем по всем событиям
        if event2[i][0]!=pos2:            # если перешли на следующую координату
            coordinate_pos2.append(pos2)
            coordinate_st2.append(len(starts2))  # запомнили где начало этой координаты в началах и концах
            coordinate_end2.append(len(ends2))
            pos2 = event2[i][0]
        if event2[i][1] == 1:             # если начался
            starts2.append(event2[i][2])  # добавляем номер в стартовые события
        elif event2[i][1] == -1:          # если кончился
            ends2.append(event2[i][2])    # добавляем номер в концевые события
    coordinate_pos2.append(pos2)
    coordinate_st2. append(len(starts2))
    coordinate_end2.append(len(ends2))

    event1.sort(key=lambda x: (x[2], x[1]))  # сортируем по номеру потом сначала "кончился", потом "начался"
    event2.sort(key=lambda x: (x[2], x[1]))  # сортируем по номеру потом сначала "кончился", потом "начался"

    for i in range(0,len(event1),2):                                # ищем индекс нужных координат начальная+1 и конечная
        index_cor_end1   = coordinate_pos1.index(event1[i+1][0])    # сколько закончилось на начальной прямоугольника
        index_cor_start1 = coordinate_pos1.index(event1[i][0])-1    # сколько началось до конечной прямоугольника

        mass11 = set(starts1[:coordinate_st1[index_cor_start1]])    # сколько началось до конечной прямоугольника
        mass21 = set(ends1  [:coordinate_end1[index_cor_end1]])     # сколько закончилось на начальной прямоугольника
        result1 = mass11.difference(mass21)

        index_cor_end2   = coordinate_pos2.index(event2[i + 1][0])  # сколько закончилось на начальной прямоугольника
        index_cor_start2 = coordinate_pos2.index(event2[i][0]) - 1  # сколько началось до конечной прямоугольника

        mass11 = set(starts2[:coordinate_st2[index_cor_start2]])    # сколько началось до конечной прямоугольника
        mass21 = set(ends2[:coordinate_end2[index_cor_end2]])       # сколько закончилось на начальной прямоугольника
        result2=mass11.difference(mass21)

        result[(i//2)]=len(result1.intersection(result2)) - 1
        #print('цикл i  =',i//2,' ', datetime.now() - start_time1)
    print('res=', result)

search_cross(event_x,event_y)
print('конец прог.  =', datetime.now()-start_time1)
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