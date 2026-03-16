import engine


def check(secret, guess, expected):
    result = engine.guess_to_secret_compare(secret, guess)
    assert result == expected


def test_secret_code_has_4_colors():
    code = engine.secrete_code()
    assert len(code) == 4


def test_secret_code_only_allowed_colors():
    code = engine.secrete_code()
    for c in code:
        assert c in engine.COLORS


def test_compare_win_case():
    secret = ["red", "green", "blue", "yellow"]
    guess = ["red", "green", "blue", "yellow"]
    check(secret, guess, (4, 0))


def test_compare_no_common_color():
    secret = ["red", "red", "green", "green"]
    guess = ["blue", "blue", "yellow", "yellow"]
    check(secret, guess, (0, 0))


def test_compare_some_black_some_white():
    # check the black and white pawns
    secret = ["red", "green", "blue", "yellow"]
    guess = ["red", "blue", "purple", "green"]
    check(secret, guess, (1, 2))


def test_compare_only_misplaced():
    # When colors are correct but misplaced
    secret = ["red", "green", "blue", "yellow"]
    guess = ["green", "red", "yellow", "blue"]
    check(secret, guess, (0, 4))


def test_compare_when_duplicates():
    # Compare when duplicate colors appear
    secret = ["red", "red", "blue", "yellow"]
    guess = ["red", "green", "red", "purple"]

    # well placed: position 0 => red (1)
    # common colors: red=2 => misplaced = 2 - 1 = 1
    check(secret, guess, (1, 1))
