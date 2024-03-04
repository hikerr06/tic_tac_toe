field = [f"\033[37m\033[40m{i}\033[0m" for i in range(1, 10)]
win1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
win2 = [i for i in win1]
step = {1, 2, 3, 4, 5, 6, 7, 8, 9}
players = list()
player1 = list()
player2 = list()


def win(b, c):
    if b == 0:
        player1.append(players[c])
        d = player1
    else:
        player2.append(players[c])
        d = player2
    for j in win1:
        if set(j) & set(d) == set(j):
            return True


def view_field():
    for j in range(3, 10, 3):
        print(*field[j - 3:j], sep="\033[40m  \033[0m")


def if_repeat(c, b):
    a = int(input())
    step.discard(a)
    if 0 < a < 10:
        if a in c[:b]:
            print("соперник или вы уже походил тут!")
            if_repeat(c, b)
        else:
            players.append(a)
    else:
        print("Введите числа от 1 до 9")
        if_repeat(c, b)


def bot():
    if field[4] == "\033[37m\033[40m5\033[0m":
        players.append(5)
    else:
        for j in win2:
            if len(set(j) & set(player2)) == 2:
                n = list(set(j) - (set(j) & set(player2)))[0]
                if not (n in player1 or n in player2):
                    players.append(n)
                    step.discard(n)
                    del win2[win2.index(j)]
                    break
        else:
            for j in win2:
                if len(set(j) & set(player1)) == 2:
                    n = list(set(j) - (set(j) & set(player1)))[0]
                    if not (n in player1 or n in player2):
                        players.append(n)
                        step.discard(n)
                        del win2[win2.index(j)]
                        break
            else:
                players.append(step.pop())


view_field()
for i in range(0, 9):
    num = i % 2 + 1
    print(f"Ход игрока {num}")
    if i % 2 == 0:
        if_repeat(players, i)
        field[players[-1] - 1] = "\033[31m\033[40m\033[1mX\033[0m"
    else:
        bot()
        field[players[-1] - 1] = "\033[32m\033[40m\033[1mO\033[0m"
    view_field()
    if win(i % 2, i):
        print(f"Игрок {num} победил!")
        break
else:
    print("Ничья!")
