import math
from collections import defaultdict

def giant_step_interval(n: int) -> int:
    return math.ceil(math.sqrt(n))

def baby_step(g: int, m: int, p, flag: int) -> int:
    temp: int = 1
    for i in range(0, m, 1):
        if flag == 1:
            d[temp].append(i)
        temp = temp * g

        while temp > p:
            temp = temp - p

    if flag == 0:
        return temp

def multiplicative_inverse(a: int, b: int) -> int:
    b_inverse = extended_euclidean_algorithm(a,b)[1]
    if b_inverse < 0:
        return a + b_inverse
    return b_inverse


def giant_step(h: int, p: int, m: int, inverse: int) -> int:
    key: int = 0
    inverse_copy = inverse
    for i in range(1, m, 1):
        answer = inverse * h % p
        d[answer].append(m * i)
        if d[answer].__len__() > 1:
            return answer
        inverse = inverse * inverse_copy
        while inverse > p:
            inverse = inverse - p
    return key

def extended_euclidean_algorithm(a: int, b: int):
    s_1 = 1; s_2 = 0; t_1 = 0; t_2 = 1
    return extended_euclidean_algorithm_helper(a, b, s_1, s_2, t_1, t_2)

def extended_euclidean_algorithm_helper(a: int, b: int, s_1: int, s_2: int, t_1: int, t_2: int):
    q: int = 0
    if a == b:
        raise ValueError(f"Multiplicative inverse does not exist for multiplicative_inverse(a,b)")
    if b == 0:
        return [1,0]
    while a > b:
        a = a - b
        q = q + 1
    a,b = b,a
    t_3 = t_1 - (t_2 * q)
    s_3 = s_1 - (s_2 * q)
    if  b == 1:
        result = [s_3, t_3]
        return result
    return extended_euclidean_algorithm_helper(a, b, s_2, s_3, t_2, t_3)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ##NOTE:
        #KEY := some integer that's congruent to both g^i mod p and congruent to h * (g^-1)^(m*j) mod p
        #VALUE := the exponents values i and/or m*j
    save = 1
    discard = 0

    ##MODIFY h,g,p BELOW TO CALCULATE ###
    h: int = 2213
    p: int = 3571
    g: int = 650

    d = defaultdict(list)
    g_inverse: int = multiplicative_inverse(p , g) # 1st arg m, 2nd arg a
    print("inverse",g_inverse)
    m: int = giant_step_interval(p)
    baby_step(g, m, p, save)
    inverse_remainder: int = baby_step(g_inverse, m, p, discard)
    key: int = giant_step(h, p, m, inverse_remainder)
    print(g,"ˣ ≡",h, "mod",p)
    print("x = ",sum(d[key]))
