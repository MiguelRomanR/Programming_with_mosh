import random

# Roll the Dice

user = input("Enter your name: ").strip()
print(f'\nHi {user}, Welcome to the game! Good luck!! 🙌')

count = 0
points = 0

while True:
    game = input(
        f"\n{user}, do you want to roll the dice? (y/n): ").strip().lower()

    if game == 'y':
        # Generar los valores de los dados y calcular el total
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        total = dice_1 + dice_2

        # Contar las veces que se ha jugado y sumar los puntos totales
        count += 1
        points += total  # Acumula los puntos generados en cada turno

        # Mostrar el resultado de la tirada
        print(
            f"\n  ➡️ You rolled {dice_1} and {dice_2}, that's {total} points!")

    elif game == 'n':
        # Mostrar el total de veces que se ha jugado y la puntuación total
        print(
            f'\n  ➡️ You rolled the dice {count} times and got {points} points.')
        print(f'\n  ➡️ Thanks for playing, come back later! 🙌\n')
        break

    else:
        print(f'\nPlease enter a valid option (y/n).')
