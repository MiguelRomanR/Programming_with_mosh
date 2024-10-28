""" Se realiza una nueva versión donde van a incluir clases para poder
practicar Lógica de programación """

import random
from datetime import datetime


class DiceGame:
    def __init__(self):
        self.high_score = 0
        self.high_score_holder = None
        self.history = []

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

    def play(self):
        user = input("Enter your name: ").strip()
        print(f'\nHi {user}, Welcome to the game! Good Luck!! 🎲')
