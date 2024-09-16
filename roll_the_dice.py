import random

# Creamos una variable para que el no de usuario y otra
# para que pueda ingresar su opción
name = input("What's your name?: ")

while True:
    choice = input("\nRoll the dice? (y/n): ").lower()
    if choice == 'y':
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print(f'{dice_1}, {dice_2}')
    elif choice == 'n':
        print(f'Good bye {name}, Thanks for playing')
        break
    else:
        print('Invalid choice')
