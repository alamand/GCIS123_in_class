def create_lists():
    list0 = []
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]
    list3 = ["Hello", False, 5.5, 'a']
    list4 = list("abcd")
    return list1, list2, list3, list4

def print_list(list_name, list):
    print("Length: ", len(list))
    print(list_name)
    for i in range(len(list)):
        # print("element[", i, "]: ")
        print(list[i])

def change_list(list):
    for i in range(len(list)):
        list[i] = list[i] + 10

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

    # extend/grow original list
    list3 += ["World", "2022!"]
    print_list("list3 extended", list3)

    # permanently remove from list using pop, size automatically decremented
    list3.pop()
    print_list("list3 removed last element", list3)

    list3.pop(0)
    print_list("list3 removed first element", list3)

    value = list3.pop(2)
    print_list("list3 removed element in the middle", list3)
    print("element removed: ", value)

    # permanently insert into the list using insert, size automatically incremented
    list3.insert(1, 99)
    print("value inserted into index 1: ", list3)

    # inserting at index beyond length places the element last
    list3.insert(10, 99)
    print("value inserted into index 10: ", list3)
    
main()