n = int(input())
ans = None
for i in range(2, n + 1):
    if n % i == 0:
        ans = i
        break
print(ans)