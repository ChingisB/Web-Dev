a, b = int(input()), int(input())
a += a % 2
b += int(not b % 2)
print(*range(a, b, 2))