list_discipline = {}
list_players = []
res = []
temp = ''

n = int(input())
for i in range(n):
    name, max_people = list(input().split(','))
    list_discipline[name] = int(max_people)

k = int(input())
for i in range(k):
    name_player, name_discipline, count, penalty = list(input().split(','))
    list_players.append((name_discipline, int(count) * (-1), penalty, name_player))

list_players.sort()  # list_players.sort(key=lambda x: (x[0],x[2],x[0]))

for i in range(len(list_players)):  # идем по игрокам
    if temp != list_players[i][0]:
        temp = list_players[i][0]
        count = list_discipline[list_players[i][0]]
        res.append(list_players[i][3])
        count -= 1
    elif count > 0:
        res.append(list_players[i][3])
        count -= 1
    '''
    если текущая специальность отличается от темп 
    то находим сколько игроков нужно взять из новой специальности
    темп присвоить текущую специальность
    счетчик равен макс игроков для этой специальности
    добавляем игрока
    счетчик-=1
    '''
res.sort()
print(res)