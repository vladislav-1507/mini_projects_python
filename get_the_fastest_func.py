#from datetime import datetime, timedelta
from time import perf_counter as pc, time as t

def calculate_it(func, *args):
    start_time = pc()
    res = func(*args)

    return res, pc() - start_time

def get_the_fastest_func(funcs, arg):
    min_count = float('inf')
    res_func = None
    for cur_func in funcs:
        res, cur_count = calculate_it(cur_func, arg)
        if cur_count < min_count:
            min_count = cur_count
            res_func = cur_func
    
    return res_func

def for_and_append(iterable):             # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result
        

def list_comprehension(iterable):         # с использованием списочного выражения
    return [elem for elem in iterable]    
    

def list_function(iterable):              # с использованием встроенной функции list()
    return list(iterable) 

iterable = range(100_000)
print(get_the_fastest_func((for_and_append, list_comprehension, list_function), iterable))