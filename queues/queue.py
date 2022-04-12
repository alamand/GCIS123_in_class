class Queue:

    __slots__ = ['__front', '__back', '__size', '__list', '__capacity']

    def __init__ (self, capacity = 3):
        self.__list = [0 for value in range(capacity)]
        print(self.__list)
        self.__front = 0
        self.__back = 0
        self.__size = 0
        self.__capacity = capacity

    def is_empty (self):
        return self.__size == 0

    def size (self):
        return self.__size
    
    def __str__(self) -> str:
        string = ""
        i = self.__front
        while i != self.__back:
            string += str(self.__list[i]) + ", "
            i = (i+1) % len(self.__list)
        return string

    def enqueue (self, value):
        if self.__size == self.__capacity:
            self.__resize()
            # raise IndexError ("Cannot enqueue: queue is full!")
        self.__list [self.__back] = value
        self.__back = (self.__back + 1) % len (self.__list)
        self.__size += 1

    def dequeue (self):
        if self.__size <= 0:
            raise IndexError ("Cannot dequeue from an empty queue")

        value = self.__list [self.__front]
        self.__front = (self.__front + 1) % len (self.__list)
        self.__size -= 1
        return value
    
    def get_front(self):
        return self.__list[self.__front]

    def get_back(self):
        return self.__list[self.__back-1]

    def __resize (self):
        new_list = [0 for value in range(len (self.__list) * 2 + 1)]
        self.__capacity = len (self.__list) * 2 + 1
        i = self.__front
        j = 0
        for _ in range (self.__size):
            new_list [j] = self.__list [i]
            i = (i + 1) % len (self.__list)
            j += 1

        self.__front = 0
        self.__back = j
        self.__list = new_list

def main():
    queue = Queue(3)
    try:
        queue.enqueue('a')
        queue.enqueue('b')
        queue.enqueue('c')
        queue.enqueue('d')
        print(queue.size())
        value = queue.dequeue()
        print("Value dequeued: ", value)
        print(queue)
        print("Front", queue.get_front())
        print("Back", queue.get_back())
    except IndexError as e:
        print("An error occurred: ", e)
main()