n_10 = int(input())

def boh(num):
    num_bin = bin(num)
    num_oct = oct(num)
    num_hex = hex(num)
    
    return [num_bin[2:], num_oct[2:], num_hex[2:].upper()]
    
print(*boh(n_10), sep = '\n')