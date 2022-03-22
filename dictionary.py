def create_dictionaries():
    dict1 = {}
    dict2 = dict()
    dict3 = {"sid":12345, "name": "Mandy", "GPA": 3.5}
    return dict1, dict2, dict3

def change_dictionary(dict):
    dict["GPA"] = 4.0
    dict["age"] = 20
    dict["age"] = 26    #replaces age
    print(dict.get("age"))
    # dict.clear()

def print_dictionary(dict):
    print("Length: ", len(dict))
    
    # print keys and values
    for key in dict:
        print(key, ":", dict[key], end=" ")
        print()

    # print keys only
    list = dict.keys()
    print("Keys: ", list)

    # print values only
    list = dict.values()
    print("Values: ", list)

    # make a copy
    dict_copy = dict.copy()
    print("copy: ", dict_copy)

    # remove an items using the key to identify it
    removed = dict.pop("age")
    print("age removed: ", dict)

    # check if the key exists before printing it
    if "age" in dict:
        print(dict["age"])

def main():
    d1, d2, d3 = create_dictionaries()
    change_dictionary(d3)
    print(d3)
    # print(d3["credits"])      # KeyError! Use an if statement to check that the key exists
    print_dictionary(d3) # ordered but not sorted
    # print(sorted(d3))  # only sorts the keys

main()