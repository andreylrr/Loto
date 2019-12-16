import unittest
import game as gm
import random as rd

"""
    Программа реализует игру Лото
"""

print("Добро пожаловать в игру лотерея!!!!")
print("\n")

# Запрашиваем у пользователя количество игроков
while True:
    s_n_players = input('Введите число участников игры:')
    if s_n_players.isdigit():
        i_n_plaers = int(s_n_players)
        break
    print("Число участников игры указано не верно.")

# Запрашиваем у пользователя имена игроков
l_name_players = []
l_type_players = []
for i in range(1,i_n_plaers+1):
    l_name_players.append(input(f'Введите имя участника под номером {i}:'))
    while True:
        s_type = input("Введите тип игрока 1 - компютер, 2 - человек:")
        if s_type == "1":
            l_type_players.append("Computer")
            break
        elif s_type == "2":
            l_type_players.append("Human")
            break
        else:
            print("Неверно указан тип игрока!!")

# Запрашиваем у пользователя количество карт у каждого игрока
while True:
    s_n_cards = input("Введите количество карт у каждого участника:")
    if s_n_cards.isdigit():
        i_n_cards = int(s_n_cards)
        break
    print("Количество карт указано неверно.")

# Создаем экземпляр класса игры в Лото
c_loto_game = gm.Game()

# Начиаем игру и продолжаем до тех пор, пока пользователь не откражется
while True:
    c_loto_game.start_game(i_n_plaers, i_n_cards, l_name_players, l_type_players)
    s_continue = input("Хотите сыграть еще раз (y/n)?")
    if s_continue == "n":
        break

