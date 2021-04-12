import sys
import time

monsters = {'1': 'Archer', '2': 'Ninja', '3': 'Tank', '4': 'BladeMasteR'}
characters = {'1': 'Khaled', '2': 'Hamza', '3': 'Cnblack', '4': 'Murad', '5': 'Waled', '6': 'Lieth'}
Helath = 100
charater_value = ''
Attack = 0
value3 = ''
chraeterskey = ''
attackvalue = 0


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep( 0.1/10)


slowprint('welcome Stranger This is a stupid Game to waste your time Your Attack Depends on the character you select')


def display():
    global charater_value
    i = True
    while i:
        name = str(input('Please Enter Your name :'))

        if name.strip().isdigit():
            print('Please Enter A valid name\t')
        else:
            i = False
    for key in characters:
        print(key, ' ', characters[key])
    i = True
    while i:
        try:
            chosing = int(input('Choose Your Character:\t '))
            if chosing > 6 or chosing == 0:
                print('The Character is not in the list try again\t')

            value = str(chosing)
            charater_value = characters[value]
            print('YOU Choosed ', chosing, 'Which is', charater_value)
        except ValueError:
            print('Please Enter A valid Number\t')
        else:
            i = False
    return charater_value


display()


def charecter():
    global value3
    for key in monsters:
        print(key, ' ', monsters[key])


    if value3 == '1':
        print("you chose The", monsters[value3])
        archer ( charater_value )
    elif value3 == '2':
        print("you chose The", monsters[value3])
    elif value3 == '3':
        print("you chose The", monsters[value3])
    elif value3 == '4':
        print("you chose The", monsters[value3])

    while True:
        value3 = str(input("Chose the monster that you want to fight"))
        if value3 not in monsters.keys():
            print('not found')


        else:
            break

    # print('You Will Attack the ', monsters[value3])
    return value3


charecter()


def archer(value):
    global attack_value
    archer_hp = 100

    print("press 1 to start the Fight")
    attack = int(input())
    while attack != 1:
        print ( 'Attack Value must me 1 ')
        attack_value = int(input("\t"))
        if attack_value == 1:
            break
    while True:
        attack_value = int(input("1.Attack\t"))
        if value == 'Murad':
            attack = 20
            archer_hp = archer_hp - attack
            print(monsters[value3], 'HP:', archer_hp)

        elif value == 'Lieth':
            attack = 20
            archer_hp = archer_hp - attack
            print(monsters[value3], 'HP:', archer_hp)
        elif value == 'Waled':
            attack = 20
            archer_hp = archer_hp - attack
            print(monsters[value3], 'HP:', archer_hp)

        elif value == 'Hamza':
            attack = 20
            archer_hp = archer_hp - attack
            print(monsters[value3], ' HP:', archer_hp)

        elif value == 'Cnblack':
            attack = 25
            archer_hp = archer_hp - attack
            print(monsters[value3], ' HP:', archer_hp)
        elif value == 'Khaled':
            print('You are a peaceful guy you cant play the game')
            break
        if archer_hp <= 0:
            break
    charecter()




def Ninja(value):

    ninja_hp = 200
    while ninja_hp <= 200:
        attack_value = int(input("1.Attack\t"))

        if value == 'Murad':
            attack = 20
            ninja_hp = ninja_hp - attack
            print ( monsters[value3], 'HP:', ninja_hp)

        elif value == 'Lieth':
            attack = 20
            ninja_hp = ninja_hp - attack
            print ( monsters[value3], 'HPs:', ninja_hp)
        elif value == 'Waled':
            attack = 20
            ninja_hp = ninja_hp - attack
            print(monsters[value3], 'HP:', ninja_hp)

        elif value == 'Hamza':
            attack = 20
            ninja_hp = ninja_hp - attack
            print(monsters[value3], ' HP:', ninja_hp)

        elif value == 'Cnblack':
            attack = 25
            ninja_hp = ninja_hp - attack
            print(monsters[value3], ' HP:', ninja_hp)
        elif value == 'Khaled':
            print('You are a peaceful guy you cant play the game')
            break
        if ninja_hp <= 0:
            break
    charecter()

Ninja(charater_value)
archer(charater_value)
