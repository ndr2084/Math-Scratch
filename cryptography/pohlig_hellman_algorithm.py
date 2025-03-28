from chinese_remainder_theorem import compute_CRT
from square_root_moduli import prime_factors
from giant_step_baby_step import compute_giant_step_baby_step

def fast_exponentiation(a: int, m: int, binary: int) -> int:
    if binary == 1:
        return a
    a = a * a % m
    return fast_exponentiation(a, m, binary>>1)

if __name__ == "__main__":
    # TODO: sooner or later you're gonna have to implement legranges theorem
    # step 1: find the prime factors
    mi = prime_factors(433 - 1) #[16, 27]
    print(mi)

    # step 2: solve the DLP for the sub groups
    print(f"h for next step: {fast_exponentiation(166, 433, 16)}")
    print(int(compute_giant_step_baby_step(335,433,7)/16))

    print(f"h for next step: {(fast_exponentiation(166, 433, 16) *
          (fast_exponentiation(166, 433, 8)) *
          (fast_exponentiation(166, 433, 2)) *
          (fast_exponentiation(166, 433, 1))) % 433}")
    print(int(compute_giant_step_baby_step(250, 433, 7) / 27))

    #step 3: apply CRT to the DLP solutions found in step 2
    ai =[15,20]
    print(compute_CRT(ai, mi))

