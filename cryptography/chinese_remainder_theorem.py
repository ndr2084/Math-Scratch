from itertools import combinations
from cryptography.giant_step_baby_step import multiplicative_inverse

def gcd(a: int, b: int) -> int:
    if a < b:
        a,b = b,a
    if a == 0 or b == 0:
        return abs(a + b)
    while a >= b:
        a = a - b
    return gcd(b,a)

def pairwise_coprime(S: list, ai: list) -> bool:
    combo = tuple(combinations(S, 2))
    for i in range(0, len(combo), 1):
        result = gcd(combo[i][0], combo[i][1])
        if result > 1:
            print(f"gcd({combo[i][0]}, {combo[i][1]}) = {result}. Checking if solution exists...")
            solution_exists(result, i, ai)
            #raise ValueError(f"values aren't pairwise coprime. gcd({combo[i][0]}, {combo[i][1]}) = {result}")
    return True

#TODO: this is scuffed and only works when len(ai) is 2. Consider combining ai and mi into a k:v pair
def solution_exists(result: int, i: int, ai: list) -> bool:
    difference: int = 0
    difference = difference + abs(ai[i] - ai[i+1])
    if difference % result == 0:
        print(f"{difference} | {result} is true")
        return True
    raise ValueError(f" {result} | {difference} is false. Thus, no solution exists")

def modulo_M(S: list) -> int:
    M: int = 1
    for i in range(0,len(S), 1):
        M = M * S[i]
    print(f"Product of all members of the set of modulo {S} is M = {M} ")
    return M

def modulo_Mi(S: list, M: int) -> list:
    Mi = []
    for i in range(0, len(S), 1):
        Mi.append( (M//S[i]))
        print(f"M/m{i+1} = {Mi[i]}")
    return Mi

def modulo_Mi_inverse(Mi: list, mi: list) -> list:
    Mi_inverse = []
    for i in range(0, len(Mi), 1):
        Mi_inverse.append(multiplicative_inverse(mi[i], Mi[i])) #mi is 1st argument, Mi is 2nd
        print(Mi_inverse[i] ,"*", Mi[i], "≡", "1 mod", mi[i])
    print("Thus, M_inverse =",Mi_inverse)
    return Mi_inverse

def CRT_result(ai: list, Mi:list, Mi_inverse: list, M: int) -> int:
    result: int = 0
    for i in range(0, len(ai), 1):
        result = result + (ai[i] * Mi[i] * Mi_inverse[i])
    while(result > M):
        result = result - M
    print("Final result:", result, "mod", M)
    return result

def compute_CRT(ai: list, mi: list):
    pairwise_coprime(mi, ai)
    M = modulo_M(mi)
    Mi = modulo_Mi(mi, M)
    Mi_inverse = modulo_Mi_inverse(Mi, mi)
    CRT_result(ai, Mi, Mi_inverse, M)

if __name__ == "__main__":
    mi = [7,449]
    ai = [1, 40]
    compute_CRT(ai, mi)

