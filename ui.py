# --------------------------Import libraries--------------------------
import tkinter as tk
import engine

# --------------------------UI Constants--------------------------
BACKGROUND_COLOR = "floral white"
TITLE_FONT = ("Helvetica", 20, "bold")
CELL_FONT = ("Arial", 16, "italic")
BUTTON_FONT = ("Arial", 12)
CELL_PADDING = 10
PAD_X = 6
PAD_Y = 6
COLORS = ["red", "green", "blue", "yellow", "orange", "purple"]

# --------------------------UI Variables--------------------------

current_row = 0
current_column = 0
# List that contain the 4 colors secret code generate by engine.secret_code().
secret_code = []
current_guess = []
feedback_pawns = []
# Flag that says if the game is finished or not.
game_finished = False
score = 0


# --------------------------MAIN FUNCTION--------------------------
def main() -> None:
    """
    1. Create the windows ( root)
    2. Build the interface ( frames, labels, etc)
    3. Initiate the secret code from engine
    4. Launch the main loop.
    """
    global root, secret_code
    root = tk.Tk()

    build_ui()
    build_title()
    build_board_display()
    build_button()
    build_victory_or_lose_message()
    color_choice_display()

    secret_code = engine.secrete_code()

    global score

    # Open the file to read the score saved ( "r" = read)
    try:
        file = open("score.txt", "r")
        score = int(file.read())
        file.close()
    except:
        score = 0

    root.mainloop()


def build_ui():
    """Build the main window/the root"""
    root.title("Mastermind")
    root.configure(background=BACKGROUND_COLOR)


def build_button() -> None:
    # Frame that contains our buttons
    button_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
    button_frame.pack(padx=PAD_X, pady=PAD_Y)

    lbl_delete_button = tk.Button(
        button_frame, text="Delete", bg="SlateGray", command=on_delete_click
    )
    lbl_delete_button.pack(side="left", padx=PAD_X, pady=PAD_Y)
    lbl_new_game_button = tk.Button(
        button_frame,
        text="New Game",
        bg="forest green",
        command=on_new_game_button_click,
    )
    lbl_new_game_button.pack(side="right", padx=PAD_X, pady=PAD_Y)


def build_title() -> None:
    title_frame = tk.Frame(root, bg="RoyalBlue4")
    title_frame.pack(padx=PAD_X, pady=PAD_Y)

    lbl_title = tk.Label(
        title_frame, font=TITLE_FONT, text="MASTERMIND", fg="white", bg="RoyalBlue4"
    )
    lbl_title.pack(padx=PAD_X, pady=PAD_Y)

    lbl_subtitle = tk.Label(
        title_frame,
        font=(
            "Helvetica",
            14,
        ),
        text="Guess the secret code",
        fg="white",
        bg="RoyalBlue4",
    )
    lbl_subtitle.pack(padx=PAD_X, pady=PAD_Y)


def build_board_display():
    """Build the board.The smallest unit is the cells
    The board is made of 10 rows. Each row contains :
    - a guess zone of 4 cells ( the color square of the game)
    - a feedback area made of 4 cells maximum ( black/withe pawn)
    """
    global cells, feedback_frames, feedback_pawns

    board_frame = tk.Frame(root, bg="grey17")
    board_frame.pack(padx=PAD_X, pady=PAD_Y)

    cells = []
    feedback_frames = []
    feedback_pawns = []

    # One iteration for each row
    for row in range(10):
        row_cells = []
        feedback_pawns.append([])

        row_frame = tk.Frame(board_frame, bg="grey17")
        row_frame.pack(padx=PAD_X, pady=PAD_Y)

        guess_frame = tk.Frame(row_frame, bg="white")
        guess_frame.pack(padx=PAD_X, side="left")

        cell_box_frame = tk.Frame(guess_frame, bg="white")
        cell_box_frame.pack(padx=PAD_X, side="left")

        feedback_frame = tk.Frame(row_frame, bg="RoyalBlue4")
        # We need to stock the frame value row after row.
        feedback_frames.append(feedback_frame)

        for col in range(4):
            cell_frame = tk.Frame(cell_box_frame, bg="black", width=14, height=14)
            cell_frame.pack(padx=20, pady=PAD_Y, side="left")
            # We stock cell_frame in row_cells in order to find it back and retrieve the color.
            # So row_cells become a list that contains [case0, ..., case3]
            row_cells.append(cell_frame)

        # After creating the 4 cells of the line. We add the list row_cells in the cells list.
        # So we've a list of lists ( 2d matrix). Cells[row][col] represents the cells to modify it.
        cells.append(row_cells)


def build_victory_or_lose_message():
    global status_label, secret_display_frame
    # Set up an empty text because we don't want to display anything before lose or victory
    status_label = tk.Label(root, text="", font=("Helvetica", 14), bg=BACKGROUND_COLOR)
    status_label.pack(pady=10)

    # Use to display the color squares
    secret_display_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
    secret_display_frame.pack()

    # Set the number of attempts message
    status_label.configure(text="Attempts left: 10")


def color_choice_display():
    palette_frame = tk.Frame(root, bg="grey17")
    palette_frame.pack(padx=PAD_X, pady=PAD_Y)

    # Build one button per color in the COLORS list. We use the lambda to pass the current color to on_color_click.
    # The "c=color" captures the argument one at time.
    for color in COLORS:
        btn_color_palette = tk.Button(
            palette_frame,
            width=4,
            height=2,
            bg=color,
            command=lambda c=color: on_color_click(c),
        )
        btn_color_palette.pack(padx=PAD_X, pady=PAD_Y, side="left")


# ------------EVENT-------------------------
# Run the application only when this file is executed directly (main files)


def add_feedback_frame(row, result):
    """Add black and white pawns for a row"""

    black = result[0]
    white = result[1]

    feedback_frames[row].pack(padx=PAD_X, pady=PAD_Y, side="left")

    for _ in range(black):
        pawn = tk.Frame(feedback_frames[row], width=8, height=8, bg="black")
        pawn.pack(padx=PAD_X, pady=PAD_Y, side="left")
        feedback_pawns[row].append(pawn)

    for _ in range(white):
        pawn = tk.Frame(feedback_frames[row], width=8, height=8, bg="white")
        pawn.pack(padx=PAD_X, pady=PAD_Y, side="left")
        feedback_pawns[row].append(pawn)


def remove_feedback_frame():
    """Remove all feedback pawns from the board"""

    for row in range(10):
        for pawn in feedback_pawns[row]:
            pawn.pack_forget()

        feedback_pawns[row] = []

        # hide the blue feedback area frame
        feedback_frames[row].pack_forget()


def on_color_click(color):
    """
    Function called when a color buton is clicked. The goal of the function is to :
    1. Add the color to the actual try (current_guess)
    2. Color the correct cells of the board
    3. When 4 colors are selected.
        -  call engine.guess_to_secret_compare() to get the feedback
        - display the feedback pawns
        - Go to the next cells and "restart" the turn
    """

    # Modify the global state variable : position, try, secret
    global current_column, current_row, current_guess, secret_code, game_finished, score

    # If the game is finished, ignore next clicks
    if game_finished:
        return
    # If we already filled 4 columns, we ignore the next clics
    if current_column >= 4:
        return

    # Store the clicked color of the actual try.
    current_guess.append(color)

    cells[current_row][current_column].configure(bg=color)

    current_column += 1

    # Value for one full turn
    if current_column == 4:
        # Compare secret_code/current_guess and send black and white
        result = engine.guess_to_secret_compare(secret_code, current_guess)
        # Affiche le feedback in the zone of the current_row
        add_feedback_frame(current_row, result)

        # When 4 black pawns, it's a win.
        if result[0] == 4:
            status_label.configure(text="Congratulations ! YOU WIN ")

            score += 1

            file = open("score.txt", "w")
            file.write(str(score))
            file.close()

            game_finished = True
            return

        if current_row == 9 and result[0] != 4:
            status_label.configure(text="Game Over!")
            display_secret_code(secret_code)
            game_finished = True
            return

        # Empty the list and go back to the first column
        current_guess = []
        current_column = 0
        current_row += 1
        # Display the number of attempt
        status_label.configure(text=f"Attempts left: {10 - current_row}")


def on_delete_click():
    """Delete the last selected color"""

    global current_column, current_guess

    if current_column > 0:
        current_column -= 1
        # Use pop instead of clear to remove only the last color.
        current_guess.pop()
        cells[current_row][current_column].configure(bg="black")


def on_new_game_button_click():
    """Reset the whole board by putting all the cells back to black.
    And reset the secret code"""

    global current_row, current_column, current_guess, secret_code, game_finished

    current_row = 0
    current_column = 0
    current_guess = []

    game_finished = False

    for row in range(10):
        for col in range(4):
            cells[row][col].configure(bg="black")

    remove_feedback_frame()

    secret_code = engine.secrete_code()

    # Use to reset the win/lose message
    status_label.configure(text="Attempts left: 10")
    secret_display_frame.pack_forget()
    secret_display_frame.pack()


def display_secret_code(secret_code):
    """Display the secret code in visual way with color squares"""

    try:

        label = tk.Label(
            secret_display_frame,
            text="The secret code was:",
            bg=BACKGROUND_COLOR
        )
        label.pack(side="left", padx=10)

        for color in secret_code:
            square = tk.Frame(secret_display_frame, width=16, height=16, bg=color)
            square.pack(side="left", padx=5)

    except:
        print("Error: impossible to display secret code")

if __name__ == "__main__":
    main()
