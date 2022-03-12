def print_tuple(tuple):
    print("Length: ", len(tuple))
    print("Tuple values: ")
    for i in range(len(tuple)):
        print(tuple[i])

def create_tuples():
    tuple_a = (1, 2, 3)
    tuple_b = ('a', 'b', 'c')
    tuple_c = (1, 'hi', 2.5, True, -1, "hello")
    tuple_d = tuple("abcde")
    tuple_e = ("Mon", "Tue", "Wed")
    return tuple_a, tuple_b, tuple_c, tuple_d, tuple_e

def main():    
    # tuple1, tuple2, tuple3, tuple4, tuple5 = create_tuples()
    tuple1, tuple2, tuple3, tuple4, tuple5 = create_tuples()
    print_tuple(tuple4)
    # tuple4[0] = 10    //immutable
    
    tuple6 = tuple("abc")
    # comparing tuple values
    print(tuple2 == tuple6)

    # comparing tuple instances to each other
    print(tuple2 is tuple6)

main()