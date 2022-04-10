import node

class Stack:
    __slots__ = ["__size", "__top"]
    
    def __init__(self) -> None:
        self.__top = None
        self.__size = 0
    
    def size (self):
        return self.__size
    
    def is_empty (self):
        return self.__top == None
    
    def __str__(self, node):
        if node == None:
            return ''
        else:
            return str(node.get_value()) + ', ' + self.__str__(node.get_next())

    def print_stack(self):
        print(self.__str__(self.__top))

    def push (self, value):
        new_node = node.Node(value, self.__top)
        self.__top = new_node
        self.__size += 1

    def peek (self):
        return self.__top.get_value()

    def pop (self):
        value = self.__top.get_value()
        self.__top = self.__top.get_next()
        self.__size -= 1
        return value

def main():
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    print("Stack size is: ", stack.size())
    stack.print_stack()
    node = stack.pop()
    print("Stack size is: ", stack.size())
    print("Node popped:", node)
    stack.print_stack()

if __name__ == "__main__":
    main()
