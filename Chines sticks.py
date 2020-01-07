"""Предлагаю древнюю китайскую игру в палочки.

Играют два игрока.  Есть 10 палочек. Игроки по очереди берут от одной
до трёх палочек. Играют до тех пор пока не закончатся палочки.
Тот кто взял последним - тот проиграл.

Реализуйте игру таким образом, чтобы могли играть два человека.
Изначально есть 10 палочек. На каждом ходу выводите на консоль текущее
количество оставшихся палочек и просите ввести количество палочек,
которое хочет взять игрок (который делает ход). Не забывайте менять
очерёдность игроков и сокращать кол-во палочек. В конце надо вывести
кто победил - первый или второй игрок.

Нюансы реализации могут отличаться. Кто-то может захотет запросить
имена у игроков. Кто-то может захотеть реализовать не с 10-ю палочками,
а с тем количеством, которое введёт пользователь (может он хочет играть с
20-ю палочками?)."""

print('Welcome. This is a game "Chines sticks".')
print('This game is for two players.')
sticks_amount = int(input('Please, enter amount of sticks,' +\
                          'that you want play with: '))

print('First move: Player 1')
player_turn = 1

while True:
    if player_turn == 1:
        print('Player 1 - your move.')
        sticks = int(input('How much sticks you want to remove?' +\
                           'Be aware, that amount of sticks shold be' +\
                           'less then {}. '.format(sticks_amount)))
        sticks_amount -= sticks
        if sticks_amount == 0:
            print('You lost.')
            break
        else:
            player_turn = 2
    else:
        print('Player 2 - your move.')
        sticks = int(input('How much sticks you want to remove?' +\
                           'Be aware, that amount of sticks shold be' +\
                           'less then {}. '.format(sticks_amount)))
        sticks_amount -= sticks
        if sticks_amount == 0:
            print('You lost.')
            break
        else:
            player_turn = 1
    
    

