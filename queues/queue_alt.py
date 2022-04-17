class Queue:

    __slots__ = ['__front', '__back', '__size', '__list', '__capacity']

    def __init__ (self, capacity = 3):
        self.__list = [0 for value in range(capacity)]        
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
        loop_times = self.__size
        j = 1
        while j <= loop_times:
            string += str(self.__list[i]) + ", "
            if i == self.__capacity - 1:
                i = 0
            else:
                i += 1
            j += 1
            # i = (i+1) % len(self.__list)
        return string

    def enqueue (self, value):
        if self.__size == self.__capacity:            
            raise IndexError ("Cannot enqueue: queue is full!")
        self.__list [self.__back] = value
        if self.__back == self.__capacity - 1:
            self.__back = 0
        else:
            self.__back += 1
        # self.__back = (self.__back + 1) % len (self.__list)
        self.__size += 1

    def dequeue (self):
        if self.__size <= 0:
            raise IndexError ("Cannot dequeue from an empty queue")

        value = self.__list [self.__front]
        if self.__front == self.__capacity - 1:
            self.__front = 0
        else:
            self.__front += 1
        # self.__front = (self.__front + 1) % len (self.__list)
        self.__size -= 1
        return value
    
    def get_front(self):
        return self.__list[self.__front]

    def get_front_index(self):
        return self.__front

    def get_back(self):
        return self.__list[self.__back-1]

    def get_back_index(self):
        return self.__back

def main():
    queue = Queue(3)
    try:
        queue.enqueue('a')
        queue.enqueue('b')
        queue.enqueue('c')
        print("Front", queue.get_front())
        print("Front index", queue.get_front_index())
        print("Back", queue.get_back())
        print("Back index", queue.get_back_index())
        print(queue.size())
        print(queue)
        # value = queue.dequeue()
        # print("Value dequeued: ", value)
        # print(queue)
        # print("Front", queue.get_front())
        # print("Back", queue.get_back())
    except IndexError as e:
        print("An error occurred: ", e)
main()