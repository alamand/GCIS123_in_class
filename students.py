import course

class Students:
    ''' A class to represent students '''

    # id = "No ID"
    # name = "Student"
    # credits = 0
    # gpa = 0.0
    __slots__ = ['id', 'name', 'credits', 'gpa', 'courses']

    def __init__(self, id , name):
        self.id = id
        self.name = name
        self.credits = 0
        self.gpa = 0.0
        self.courses = []

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_credits(self):
        return self.credits

    def get_gpa(self):
        return self.gpa

    def print_student(self):
        print(self.id, self.name, self.credits, self.gpa)

    def set_credits(self, credits):
        self.credits = credits

    def set_gpa(self, gpa):
        self.gpa = gpa
    
    def add_course(self,course):
        self.courses += [course]
        self.credits += course.get_credits()
    
    def print_courses(self):
        for course in self.courses:
            print(course.name, course.credits, course.grade)

def main():
    st1 = Students(12345, "Mandy")
    st1.print_student()    
    st1.set_credits(100)
    st1.set_gpa(3.9)
    print(st1.get_id(), st1.get_name(), st1.get_credits(), st1.get_gpa())
    c1 = course.Course("GCIS123", 4, 89)
    st1.add_course(c1)    
    st1.print_courses()
    st2 = Students(56789, "Raj")

main()