import random

user_money = 10
casino_money = 10

while user_money and casino_money:

    #сколько у кого денег
    print("у игрока", user_money, "монет")

    input("нажмите ENTER что-бы делать ход")
    #делаем ходы
    user_turn = random.randint(1, 6)
    casino_turn = random.randint(1, 6)
    print("игрок выбросил", user_turn)
    print("казино выбросило", casino_turn)


    #считаем, кто выйграл
    if user_turn > casino_turn:
        print("игрок победил")
        user_money+=1
        casino_money-=1
    elif casino_turn > user_turn:
        print("казино победило")
        casino_money+=1
        user_money-=1
    else:
        print("ничья")

if casino_money == 0:
    print("игрок забрал все деньги")
else:
    print("казино забрал все деньги")


