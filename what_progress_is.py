import sys

def is_arifmetic_progress(seq):
    res = True
    for i in range(1, len(seq) - 1):
        if (seq[i - 1] + seq[i + 1]) / 2 != seq[i]:
            res = False
            break
    return res

def is_geometric_progress(seq):
    res = True
    for i in range(1, len(seq) - 1):
        if seq[i - 1] / seq[i] != seq[i] / seq[i + 1]:
            res = False
            break
    return res

data = list(map(int, sys.stdin))
possible_results = 'Арифметическая прогрессия', 'Геометрическая прогрессия', 'Не прогрессия'

if is_arifmetic_progress(data):
    res = possible_results[0]
elif is_geometric_progress(data):
    res = possible_results[1]
else:
    res = possible_results[2]

print(res)