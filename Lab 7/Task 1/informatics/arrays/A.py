n = int(input())
arr = input().split()
print(*[arr[i] for i in range(n) if i % 2 == 0])