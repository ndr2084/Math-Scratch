from math import sqrt
from chinese_remainder_theorem import compute_CRT

def prime_factors(n: int) -> list:

    prime_factors_list = [n]
    prime_factors_helper(n, prime_factors_list)
    return prime_factors_list

def prime_factors_helper(n: int, prime_factors_list: list) -> list:

    upper_bound: int = int(sqrt(prime_factors_list[len(prime_factors_list) - 1])) + 1
    for i in range(2, upper_bound, 1):
        if n % i == 0:
            prime_factors_list[len(prime_factors_list) - 1] = i
            prime_factors_list.append(n // i)
            prime_factors_helper(n // i, prime_factors_list )
            break
    return prime_factors_list

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
    a = 340
    mi = prime_factors(437)
    ai = squares_mod_m(a, mi)
    compute_square_root_modulo(mi, ai)


