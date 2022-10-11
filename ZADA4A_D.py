plan = []
Arr_shift = [(0,-1,'U'), (0,1,'D'), (1,0,'R'), (-1,0,'L')]  # массив сдвигов
N, M = list(map(int, input().split()))

for i in range(N):
    STRING = list(input())  # считываем строки
    plan.append(STRING)

def hod(plan, x, y, Arr_shift):  # ищем стартовые точки, из которых только 1 путь
    if plan[y][x] == '.':  # если точка равна . то работаем
        count = 0
        for i in range(4):  # проверяем стороны ищем путь
            dx = Arr_shift[i][0]
            dy = Arr_shift[i][1]
            ds = Arr_shift[i][2]
            # находим точки куда можно идти, '.' или 'S'
            if plan[y + dy][x + dx] == '.' or plan[y + dy][x + dx] == 'S':
                simbol = ds                      # запоминаем букву направления
                next_x = x + dx                  # запоминаем x свободного следующего хода
                next_y = y + dy                  # запоминаем y свободного следующего хода
                count += 1                      # считаем количество свободных путей
        if count == 1:                           # если путь 1 то:
            plan[y][x] = simbol                  # пишем в точку направление согласно схеме
            hod(plan, next_x, next_y,Arr_shift)  # запускаем себя же но со следующей точки

for i in range(len(plan)):
    for j in range(len(plan[i])):
        hod(plan, j, i, Arr_shift)

for i in range(len(plan)):  # печатаем ответ
    print("".join(plan[i]))
