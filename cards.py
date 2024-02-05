from itertools import product
import random


def welcome():
    print("=====================================")
    print("               WELCOME               ")
    print("                 TO                  ")
    print("                KEMPS                ")
    print("=====================================")


def menu():
    commands = ["Draw", "Pass/Computer turn", "Next turn", "Quit the game"]
    print("What You Want To Do?")
    for index, el in enumerate(commands, start=1):
        print(f"{index} - {el}")


def command_menu():
    print("Choose A Card From The Playing Field To Take.")
    choice1 = int(input("Enter your choice:"))
    print("Select A Card To Replace It With.")
    choice2 = int(input("Enter your choice:"))
    return choice1 - 1, choice2 - 1


def template_card_front(value, color):
    if value != "10":
        card_module = [('┌───────────┐'), (f'│ {value}{color}        │'), ('│           │'), (f'│     {color}     │'),
                       ('│           │'), (f'│        {color}{value} │'), ('└───────────┘')]
    else:
        card_module = [('┌───────────┐'), (f'│ {value}{color}       │'), ('│           │'), (f'│     {color}     │'),
                       ('│           │'), (f'│       {color}{value} │'), ('└───────────┘')

                       ]
    return card_module


def template_card_back():
    back = [('┌───────────┐'), ('│@@@@@@@@@@@│'), ('│@@@@@@@@@@@│'), ('│@@@@@@@@@@@│'), ('│@@@@@@@@@@@│'),
            ('│@@@@@@@@@@@│'), ('└───────────┘')]
    return back


def draw_cards_for_players():
    to_player = []
    to_computer = []
    for index in range(4):
        to_player.append(random.choice(deck))
        deck.remove(to_player[index])
        to_computer.append(random.choice(deck))
        deck.remove(to_computer[index])

    return to_player, to_computer


def first_view(p1, c1):
    player1 = [[], [], [], [], [], [], []]
    for index, card in enumerate(player):
        value, color = card[0], card[1]
        el = template_card_front(value, color)
        for i in range(len(el)):
            player1[i].append(el[i])
    cards_to_player = []
    for index in range(len(player1)):
        cards_to_player.append(" ".join(player1[index]))

    cards_computer = [[], [], [], [], [], [], []]
    back = list(template_card_back())
    for index in range(4):
        for i in range(len(back)):
            cards_computer[i].append(back[i])
    back_card_computer = []
    for index in range(len(cards_computer)):
        back_card_computer.append(" ".join(cards_computer[index]))

    return "\n".join(cards_to_player), "\n".join(back_card_computer)


def gameplay_area_cards():
    area = []
    for index in range(4):
        area.append(random.choice(deck))
        deck.remove(area[index])
    gameplay_area = [[], [], [], [], [], [], []]
    for index, card in enumerate(area):
        value, color = card[0], card[1]
        el = template_card_front(value, color)
        for i in range(len(el)):
            gameplay_area[i].append(el[i])
    area_cards = []
    for index in range(len(gameplay_area)):
        area_cards.append(" ".join(gameplay_area[index]))
    return "\n".join(area_cards), area


def area_view(area):
    gameplay_area = [[], [], [], [], [], [], []]
    for index, card in enumerate(area):
        value, color = card[0], card[1]
        el = template_card_front(value, color)
        for i in range(len(el)):
            gameplay_area[i].append(el[i])
    area_cards = []
    for index in range(len(gameplay_area)):
        area_cards.append(" ".join(gameplay_area[index]))
    return "\n".join(area_cards)


def board(p1, c1, a):
    a = area_view(a)
    player_cards, computer_cards = first_view(p1, c1)
    print("Computer Cards:")
    print(computer_cards)

    print("Gameplay Area Whit Cards:")
    print(a)

    print("Your Cards:")
    print(player_cards)


Suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
Ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = list(product(Ranks, Suits))

welcome()
print("-To Start The Game Please press: 0")
start = input("Enter:")
while True:
    if start == "0":
        break
    else:
        print("Invalid choice!Press 0 to start")
        start = input("Enter:")

player, computer = draw_cards_for_players()
area_card, area = gameplay_area_cards()
first_view(player, computer)
board(player, computer, area)
while True:
    menu()
    choice = input("Enter your choice:")
    if choice == "1":
        card_take_from_area, card_switch = command_menu()
        take_card = area.pop(card_take_from_area)
        switch = player.pop(card_switch)
        player.append(take_card)
        area.append(switch)
        player.sort()
        board(player, computer, area)
    elif choice == "2":
        flag = True
        while True:
            values_computer = [x[0] for x in computer]
            take_card = 0
            switch = 0
            computer.sort()
            max_count_card = computer[2][0]
            count = values_computer.count(max_count_card)
            for i, el in enumerate(area):
                if count == 3 and el[0] == max_count_card:
                    take_card = area.pop(i)
                    break
                if el[0] in values_computer and count < 3:
                    take_card = area.pop(i)
                    break
            else:
                flag = False

            if not flag:
                break

            for i, el in enumerate(computer):
                if el[0] != take_card[0]:
                    switch = computer.pop(i)
                    break
            computer.append(take_card)
            area.append(switch)
        board(player, computer, area)

    elif choice == "3":
        if len(deck) < 4:
            print("\nDRAW!")
            break
        area_card, area = gameplay_area_cards()
        board(player, computer, area)
        continue
    elif choice == "4":
        print("\nSee you again cowardly chicken!")
        exit()
    else:
        print("Invalid choice!")
    player1 = [x[0] for x in player]
    computer1 = [x[0] for x in computer]
    if len(set(player1)) == 1:
        print()
        print("CONGRATULATION! \nYOU WON THE GAME!")
        break
    if len(set(computer1)) == 1:
        print()
        print("SORRY,YOU LOSE THE GAME")
        c = [[], [], [], [], [], [], []]
        for index, card in enumerate(computer):
            value, color = card[0], card[1]
            el = template_card_front(value, color)
            for i in range(len(el)):
                c[i].append(el[i])
        c1 = []
        for index in range(len(c)):
            c1.append(" ".join(c[index]))
        print("\n".join(c1))
        break

