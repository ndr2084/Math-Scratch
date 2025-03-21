from collections import defaultdict

def euclidean_algorithm(a: int, b: int) -> int:
    q: int = 0
    print("NEW: a:=",a, "b:=",b)
    while a > b:
        a = a - b
        q = q + 1

    print("q =", q,  "r=", a)
    if a < b: # the remainder is larger than 0
        return euclidean_algorithm(b, a)

    if a - b == 0:
        return a

    if a == 1: # a would be the dividend of the next step, and anything divided by 1 will have remainder 0, thus a = gcd
        return a





if __name__ == "__main__":
    a: int = 35
    b: int = 17
    loop_variables = defaultdict(int)
    S_n_choose_k = defaultdict()
    S_modulo = [8,3,7,9,18]
    if a - b < 0:
        a,b = b,a

    print(euclidean_algorithm(a, b))
