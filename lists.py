def create_lists():
    list0 = []
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]
    list3 = ["Hello", False, 5.5, 'a']
    list4 = list("abcd")
    return list1, list2, list3, list4

def print_list(list_name, list):
    print("list", list)
    print("Length: ", len(list))
    print(list_name)
    for i in range(len(list)):
        # print("element[", i, "]: ")
        print(list[i])

def change_list(list):
    for i in range(len(list)):
        list[i] = list[i] + 10

def make_table(rows, columns, value):
    table = [[] for _ in range(rows)]
    for row in table:
        row += [value for _ in range(columns)]
    
    # assign value to table element, first slot
    table[0][0] = 10

    #last slot
    table[rows-1][columns-1] = 100
    
    return table

def test_slicing():
    list5 = list("Hello World")

    # copy
    list6 = list5[:]
    print_list("list6 copy of list5", list6)
    # first word
    list6 = list6[:5]
    print_list("list6 first word", list6)
    # last word
    list6 = list5[6:]
    print_list("list6 last word", list6)
    # reverse string
    list6 = list5[::-1]
    print_list("reverse of list5", list6)
    # steps
    list6 = list5[:5:2]
    print_list("steps of list5", list6)

def test_comprehension():
    # All of the letters in the string “foobar”
    string = "foobar"
    list3 = [char for char in string]
    print(list3)

    # 15 0s
    list2 = [0 for _ in range(1, 15)]
    print(list2)

    # integers between 0 and 12
    list0 = [i for i in range(0, 13)]
    print(list0)

    # even integers between 0 and 20
    list1 = [i for i in range(0, 21, 2)]
    print(list1)
    
    # integers less than 50 divisible by 3 or 5
    list4 = [i for i in range(0, 51) if i % 3 == 0 or i % 5 == 0]
    print(list4)

    

def main():    
    list1, list2, list3, list4 = create_lists()
    print_list("list4", list4)
    change_list(list1)
    print_list("list1", list1)

    # adds value at the back
    list1.append(5)
    print_list("list1 after appending", list1)

    # + to join lists, original lists unchanged
    new_list = list1 + list2
    print_list("joined list: ", new_list)

    # TypeError below: can only use + with list types
    # new_list = list1 + 4
    new_list = list1 + [4]
    print_list("new list: ", new_list)

    # extend/grow original list
    list3 += ["World", "2022!"]
    print_list("list3 extended", list3)

    # permanently remove from list using pop, size automatically decremented
    list3.pop() #last element
    print_list("list3 removed last element", list3)

    list3.pop(0)    # first element
    print_list("list3 removed first element", list3)

    value = list3.pop(2) # element at specific index
    print_list("list3 removed element in the middle", list3)
    print("element removed: ", value)

    # permanently insert into the list using insert, size automatically incremented
    list3.insert(1, 99)
    print("value inserted into index 1: ", list3)

    # inserting at index beyond length places the element last
    list3.insert(10, 99)
    print("value inserted into index 10: ", list3)
    
    print_list("list1 before sorting", list1)
    print(sorted(list1))

    list1.sort()
    print_list("list1 sorted", list1)

    #slicing
    test_slicing()

    #comprehension
    test_comprehension()

    # 2D lists (table of 5 rows, 10 columns filled with 0s)
    table = make_table(5, 10, 0)
    print(table)

main()