phone_dict = {
    1: ('.', ',', '?', '!', ':'),
    2: ('A', 'B', 'C'),
    3: ('D', 'E', 'F'),
    4: ('G', 'H', 'I'),
    5: ('J', 'K', 'L'),
    6: ('M', 'N', 'O'),
    7: ('P', 'Q', 'R', 'S'),
    8: ('T', 'U', 'V'),
    9: ('W', 'X', 'Y', 'Z'),
    0: (' ',)
}

s = input()
res_nums = []

for el in s:
    for key, value in phone_dict.items():
        for i in range(len(value)):
            if el.upper() in value[i]:
                res_nums += str(key) * (i + 1)

print(*res_nums, sep = '')


