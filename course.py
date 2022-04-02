class Course:
    __slots__ = ["name", "credits", "grade"]

    def __init__(self, name, credits, grade):
        self.name = name
        self.credits = credits
        self.grade = grade

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def get_grade(self):
        return self.__grade

    def set_grade(self,grade):
        self.__grade = grade

    def print_course(self):
        print("Course:  name=", self.name,  ", credits=", self.credits,
            ", grade=", self.grade)

def main():
    c1 = Course("Intro to Python", 4, 89)
    c1.print_course()
main()