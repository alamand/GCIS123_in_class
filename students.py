class Students:
    ''' A class to represent students '''

    # id = "No ID"
    # name = "Student"
    # credits = 0
    # gpa = 0.0
    __slots__ = ['id', 'name', 'credits', 'gpa']

    def __init__(self, id , name) -> None:
        self.id = id
        self.name = name
        self.credits = 0
        self.gpa = 0.0

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_credits(self):
        return self.credits

    def get_gpa(self):
        return self.gpa

    def print_student(student):
        print(student.id, student.name, student.credits, student.gpa)

    def set_credits(self, credits):
        self.credits = credits

    def set_gpa(self, gpa):
        self.gpa = gpa

def main():
    st1 = Students(12345, "Mandy")
    st1.print_student()    
    st1.set_credits(100)
    st1.set_gpa(3.9)
    print(st1.get_id(), st1.get_name(), st1.get_credits(), st1.get_gpa())
    st2 = Students(56789, "Raj")

main()