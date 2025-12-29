"""
Projet Mastermind

__author__ = Théodore Aspeel

"""

# --------------------------Import libraries--------------------------
from typing import List, Tuple
from random import random, choice

# --------------------------Constants--------------------------

COLORS = ["red", "green", "blue", "yellow", "orange", "purple"]
CODE_LENGTH = 4

# --------------------------Fonctions--------------------------

def secrete_code() -> List[str]:
    """
    Choose randomly colours to the code that the player will have to guess
    """
    selected_colour = []
    for _ in range(CODE_LENGTH):
        # Add a random color to the end of an existing list
        selected_colour.append(choice(COLORS))
    return selected_colour
# print(secrete_code())

"""def player_selection() -> List[str]:
    colour_guess = []
    for _ in range(CODE_LENGTH):
        colour_guess.append(choice(COLORS))
    return colour_guess
    
    PAS DE SELECTION ICI MAIS DANS L UI DIRECTEMENT
    """

def guess_test():

    well_placed = 0
    for n in range(CODE_LENGTH):
        if player_selection(n) == secrete_code(n):
            well_placed += 1

    good_colour = 0
    for _ in range(CODE_LENGTH):
        if

