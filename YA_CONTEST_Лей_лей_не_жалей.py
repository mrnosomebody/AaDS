# This solution is inefficient
n = int(input())
orders = []
for i in range(n):
    start, end, cost = list(map(int, input().split()))
    orders.append((start, end, cost))
q = int(input())

for i in range(q):
    start, end, type = list(map(int, input().split()))
    if type == 1:
        amount = 0
        for order in orders:
            if start <= order[0] <= end:
                amount += order[2]
        print(amount, end=' ')
    else:
        time = 0
        for order in orders:
            if start <= order[1] <= end:
                time += (order[1] - order[0])
        print(time, end=' ')