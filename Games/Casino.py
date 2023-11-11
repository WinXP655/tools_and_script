import random
import time

def get_bet(player_balance):
    while True:
        try:
            bet = int(input(f"Введите ставку (ваш баланс: {player_balance}): "))
            if bet < 0:
                print("Ставка не может быть отрицательной.")
            elif bet > player_balance:
                print("У вас недостаточно средств.")
            else:
                return bet
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

def casino_game():
    player_balance = 1000
    print("Добро пожаловать в казино!")

    while player_balance > 0:
        print()
        bet = get_bet(player_balance)

        if bet == 0:
            print("Спасибо за игру! Ваш баланс:", player_balance)
            break

        player_number = random.randint(1, 6)
        computer_number = random.randint(1, 6)

        print("Идет сравнение...")
        time.sleep(1)

        print(f"Ваше число: {player_number}")
        print(f"Число компьютера: {computer_number}")

        if player_number > computer_number:
            print("Вы выиграли!")
            player_balance += bet
        elif player_number < computer_number:
            print("Вы проиграли.")
            player_balance -= bet
        else:
            print("Ничья! Ставка возвращена.")

        print("Обновление баланса...")
        time.sleep(1)
        print(f"Ваш баланс: {player_balance} единиц")

    if player_balance <= 0:
        print("Игра окончена. Вы потеряли все средства.")

if __name__ == "__main__":
    casino_game()