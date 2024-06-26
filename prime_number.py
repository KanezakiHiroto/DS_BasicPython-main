

def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if prime(a):
    print(f"a = {a} は素数である")
else:
    print(f"a = {a} は素数ではない")

if prime(b):
    print(f"b = {b} は素数である")
else:
    print(f"b = {b} は素数ではない")
    