def window(window_size, lst):
    result = []
    for i in range(len(lst) - window_size + 1):
        result.append(tuple(lst[i:i + window_size]))
    return result
print(window(3, [1,2,3,4,5,6,7,8,9,0]))
