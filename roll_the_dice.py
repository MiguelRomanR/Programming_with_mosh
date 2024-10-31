""" Se realiza una nueva versión donde van a incluir clases para poder
practicar Lógica de programación """

import random
from datetime import datetime


class DiceGame:
    """ Se definen las funciones para hacer mas legible el código """

    def __init__(self):
        self.high_score = 0
        self.high_score_holder = None
        self.history = []

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

    def play(self):
        user = input("Enter your name: ").strip()
        print(f'\nHi {user}, Welcome to the game! Good Luck!! 🎲')

        count = 0
        points = 0

        while True:
            start_all = input(
                f'\n{user}, do you want to roll the dice? (y/n): ').strip().lower()

            if start_all == 'y':
                dice_1, dice_2 = self.roll_dice()
                total = dice_1+dice_2
                count += 1
                points += total

                # Se define el Json para guardar el historial del juego
                self.history.append({
                    'player': user,
                    'dice_1': dice_1,
                    'dice_2': dice_2,
                    'total': total,
                    'timestamp': datetime.now()
                })

                # Verificar si la tirada salen dobles
                if dice_1 == dice_2:
                    bonus = total*2
                    points += bonus
                    print(
                        f"\n  ➡️ DOUBLES! You rolled {dice_1} and {dice_2}. Bonus points! Total: {total + bonus} points! 🎯")
                else:
                    print(
                        f"\n  ➡️ You rolled {dice_1} and {dice_2}, that's {total} points! 🎲")

                # Mostrar las estadísticas del turno actual
                print("  📊 Current game stats:")
                print(f'     Rolls:{count}')
                print(f'     Total Points: {points}')
                print(f'     Average Points per Roll: {points/count:.1f}')

            elif start_all == 'n':
                # Actualizar high score si corresponde
                if points > self.high_score:
                    self.high_score = points
                    self.high_score_holder = user
                    print(f"\n  🏆 NEW HIGH SCORE! Congratulations {user}!")

            # Mostrar resumen final
                print('\n  📊 Final Stats:')
                print(f'     Rolls: {count}')
                print(f'     Total Points: {points}')
                print(f'     Average Points per Roll: {points/count:.1f}')
                print(
                    f'     High Score: {self.high_score} (by {self.high_score_holder})')
                print(f'\n  👋 Thanks for playing {user}, come back later!\n')
                break

            else:
                print("\n❌ Please enter a valid option (y/n).")


if __name__ == "__main__":
    start_all = DiceGame()
    start_all.play()
