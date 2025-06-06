with open('goats.txt',) as input_file, open('answer.txt', 'w') as output_file:
    content = [line.strip() for line in input_file.readlines()]
    if 'COLOURS' and 'GOATS' in content:
        c_index = content.index('COLOURS')
        g_index = content.index('GOATS')
    colours_list = content[c_index+1:g_index]
    goats_list = content[g_index+1:]
    count_of_goats = len(goats_list) * 0.07
    dict_of_goats = {}
    for goat in colours_list:
        dict_of_goats[goat] = goats_list.count(goat)
    for goat, count in sorted(dict_of_goats.items()):
        if count > count_of_goats:
            output_file.write(goat + '\n')

'''"Были разноцветные козлы. Сколько?"

"Сколько чего?"

"Сколько из них составляет более 7% от общего количества козлов?"'''