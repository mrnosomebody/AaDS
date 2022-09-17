n = int(input())
for i in range(n):
    f_name, l_name, m_name, day, month, year = input().split(',')
    fio = f_name + l_name + m_name
    birth_sum = 0
    distinct_fio_chars = set()
    pos_in_alphabet = (ord(fio[0]) - ord('A') + 1)
    sum_ = 0

    for c in fio:
        distinct_fio_chars.add(c)

    for num in day + month:
        birth_sum += int(num)

    sum = len(distinct_fio_chars) + 64 * birth_sum + 256 * pos_in_alphabet
    hex_sum = hex(sum)[-3:].upper().zfill(3)

    print(hex_sum, end=' ')