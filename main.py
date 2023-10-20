from cell import Cell
from copy import deepcopy

t = 0
visited = set()


def dfs(prev, where_prev_looks, A, B):
    global t
    global visited
    where_looks = where_prev_looks
    where_looks_after_dfs = -1
    # Пытаемся пойти налево

    # Поворот на 90 градусов
    next_cell = deepcopy(prev)

    print(2, 0, flush=True)
    result = int(input())
    t += B

    if where_looks == 'd':
        where_looks = 'r'
        next_cell.x = next_cell.x + 1
        next_cell.y = next_cell.y
    elif where_looks == 'u':
        where_looks = 'l'
        next_cell.x = next_cell.x - 1
        next_cell.y = next_cell.y
    elif where_looks == 'r':
        where_looks = 'u'
        next_cell.x = next_cell.x
        next_cell.y = next_cell.y + 1
    elif where_looks == 'l':
        where_looks = 'd'
        next_cell.x = next_cell.x
        next_cell.y = next_cell.y - 1

    # Проверяем, можем ли пойти влево
    print(1, flush=True)
    result = int(input())
    t += A

    if result == 1 and next_cell not in visited:
        visited.add(next_cell)
        dfs(next_cell, visited, next_cell, where_looks, A, B)

    # Пытаемся пойти прямо

    # Поворот на 90 градусов по часовой стрелке
    next_cell = deepcopy(prev)
    where_looks = where_prev_looks

    print(2, 1, flush=True)
    result = int(input())
    t += B

    # where_looks остаётся прежним
    if where_looks == 'd':
        next_cell.x = next_cell.x
        next_cell.y = next_cell.y - 1
    elif where_looks == 'u':
        next_cell.x = next_cell.x
        next_cell.y = next_cell.y+ 1
    elif where_looks == 'r':
        next_cell.x = next_cell.x + 1
        next_cell.y = next_cell.y
    elif where_looks == 'l':
        next_cell.x = next_cell.x - 1
        next_cell.y = next_cell.y

    # Проверяем, можем ли пойти прямо
    print(1, flush=True)
    result = int(input())
    t += A

    if result == 1 and next_cell not in visited:
        visited.add(next_cell)
        dfs(visited, next_cell, where_looks, A, B)

    # Пытаемся пойти направо

    # Поворот на 90 градусов по часовой стрелке
    next_cell = deepcopy(prev)
    where_looks = where_prev_looks

    print(2, 1, flush=True)
    result = int(input())
    t += B

    if where_looks == 'd':
        where_looks = 'l'
        next_cell.x = next_cell.x - 1
        next_cell.y = next_cell.y
    elif where_looks == 'u':
        where_looks = 'r'
        next_cell.x = next_cell.x + 1
        next_cell.y = next_cell.y
    elif where_looks == 'r':
        where_looks = 'd'
        next_cell.x = next_cell.x
        next_cell.y = next_cell.y - 1
    elif where_looks == 'l':
        where_looks = 'u'
        next_cell.x = next_cell.x
        next_cell.y = next_cell.y + 1

    # Проверяем, можем ли пойти направо
    print(1, flush=True)
    result = int(input())
    t += A

    if result == 1 and next_cell not in visited:
        visited.add(next_cell)
        dfs(visited, next_cell, where_looks, A, B)

    # Вернёмся в предка (повернуться ещё на 90, сделать шаг и вернуться на прошлый слой дфс)
    print(2, 1, flush=True)
    result = int(input())
    t += B
    print(1, flush=True)
    result = int(input())
    t += A
    # развернёмся на 180, чтобы смотреть туда же, куда и при входе в dfs
    print(2, 1, flush=True)
    result = int(input())
    t += B
    print(2, 1, flush=True)
    result = int(input())
    t += B


def main():
    x, y, x1, y1, A, B, C, K = map(int, input().split(', '))
    # t = 0
    global t
    global visited

    # Подготовка
    start1 = Cell(x, y)
    start2 = Cell(x1, y1)

    # visited.add(start1)

    # 'd' - down
    # 'u' - up
    # 'r' - right
    # 'l' - left
    where_looks = 'd'

    if x == x1 and y + 1 == y1:
        where_looks = 'u'
    elif x == x1 and y == y1 + 1:
        where_looks = 'd'
    elif x + 1 == x1 and y == y1:
        where_looks = 'r'
    elif x == x1 + 1 and y == y1:
        where_looks = 'l'

    # Шаг 1 - переходим в уже известную клетку и оттуда начинаем обход части графа.
    cur_cell = deepcopy(start2)
    t += A
    visited.add(start2)

    dfs(start2, where_looks, A, B)


    # дважды разворачиваемся, шагаем и запускаем dfs из start1

    print(2, 1, flush=True)
    result = int(input())
    t += B
    print(2, 1, flush=True)
    result = int(input())
    t += B
    print(1, flush=True)
    result = int(input())
    t += A

    if where_looks == 'd':
        where_looks = 'u'
    elif where_looks == 'u':
        where_looks = 'd'
    elif where_looks == 'l':
        where_looks = 'r'
    elif where_looks == 'r':
        where_looks = 'l'
    dfs(start2, where_looks, A, B)

    visited.add(start1)
    print(4, t)


if __name__ == '__main__':
    main()
