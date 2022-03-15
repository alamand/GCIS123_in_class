def create_set():
    set1 = {1, 2, 3}
    set1.add(4)
    # no duplicates added
    set1.add(4)
    if 4 in set1:
        print("Found")
    else:
        print("Not found")

    set2 = set("Hello") # no duplicates
    return set1, set2

def print_set(set):
    for value in set:
        print(value)

def main():
    set1, set2 = create_set()
    print_set(set1)
    print_set(set2)

    print(sorted(set2))
main()