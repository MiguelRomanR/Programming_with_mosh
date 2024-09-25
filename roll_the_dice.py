import random  # Asegúrate de importar el módulo random al inicio

# Solicitar el nombre del usuario
user = input("Enter your name: ").strip()
print(f'\nHi {user}, Welcome to the game! Good luck!! 🙌')

while True:
    # Preguntar si el usuario quiere lanzar los dados
    game = input(
        f"\n{user}, do you want to roll the dice? (y/n): ").strip().lower()

    # Validar la respuesta del usuario
    if game == 'y':
        # Lanzar los dados y calcular el total
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        total = dice_1 + dice_2
        print(
            f"\n  ➡️ You rolled {dice_1} and {dice_2}, that's {total} points!")

    elif game == 'n':
        print(f'\n  ➡️ Thanks for playing, come back later! 🙌\n')
        break

    else:
        print(f'\nPlease enter a valid option (y/n).')
