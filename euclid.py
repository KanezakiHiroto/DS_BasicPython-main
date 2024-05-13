import random
import math

a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# Q3
def Q3(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a

print("Q3 ({}, {})の最大公約数は{}".format(a, b, Q3(a, b)))

# Q4
def Q4(a, b):
    return Q3(a, b) == 1

if Q4(a, b):
    print("Q4 {}と{}は互いに素である".format(a, b))
else:
    print("Q4 {}と{}は互いに素ではない".format(a, b))

# extra
combination = 100000
count = 0

for _ in range(combination):
    a = random.randint(1, 10000)
    b = random.randint(1, 10000)
    if Q4(a, b):
        count += 1

probability = count / combination
prediction = 6 / (math.pi**2)

print("extra挑戦")
print("予想確率 (6/π^2):", prediction)
print("計算結果:", probability)
