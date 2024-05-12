a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
def euclid(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

print("({}, {})の最大公約数は{}"
      .format(a, b, euclid(a, b)))