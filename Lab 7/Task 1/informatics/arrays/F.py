n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, n - 1):
    cnt += 1 if arr[i] > arr[i - 1] and arr[i] > arr[i + 1] else 0
print(cnt)