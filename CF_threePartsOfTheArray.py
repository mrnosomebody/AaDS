n = int(input())
arr = list(map(int, input().split()))
l = 0
s1 = 0
s2 = 0
res = 0

for r in range(n - 1, 0, -1):
    s2 += arr[r]
    while s1 < s2 and r > l:
        s1 += arr[l]
        l += 1
    if s1 == s2:
        res = max(res, s1)
print(res)