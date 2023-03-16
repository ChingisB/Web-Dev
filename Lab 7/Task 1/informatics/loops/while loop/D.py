n = int(input())
ans = True


while n != 1:
    if n % 2 == 1:
        ans = False
        break
    n = n // 2
print("YES" if ans else "NO")