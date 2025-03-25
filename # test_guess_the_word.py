# test_guess_the_word.py
import guess_the_word

def test_select_word_is_in_list():
    word = guess_the_word.select_word()
    assert word in guess_the_word.WORD_LIST

def test_correct_guess_updates_state():
    word = "loop"
    guess = "o"
    guessed = ["_"] * len(word)
    
    for idx, letter in enumerate(word):
        if letter == guess:
            guessed[idx] = guess

    assert guessed == ["_", "o", "o", "_"]
