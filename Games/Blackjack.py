import random

def deal_card():
    return random.randint(1, 11)

def blackjack_game():
    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]

    print("Добро пожаловать в игру Блэкджек!")
    print("Ваши карты:", player_hand)
    print("Карта компьютера:", computer_hand[0])

    while sum(player_hand) < 21:
        choice = input("Хотите взять ещё карту? (да/нет): ").lower()
        if choice == "да":
            player_hand.append(deal_card())
            print("Ваши карты:", player_hand)
        else:
            break

    while sum(computer_hand) < 17:
        computer_hand.append(deal_card())

    print("Ваши карты:", player_hand)
    print("Карты компьютера:", computer_hand)

    if sum(player_hand) > 21:
        print("Вы проиграли! У вас перебор.")
    elif sum(computer_hand) > 21:
        print("Вы выиграли! У компьютера перебор.")
    elif sum(player_hand) > sum(computer_hand):
        print("Вы выиграли! Ваша сумма больше.")
    elif sum(player_hand) < sum(computer_hand):
        print("Вы проиграли! Сумма компьютера больше.")
    else:
        print("Ничья!")

if __name__ == "__main__":
    blackjack_game()