import course

class Students:
    ''' A class to represent students '''

    __slots__ = ['__id', '__name', '__total_credits', '__gpa', '__courses']

    def __init__(self, id , name):
        self.__id = id
        self.__name = name
        self.__total_credits = 0
        self.__gpa = 0.0
        self.__courses = []
    
    def __str__(self):
        return str(self.__id) + " " + self.__name + " " + str(self.__total_credits) + " " + str(self.__gpa)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.__id == other.__id

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_total_credits(self):
        return self.__total_credits

    def get_gpa(self):
        return self.__gpa

    def print_student(self):
        print(self.__id, self.__name, self.__total_credits, self.__gpa)

    def set_total_credits(self, credits):
        self.__total_credits = credits

    def set_gpa(self, gpa):
        self.__gpa = gpa
    
    def add_course(self,course):
        self.__courses += [course]
        self.__total_credits += course.get_credits()
    
    def print_courses(self):
        for course in self.__courses:
            print(course.get_name(), course.get_credits(), course.get_sectionNum())
    
def main():
    st1 = Students(12345, "Mandy")
    st1.print_student()
    # Students.print_student(st1)   # equivalent to line above
    st1.set_gpa(3.9)
    print(st1.get_id(), st1.get_name(), st1.get_total_credits(), st1.get_gpa())
    c1 = course.Course("GCIS123", 4, 89)
    st1.add_course(c1)
    c2 = course.Course("GCIS124", 4, 99)
    st1.add_course(c2)   
    st1.print_courses()
    print("Total credits: ", st1.get_total_credits())
    print(st1)                      # test __str function
    st2 = Students(56789, "John")
    print(st1 == st2)               # comparing students for equality based on student id
main()