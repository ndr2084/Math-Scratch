from collections import defaultdict
from math import sqrt
from chinese_remainder_theorem import compute_CRT

def prime_factors(n: int) -> list:
    prime_factors_dict = defaultdict(int)
    prime_factors_dict[n] += 1
    prime_factors_list = []
    for key, value in prime_factors_helper(n, prime_factors_dict).items():
        prime_factors_list.append(key ** value)
    return prime_factors_list

def prime_factors_helper(n: int, prime_factors_dict: dict) -> dict:
    upper_bound: int = int(sqrt(n)) + 1
    for i in range(2, upper_bound, 1):
        if n % i == 0:
            prime_factors_dict.pop(n)
            prime_factors_dict[(n // i)] += 1
            prime_factors_dict[i] += 1
            prime_factors_helper(n // i, prime_factors_dict)
            break
    return prime_factors_dict

def squares_mod_m(a: int, prime_factors_list: list) -> list:
    x: int = 1
    squares_mod_m_list = []
    for i in range(0, len(prime_factors_list), 1):
        while (x ** 2) % prime_factors_list[i] != a % prime_factors_list[i]:
            x += 1
        squares_mod_m_list.append(x)
        x = 0
    return squares_mod_m_list

def compute_square_root_modulo(mi, ai):
    neg_ai = []
    for i in range(0, len(ai), 1):
        neg_ai.append(mi[i] - ai[i])
    ai_total = []
    for i in range(0, len(ai), 1):
        ai_total.append((ai[i],neg_ai[i]))

    #this is so ugly and I hate it but damnit it works
    for i in range(0, 2**len(ai), 1):
        temp = []
        combination = format(i, f'0{len(ai)}b')
        for j in range(0, len(ai), 1):
            temp.append(ai_total[j][int(combination[j])])
        print(compute_CRT(temp,mi))

#TODO: doesn't fail gracefully. Do unit testing
if __name__ == "__main__":
    a = 813
    mi = prime_factors(868)
    ai = squares_mod_m(a, mi)
    compute_square_root_modulo(mi, ai)