# This is a sample Python script.
import math
from collections import defaultdict
# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def giant_step_interval(x: int) -> int:
    return math.ceil(math.sqrt(x))

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

def multiplicative_inverse(a, b):
    if a - b < 0:
        a,b = b,a
    b_inverse = extended_euclidean_algorithm(a,b)[1]
    if b_inverse < 0:
        return a + b_inverse
    return b_inverse


def giant_step(h_inner, p_inner, m_inner, m_inverse_remainder):
    key: int = 0
    mir_copy = m_inverse_remainder
    for i in range(1, m_inner, 1):
        answer = m_inverse_remainder * h_inner % p_inner
        d[answer].append(m_inner * i)
        if d[answer].__len__() > 1:
            return answer
        m_inverse_remainder = m_inverse_remainder * mir_copy
        while m_inverse_remainder > p_inner:
            m_inverse_remainder = m_inverse_remainder - p_inner
    return key

def extended_euclidean_algorithm(a: int, b: int):
    s_1 = 1; s_2 = 0; t_1 = 0; t_2 = 1
    if a - b < 0:
        a,b = b,a
    return extended_euclidean_algorithm_helper(a, b, s_1, s_2, t_1, t_2) # b <= a
def extended_euclidean_algorithm_helper(a: int, b: int, s_1: int, s_2: int, t_1: int, t_2: int):
    q: int = 0
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


    g_inverse: int = multiplicative_inverse(p, g)
    m: int = giant_step_interval(p)
    d = defaultdict(list)
    baby_step(g, m, p, save)
    inverse_remainder: int = baby_step(g_inverse, m, p, discard)
    key: int = giant_step(h, p, m, inverse_remainder)
    print("gˣ ≡",h, "mod",p)
    print("x = ",sum(d[key]))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
