from exercices.exercice2 import *

def test_fusion(L1, L2):
    assert fusion([1, 6, 10], [0, 7, 8, 9]) == [0, 1, 6, 7, 8, 9, 10]
