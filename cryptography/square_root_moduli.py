from collections import defaultdict
from email.policy import default
from math import sqrt

from numpy.core.defchararray import upper

from chinese_remainder_theorem import compute_CRT

def prime_factors(n: int) -> list:
    prime_factors_dict = defaultdict(int)
    prime_factors_dict[n] += 1
    prime_factors_list = []
    for key, value in prime_factors_helper(n, prime_factors_dict).items():
        prime_factors_list.append(key ** value)

    print (prime_factors_list)
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
    return squares_mod_m_list

#TODO: only calculates 1 root at the moment; update so all roots are calculated
#TODO: HINT- you can probably do the above all in the function below!
def compute_square_root_modulo(mi, ai):
    compute_CRT(ai, mi)

#TODO: doesn't fail gracefully. Do unit testing
if __name__ == "__main__":
    a = 813
    mi = prime_factors(868)
    print(mi)
    ai = squares_mod_m(a, mi)
    compute_square_root_modulo(mi, ai)