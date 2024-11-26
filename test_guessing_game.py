from guessing_game import guess_number

def test_guess_too_low():
    assert guess_number(50, 30) == "Too low!"

def test_guess_too_high():
    assert guess_number(50, 70) == "Too high!"

def test_guess_correct():
    assert guess_number(50, 50) == "Correct!"
