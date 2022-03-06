import arrays
import random

def create_sorted_array_descending(size):
    array = arrays.Array(size, 0)
    count = size
    for i in range(len(array)):
        array[i] = count
        count -= 1
    return array

def random_int_array(size, min = 1, max = 10):
    rand_array = arrays.Array(size)
    for i in range(len(rand_array)):
        rand_array[i] = random.randint(min, max)
    return rand_array

def split(array):
    evens_index = 0
    odds_index = 0
    if len(array) % 2 == 1:
        evens = arrays.Array(len(array)//2 + 1)
        odds = arrays.Array(len(array)//2)
    else:
        evens = arrays.Array(len(array)//2)
        odds = arrays.Array(len(array)//2)
    for i in range(len(array)):
        if i % 2 == 0:
            evens[evens_index] = array[i]
            evens_index += 1
        else:
            odds[odds_index] = array[i]
            odds_index += 1
    return evens, odds

def merge(sorted1, sorted2):
    result = arrays.Array(len(sorted1) + len(sorted2))
    i1 = 0
    i2 = 0
    i = 0
    while i1 < len(sorted1) and i2 < len(sorted2):
        if sorted1[i1] <= sorted2[i2]:            
            result[i] = sorted1[i1]
            i1 += 1
            i += 1
        else:
            result[i] = sorted2[i2]
            i2 += 1
            i +=1
    if i1 < len(sorted1):
        while i1 < len(sorted1):
            result[i] = sorted1[i1]
            i1 += 1
            i += 1
    else:
        while i2 < len(sorted2):
            result[i] = sorted2[i2]
            i2 += 1
            i += 1
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        half1, half2 = split(array)
        half1 = merge_sort(half1)
        half2 = merge_sort(half2)
        merged_array = merge(half1, half2)
        return merged_array

def main():
    # array = create_sorted_array_descending(10)
    array = random_int_array(30, 1, 100)
    print(array)
    merged_array = merge_sort(array)
    print(merged_array)

main()