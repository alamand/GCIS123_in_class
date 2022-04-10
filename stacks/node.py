class Node:
    __slots__ = ['__value', '__next']

    def __init__ (self, value, next = None):
        self.__value = value
        self.__next = next

    def get_value (self):
        return self.__value

    def get_next (self):
        return self.__next

def print_node (node_seq):
    if node_seq == None:
        print (end = '')
    else:
        print (node_seq.get_value (), end = ', ') 
        print_node (node_seq.get_next ())

def main():
    sequence_of_one = Node ('a', None)              # tail
    sequence_of_two = Node ('b', sequence_of_one)
    sequence_of_three = Node ('c', sequence_of_two) # top

    print_node(sequence_of_three)

if __name__ == "__main__":
    main()
