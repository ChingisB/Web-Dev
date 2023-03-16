n = int(input())
arr = list(map(int, input().split()))
print(*[arr[i] for i in range(n) if arr[i] % 2 == 0])