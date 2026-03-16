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
    """Create the secret code by choosing 4 random colors from the COLORS list."""
    selected_color = []
    for _ in range(CODE_LENGTH):
        # Add a random color to the end of an existing list
        selected_color.append(choice(COLORS))
    return selected_color


def guess_to_secret_compare(selected_color, player_selection) -> tuple[int, int]:
    """
    Compare the secret code with the player guess.

    The function returns:
    - the number of well placed colors
    - the number of correct colors but in the wrong position
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

