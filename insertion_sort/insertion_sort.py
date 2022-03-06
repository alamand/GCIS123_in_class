import arrays
import random
import time

def create_sorted_array_ascending(size):
    array = arrays.Array(size, 0)
    count = 1
    for i in range(len(array)):
        array[i] = count
        count += 1
    return array

def create_sorted_array_descending(size):
    array = arrays.Array(size, 0)
    count = 10
    for i in range(len(array)):
        array[i] = count
        count -= 1
    return array

def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def shift(array, index):
    if index == 0:
        return
    while array[index] < array[index -1]:
        swap(array, index, index-1)
        # print("array sorting in progress", array)
        index -= 1
        if index == 0:
            break

def insertion_sort(array):
    for i in range(len(array)):
        shift(array, i)

def random_int_array(size, min = 1, max = 10):
    rand_array = arrays.Array(size)
    for i in range(len(rand_array)):
        rand_array[i] = random.randint(min, max)
    return rand_array

def insertion_sort_timer(array):
    start_time = time.perf_counter()
    insertion_sort(array)
    end_time = time.perf_counter()
    diff = end_time - start_time
    print("it took: ", diff, " seconds to do the insertion sort")

def main():
    # array = create_sorted_array_ascending(10)
    # print(array)
    # # swap values at index 4 and 8
    # swap(array, 4, 8)
    # print(array)
    # array2 = create_sorted_array_descending(10)
    # print(array2)
    # shift(array2, 9)
    # print(array2)
    rand_array = random_int_array(10000, 1, 100)
    print("initial random array:", rand_array)
    # insertion_sort(rand_array)
    # print("final sorted array: ", rand_array)
    insertion_sort_timer(rand_array)
main()