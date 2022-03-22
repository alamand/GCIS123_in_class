def create_dictionaries():
    dict1 = {}
    dict2 = dict()
    dict3 = {"sid":12345, "name": "Mandy", "GPA": 3.5}
    return dict1, dict2, dict3

def change_dictionary(dict):
    dict["GPA"] = 4.0
    dict["age"] = 20
    dict["age"] = 26    #replaces age

def print_dictionary(dict):
    print("Length: ", len(dict))
    for key in dict:
        print(key, ":", dict[key], end=" ")
        print()
    # if "GPA" in dict:
    #     print(dict["GPA"])

def main():
    d1, d2, d3 = create_dictionaries()
    change_dictionary(d3)
    print(d3)
    # print(d3["credits"])      # KeyError! Use an if statement to check that the key exists
    print_dictionary(d3) # ordered but not sorted
    # print(sorted(d3))

main()