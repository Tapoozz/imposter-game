"""
Purpose: Have all the behind logic of the game
Author: Yuval (14.09.25)
"""


import random
import os
from termcolor import colored

class WordBank:
    WORDS = [
        "apple", "banana", "car", "mountain", "river", "computer", "guitar", "pyramid", "ocean", "camera"
    ]
    RELATED_WORDS = {
        "apple": "fruit",
        "banana": "yellow",
        "car": "vehicle",
        "mountain": "hill",
        "river": "stream",
        "computer": "keyboard",
        "guitar": "music",
        "pyramid": "Egypt",
        "ocean": "sea",
        "camera": "photo",
    }

    @classmethod
    def get_random_word(cls):
        return random.choice(cls.WORDS)

    @classmethod
    def get_related_word(cls, word):
        return cls.RELATED_WORDS[word]


class Player:
    def __init__(self, player_id: int, is_imposter: bool = False):
        self.player_id = player_id
        self.is_imposter = is_imposter

    def show_status(self, word: str, related_word: str):
        clear_screen()
        imposter = colored("IMPOSTER", "red", attrs=["bold"])
        crewmate = colored("CREWMATE", "green", attrs=["bold"])
        formatted_word = colored(word, "cyan", attrs=["bold"])
        print(f"\nPlayer {self.player_id+1}")
        print("="*30)
        if self.is_imposter:
            related = colored(related_word, "yellow", attrs=["bold"])
            print(f"You are the {imposter}!")
            print(f"Here is a hint: {related} (a word related to the secret word)")
            print("Try to blend in and guess the word.")
        else:
            print(f"You are a {crewmate}.")
            print(f"The secret word is: {formatted_word}")
        print("="*30)
        input("Press Enter when you're done...")
        clear_screen()


class Game:
    def __init__(self, min_players: int = 3):
        self.min_players = min_players
        self.players = []
        self.imposter_index = None
        self.secret_word = None

    def setup(self):
        print_intro()
        num_players = self.get_number_of_players()
        self.imposter_index = self.choose_imposter(num_players)
        self.secret_word = WordBank.get_random_word()
        self.players = [Player(i, i == self.imposter_index) for i in range(num_players)]
        print("\n--- Game Setup ---\n")
        for player in self.players:
            input(f"Player {player.player_id+1}, press Enter to see your word (make sure others aren't looking)...")
            if player.is_imposter:
                player.show_status(self.secret_word, WordBank.get_related_word(self.secret_word))
            else:
                player.show_status(self.secret_word, None)
        print("All players have seen their roles. Let the game begin!\n")

    def get_number_of_players(self):
        while True:
            try:
                num = int(input(f"Enter number of players (min {self.min_players}): "))
                if num < self.min_players:
                    print(f"Need at least {self.min_players} players.")
                    continue
                return num
            except ValueError:
                print("Please enter a valid number.")

    def choose_imposter(self, num_players):
        return random.randint(0, num_players - 1)


def clear_screen():
    os.system('cls' if os.name == "nt" else 'clear')

def print_intro():
        balloon = r'''
            .-""""-.
        .'        '.
     /   O    O   \
    :           `  :
    |             |
    :    .------.  :
     \  '        / 
        '.        .'
            '-.__.-'
     __   |  |   __
    (  `-.|  |.-'  )
     '-.________.-'
        IMPOSTER GAME
        --------------
        Welcome to the party game!
        One of you is the imposter...
        Try to blend in, or catch the fake!
    
        (Inspired by the classic party game)
        '''
        print(balloon)


def game_setup():
    Game().setup()
