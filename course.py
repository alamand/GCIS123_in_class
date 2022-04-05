class Course:
    __slots__ = ["__name", "__credits", "__sectionNum"]

    def __init__(self, name, credits, sectionNum):
        self.__name = name
        self.__credits = credits
        self.__sectionNum = sectionNum

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def get_grade(self):
        return self.__grade

    def set_sectionNum(self, sectionNum):
        self.__sectionNum = sectionNum

    def get_sectionNum(self):
        return self.__sectionNum

    def print_course(self):
        print("Course:  name=", self.__name,  ", credits=", self.__credits,
            ", grade=", self.__sectionNum)    

def main():
    c1 = Course("Intro to Python", 4, 89)
    c1.print_course()
main()