n = int(input())
rows = []
for _ in range(n):
    left, right = input().split('_')
    rows.append([left, right])
m = int(input())
reqs = []
for _ in range(m):
    num, side, position = input().split(' ')
    reqs.append((int(num), side, position))
row_letter = ('ABC', 'DEF')
for req in reqs:
    num = req[0]
    side = req[1]
    position = req[2]
    out = []
    if side == 'right' and position == 'aisle':
        flag = 0
        for i in range(len(rows)):
            if rows[i][1][:num] == '.' * num:
                rows[i][1] = 'X' * num + rows[i][1][num:]
                for letter in row_letter[1][:num]:
                    out.append(f'{i + 1}{letter}')
                print(f'Passengers can take seats: {" ".join(out)}')
                for row in rows:
                    print(row[0] + '_' + row[1])
                rows[i][1] = '#' * num + rows[i][1][num:]
                flag = 1
                break
        if not flag:
            print('Cannot fulfill passengers requirements')
        continue
    if side == 'right' and position == 'window':
        flag = 0
        for i in range(len(rows)):
            if rows[i][1][-1:-num - 1:-1] == '.' * num:
                rows[i][1] = rows[i][1][:-num] + 'X' * num
                for letter in row_letter[1][-num:]:
                    out.append(f'{i + 1}{letter}')
                print(f'Passengers can take seats: {" ".join(out)}')
                for row in rows:
                    print(row[0] + '_' + row[1])
                rows[i][1] = rows[i][1][:-num] + '#' * num
                flag = 1
                break
        if not flag:
            print('Cannot fulfill passengers requirements')
        continue
    elif side == 'left' and position == 'aisle':
        flag = 0
        for i in range(len(rows)):
            if rows[i][0][-1:-num - 1:-1] == '.' * num:
                rows[i][0] = rows[i][0][:-num] + 'X' * num
                for letter in row_letter[0][-num:]:
                    out.append(f'{i + 1}{letter}')
                print(f'Passengers can take seats: {" ".join(out)}')
                for row in rows:
                    print(row[0] + '_' + row[1])
                rows[i][0] = rows[i][0][:-num] + '#' * num
                flag = 1
                break
        if not flag:
            print('Cannot fulfill passengers requirements')
        continue
    elif side == 'left' and position == 'window':
        flag = 0
        for i in range(len(rows)):
            if rows[i][0][:num] == '.' * num:
                rows[i][0] = 'X' * num + rows[i][0][num:]
                for letter in row_letter[0][:num]:
                    out.append(f'{i + 1}{letter}')
                print(f'Passengers can take seats: {" ".join(out)}')
                for row in rows:
                    print(row[0] + '_' + row[1])
                rows[i][0] = '#' * num + rows[i][0][num:]
                flag = 1
                break
        if not flag:
            print('Cannot fulfill passengers requirements')
        continue
