from collections import defaultdict
import heapq

n = int(input())
rockets = defaultdict(list)
for i in range(n):
    day, hour, minute, id_, status = input().split(' ')
    log_time = (int(day), int(hour), int(minute))
    rockets[int(id_)].append((log_time, status))

for i in rockets:
    heapq.heapify(rockets[i])

for key in sorted(rockets):
    rocket = rockets[key]
    res = 0
    while rocket:
        tmp = heapq.heappop(rocket)
        status = tmp[1]
        time = tmp[0]
        if status == 'A':
            start_time_in_mins = time[0] * 24 * 60 + time[1] * 60 + time[2]
        if status == 'S' or status == 'C':
            end_time_in_mins = time[0] * 24 * 60 + time[1] * 60 + time[2]
            res += end_time_in_mins - start_time_in_mins
    print(res, end=' ')