phone_dict = {}
for _ in range(int(input())):
    cur_num, cur_name = input().split()
    phone_dict[cur_name] = phone_dict.get(cur_name, []) + [cur_num]        

for _ in range(int(input())):
    name_to_search = input().capitalize()
    if name_to_search in phone_dict:
        print(*phone_dict[name_to_search])
    else:
        print('абонент не найден')
