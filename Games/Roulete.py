import random

def roulette():
    print("Добро пожаловать в игру 'Рулетка'!")

    while True:
        input("Нажмите Enter, чтобы спинить рулетку...")

        result = random.randint(0, 36)  # В реальной рулетке есть числа от 0 до 36

        print(f"Выпало число: {result}")

        play_again = input("Хотите сыграть ещё раз? (да/нет): ")
        if play_again.lower() != "да":
            break

if __name__ == "__main__":
    roulette()