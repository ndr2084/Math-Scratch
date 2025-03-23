from collections import defaultdict
from itertools import permutations, combinations
from cryptography import giant_step_baby_step
from cryptography.giant_step_baby_step import multiplicative_inverse


def gcd(a: int, b: int) -> int:
    if a < b:
        a,b = b,a

    if a == 0 or b == 0:
        return abs(a + b)

    while a >= b:
        a = a - b

    if a == 1:
        return a
    else:
        return gcd(b,a)




def pairwise_coprime(S: list) -> bool:
    combo = tuple(combinations(S, 2))
    for i in range(0, len(combo), 1):
        if gcd(combo[i][0], combo[i][1]) > 1:
            print(combo[i][0], combo[i][1])
            return False
    return True

def modulo_M(S: list) -> int:
    M: int = 1
    for i in range(0,len(S), 1):
        M = M * S[i]
    return M

def modulo_Mi(S: list, M: int) -> list:
    Mi = []
    for i in range(0, len(S), 1):
        Mi.append( (M//S[i]))
    return Mi

def modulo_Mi_inverse(S: list, M: list) -> list:
    Mi_inverse = []
    for i in range(0, len(Mi), 1):
        #print(S[i],"", M[i])
        Mi_inverse.append(multiplicative_inverse(M[i], S[i]))
   # print(Mi_inverse)
    return Mi_inverse

def CRT_result(ai: list, Mi:list, Mi_inverse: list, M: int) -> int:
    result: int = 0
    for i in range(0, len(ai), 1):
        result = result + (ai[i] * Mi[i] * Mi_inverse[i])
    print(result,"mod",M)
    while(result > M):
        result = result - M
    return result




if __name__ == "__main__":
    print(gcd(236, 108))
    mi = [3, 5, 7]
    ai = [2,3,2]
    print(pairwise_coprime(mi))
    M = modulo_M(mi)
    print(M)
    Mi = modulo_Mi(mi, M)
    print(Mi)
    Mi_inverse = modulo_Mi_inverse(Mi, mi)
    print(Mi_inverse)
    result = CRT_result(ai, Mi, Mi_inverse, M)
    print(result)

