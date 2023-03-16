n = int(input())
arr = map(int, input().split())
print(len(list(filter(lambda x: x > 0, arr))))