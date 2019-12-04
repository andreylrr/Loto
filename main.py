import game as gm

print("Добро пожаловать в игру лотерея!!!!")
print("\n")

while True:
    s_n_players = input('Введите число участников игры с учетом игрока "компютер":')
    if s_n_players.isdigit():
        i_n_plaers = int(s_n_players)
        break
    print("Число участников игры указано не верно.")

l_name_players = []
for i in range(1,i_n_plaers):
    l_name_players.append(input(f'Введите имя участника под номером {i}:'))

while True:
    s_n_cards = input("Введите количество карт у каждого участника:")
    if s_n_cards.isdigit():
        i_n_cards = int(s_n_cards)
        break
    print("Количество карт указано неверно.")

c_loto_game = gm.Game()

while True:
    c_loto_game.start_game(i_n_plaers, i_n_cards, l_name_players)
    s_continue = input("Хотите сыграть еще раз (y/n)?")
    if s_continue == "n":
        break

