from math import sqrt

def prime_factors(n: int) -> list:

    prime_factors_list = [n]
    prime_factors_helper(n, prime_factors_list)
    return prime_factors_list

def prime_factors_helper(n, prime_factors_list):

    upper_bound: int = int(sqrt(prime_factors_list[len(prime_factors_list) - 1])) + 1
    for i in range(2, upper_bound, 1):
        if n % i == 0:
            prime_factors_list[len(prime_factors_list) - 1] = i
            prime_factors_list.append(n // i)
            prime_factors_helper(n // i, prime_factors_list )
            break

if __name__ == "__main__":

    print(prime_factors(4189))