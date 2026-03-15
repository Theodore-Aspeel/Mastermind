"""
Projet Mastermind

__author__ = Théodore Aspeel

"""

# --------------------------Import libraries--------------------------
from typing import List
from random import random, choice

# --------------------------Constants--------------------------

COLORS = ["red", "green", "blue", "yellow", "orange", "purple"]
CODE_LENGTH = 4


# --------------------------Fonctions--------------------------


def secrete_code() -> List[str]:
    """
    Choose randomly colours to the code that the player will have to guess
    """
    selected_color = []
    for _ in range(CODE_LENGTH):
        # Add a random color to the end of an existing list
        selected_color.append(choice(COLORS))
    return selected_color

def guess_to_secret_compare(selected_color, player_selection) -> tuple[int, int]:
    """
     well_placed = good colour & good position --> black piece
     misplaced = good colour & bad position --> white piece
     misplace = total colour in commun - well_place

    total_common_color = the minimum of every color between the secret code, and the player guess.
    EX : GUESS : Y B R R & SECRET : R G B P. total_common_color = 1R 1B 0Y 0P


    """

    total_common_color = 0
    for colors in COLORS:
        total_common_color += min(
            player_selection.count(colors), selected_color.count(colors)
        )

    well_placed = 0
    for n in range(CODE_LENGTH):
        if player_selection[n] == selected_color[n]:
            well_placed += 1

    misplaced = total_common_color - well_placed

    return well_placed, misplaced


if __name__ == "__main__":
    # Don't forget to close the function.
    test_guess_to_secret_compare()
