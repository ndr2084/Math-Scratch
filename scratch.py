##Nathan Rous: Jan 23 2025 @ 11:21am
##Some shitty scratch to help solve linear recurrence relations

r1: int = 1
r2: int = 1
import math

r1_values: list = []
r2_values: list = []
differences: list = []
quotient: list = []
gcd: list = []
mod: list = []
r1_values.append(r1)
r2_values.append(r2)
# r1 = r1 + r2
# r2 = r1 + 2(r2)
temp1: int = r1
counter: int = 3
for i in range(3, 100, 1):
    print("r%d = %d + %d = %d" % (counter, r1, r2, r1 + r2))
    counter += 1
    print("r%d = %d + 2(%d) = %d" % (counter, r1, r2, r1 + 2*r2))
    counter += 1
    r1 = r1 + r2
    r2 = temp1 + 2*r2
    r1_values.append(r1)
    r2_values.append(r2)
    differences.append(r1 - r2)
    quotient.append(r2 / r1)
    mod.append(r1 % r2)
    gcd.append(math.gcd(r2, r1))
    temp1 = r1

print(r1_values)
print(r2_values)
print(differences)
print(quotient)
print(mod)
print(gcd)





