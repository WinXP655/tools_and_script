import random

def lottery_game():
    winning_numbers = [random.randint(1, 50) for _ in range(6)]

    print("Добро пожаловать в лотерею!")
    print("Выигрышные числа:", winning_numbers)

    player_numbers = []
    for i in range(6):
        while True:
            try:
                num = int(input(f"Введите число {i + 1} (от 1 до 50): "))
                if 1 <= num <= 50:
                    player_numbers.append(num)
                    break
                else:
                    print("Число должно быть в диапазоне от 1 до 50.")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите целое число.")

    matching_numbers = set(player_numbers) & set(winning_numbers)

    print("Ваши числа:", player_numbers)
    print("Совпавшие числа:", matching_numbers)

    if len(matching_numbers) > 0:
        print("Поздравляем! Вы угадали числа:", matching_numbers)
    else:
        print("К сожалению, вы не угадали ни одного числа.")

if __name__ == "__main__":
    lottery_game()