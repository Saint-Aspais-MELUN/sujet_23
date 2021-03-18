from exercices.exercice1 import *

def test_occurence_lettres():
    phrase = "Hello world !"
    assert occurence_lettres(phrase) == {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1, '!': 1}
