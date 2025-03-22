from collections import defaultdict
from itertools import permutations, combinations


def euclidean_algorithm(a: int, b: int) -> int:
    q: int = 0
    while a > b:
        a = a - b
        q = q + 1

    if a < b: # the remainder is larger than 0
        return euclidean_algorithm(b, a)

    if a - b == 0:
        return a

    if a == 1: # a would be the dividend of the next step, and anything divided by 1 will have remainder 0, thus a = gcd
        return a

def pairwise_coprime(S: list):
    combo = tuple(combinations(S, 2))
    for i in range(0, len(combo), 1):
        if euclidean_algorithm(combo[i][0], combo[i][1]) > 1:
            return False
    return True

if __name__ == "__main__":
    a: int = 35
    b: int = 17
    loop_variables = defaultdict(int)
    S_modulo = [8,3,7,9,18]
    print(pairwise_coprime(S_modulo))

    if a - b < 0:
        a,b = b,a
