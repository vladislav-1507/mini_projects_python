def size_counter(dict_values):
    total = 0
    for el in dict_values:
        if el[2] == 'KB':
            total += int(el[1]) * 1_024
        elif el[2] == 'MB':
            total += int(el[1]) * 1_048_576
        elif el[2] == 'GB':
            total += int(el[1]) * 1_073_741_824
        else:
            total += int(el[1])
    if total < 1_024:
        res = f'Summary: {total} B'
    elif 1_024 <= total < 1_048_576:
        res = f'Summary: {round(total/1_024)} KB'
    elif 1_048_576 <= total < 1_073_741_824:
        res = f'Summary: {round(total/1_048_576)} MB'
    else:
        res = f'Summary: {round(total/1_073_741_824)} GB'
    
    return res

with open('files.txt', encoding='utf-8') as file:
    list_of_files = [line.strip().split() for line in file.readlines()]
    dict_of_files = {}
    for el in list_of_files:
        extention = el[0].split('.')[1]
        dict_of_files.setdefault(extention, []).append((el[0], el[1], el[2]))
    
for k, v in sorted(dict_of_files.items()):
    for el in sorted(v, key=lambda x: x[0]):
        print(el[0])
    print('----------')
    print(size_counter(v), end='\n\n')