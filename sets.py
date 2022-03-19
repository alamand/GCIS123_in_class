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
    empty_set = set()
    return set1, set2, empty_set

def print_set(set):
    for value in set:
        print(value)

def unique_set(a_set, value):
    if value not in a_set:
        a_set.add(value)

def unique_words(filename):
    a_set = set()
    with open(filename) as file:
        for line in file:
            words = line.split()
            for word in words:
                a_set.add(word.lower())
    return a_set

def superset(a_set, b_set):
    for value in b_set:
        if not(value in a_set):
            return False
    return True

def subset(a_set, b_set):
    for value in a_set:
        if not(value in b_set):
            return False
    return True

def union(a_set, b_set):
    c_set = set()
    for value in a_set:
        c_set.add(value)
    for value in b_set:
        c_set.add(value)
    return c_set

def intersection(a_set, b_set):
    c_set = set()
    for value in a_set:
        if value in b_set:
            c_set.add(value)
    return c_set

def main():
    set1, set2, empty_set = create_set()
    print(empty_set)
    print_set(set1)
    print_set(set2)

    print(sorted(set2)) # non-destructive

    alice = unique_words("input.txt")
    # print(alice)

    a_set = {1,2}
    print(superset(set1, a_set)) # is set1 a superset of a_set?

    print(subset(set1, a_set))  # is set1 a subset of a_set?

    b_set = {'a', 'b'}
    u = union(set1, b_set)      # union of 2 sets
    print(u)

    i = intersection(a_set, set1)   # intersection: common elements kept
    print(i)

main()