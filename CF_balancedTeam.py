n = int(input())
arr = sorted(list(map(int, input().split())))
l = 0
res = 1

for r in range(1, n):
    while arr[r] - arr[l] > 5:
        l += 1
    res = max(res, r - l + 1)

print(res)