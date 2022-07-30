n, t = map(int, input().split())
arr = list(map(int, input().split()))
l = 0
res = 0
s = 0

for r in range(n):
    s += arr[r]
    while l <= r:
        if s > t:
            s -= arr[l]
            l += 1
        else:
            break
    res = max(res, r - l + 1)
print(res)