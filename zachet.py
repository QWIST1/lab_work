# Карта и ее вывод карты
map = [" " for i in range(9)]
def print_map():
    row1 = "| {} | {} | {} |".format(map[0], map[1], map[2])
    row2 = "| {} | {} | {} |".format(map[3], map[4], map[5])
    row3 = "| {} | {} | {} |".format(map[6], map[7], map[8])
    b = "-" * 13
    print(f"{b}\n{row1}\n{b}\n{row2}\n{b}\n{row3}\n{b}")


# Комбибинации побед
victory = [[0,1,2],
           [3,4,5],
           [6,7,8],
           [0,3,6],
           [1,4,7],
           [2,5,8],
           [0,4,8],
           [2,4,6]]


# Ход первого игрока
def player_move1(map):
    while True:
        player_choice1 = input(f'Ходит {player_name1}:')
        try:
            int(player_choice1)
            if int(player_choice1) in range(1, 10):
                if map[int(player_choice1) - 1] == " ":
                    map[int(player_choice1) - 1] = "X"
                    break
                else:
                    print("Сюда уже ходили!")
                    print_map()
            else:
                print("Неправельный ход!")
                print_map()
        except ValueError:
            pass
            print("Введите число 1-9")
            print_map()


# Ход второго игрока
def player_move2(map):
    while True:
        player_choice2 = input(f'Ходит {player_name2}:')
        try:
            int(player_choice2)
            if int(player_choice2) in range(1, 10):
                if map[int(player_choice2) - 1] == " ":
                    map[int(player_choice2) - 1] = "O"
                    break
                else:
                    print("Сюда уже ходили!")
                    print_map()
            else:
                print("Неправельный ход!")
                print_map()
        except ValueError:
            pass
            print("Введите число 1-9")
            print_map()


# Вывод текущего результата
def result():
    win = ""
    for i in victory:
        if map[i[0]] == map[i[1]] == map[i[2]] == "X":
            win = player_name1
        elif map[i[0]] == map[i[1]] == map[i[2]] == "O":
            win = player_name2
        elif " " not in map:
            win = "Ничья!"
    return win


# Основание игрового процесса
End_game = False
player_name1 = str(input("Введи имя превый игрок:"))
player_name2 = str(input("Введи Имя второй игрок:"))
while True: # Опрос куда пойдет игрок
    print_map()
    player_move1(map)
    win = result()
    if win != "":
        End_game = True
        break
    else:
        End_game = False
    print_map()
    player_move2(map)
    win = result()
    if win != "":
        End_game = True
        break
    else:
        End_game = False


print_map()
print("Победил(а)", win)
