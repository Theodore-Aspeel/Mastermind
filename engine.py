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


def guess_test(selected_colour, color_guess) -> tuple[int, int]:
    """
    well_placed = good colour & good position --> black piece
    misplaced = good colour & bad position --> white piece
    misplace = total colour in commun - well_place

   total_common_color = the minimum of every color between the secret code, and the player guess.
   EX : GUESS : Y B R R & SECRET : R G B P. total_common_color = 1R 1B 0Y 0P


    """
    player_selection = ["red", "green", "blue", "yellow"]
    selected_colour = ["blue", "green", "purple", "green"]

    total_common_color = 0
    for colors in COLORS:
        total_common_color += min(player_selection.count(colors), selected_colour.count(colors))

    well_placed = 0
    for n in range(CODE_LENGTH):
        if player_selection[n] == selected_colour[n]:
            well_placed += 1

    misplaced = total_common_color - well_placed

    return well_placed, misplaced

def test():
    player_selection = ["red", "green", "blue", "yellow"]
    selected_colour = ["blue", "green", "purple", "green"]
    guess_test(selected_colour, player_selection)



    print(guess_test(selected_colour, player_selection))