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

def array_cat(array1, array2):
    cat_array = arrays.Array(len(array1) + len(array2), 0)
    index = 0
    for i in range(len(array1)):
        cat_array[index] = array1[i]
        index += 1    

    for i in range(len(array2)):
        cat_array[index] = array2[i]
        index += 1    
    return cat_array    

def partition(pivot, array):
    less_count = 0
    same_count = 0
    more_count = 0
    for index in range(len(array)):
        if array[index] < pivot:
            less_count += 1
        elif array[index] > pivot:
            more_count += 1
        else:
            same_count += 1
    
    less = arrays.Array(less_count, 0)
    same = arrays.Array(same_count, 0)
    more = arrays.Array(more_count, 0)
    index_less = 0
    index_same = 0
    index_more = 0
    for i in range(len(array)):
        if array[i] < pivot:
            less[index_less] = array[i]
            index_less += 1
        elif array[i] > pivot:
            more[index_more] = array[i]
            index_more += 1
        else:
            same[index_same] = array[i]
            index_same += 1
    return less, same, more

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less, same, more = partition(pivot, array)
        new_array = array_cat(quicksort(less), same)
        new_array = array_cat(new_array, quicksort(more))
        return new_array

def main():
    array = create_sorted_array_descending(10)
    print("descending array: ", array)
    rand_array = random_int_array(5)
    print("random array: ", rand_array)    
    # less, same, more = partition(array[0], array)
    # print("less array: ", less)
    # print("same array: ", same)
    # print("more array: ", more)
    cat_array = array_cat(array, rand_array)
    print("joined array: ", cat_array)
    sorted_array = quicksort(array)
    print("sorted array: ", sorted_array)
main()