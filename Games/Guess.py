import random

def guess_the_number():
    secret_number = random.randint(1, 100)  # Загадываем число от 1 до 100
    attempts = 0

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте угадать.")

    while True:
        try:
            guess = int(input("Ваше предположение: "))
            attempts += 1

            if guess < secret_number:
                print("Загаданное число больше.")
            elif guess > secret_number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    guess_the_number()