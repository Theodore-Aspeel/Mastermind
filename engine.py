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

def secrete_code_selection() -> List[str]:
    """
    Select randomly the secret colour code that the player will have to guess
    """
    selected_colour = []
    for _ in range(CODE_LENGTH):
        # Add a random color to the end of an existing list
        selected_colour.append(random(COLORS))
    return selected_colour
print(secrete_code_selection())
