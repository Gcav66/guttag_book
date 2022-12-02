class Grades:

    def __init__(self):
        """Create empty grade book"""
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        #if student in self._students:
            #raise ValueError('Duplicate student')

        self._is_sorted = False

ug1 = "Gus"
foo = Grades()
foo.add_student(ug1)

class info_hiding:
    def __init__(self):
        self.visible = 'Look at me'
        self.__also_visible__ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directly'

    def print_visible(self):
        print(self.visible)

    def print_invisible(self):
        print(self.__invisible)

    def __print_invisible(self):
        print(self.__invisible)

    def __print_invisible__(self):
        print(self.__invisible)

class Sub_class(info_hiding):
    def new_print_invisible(self):
        print(self.__invisible)

test = info_hiding()
print(test.visible)
print(test.__also_visible__)
#print(test.__invisible)
test.print_invisible()
test.__print_invisible__()
#test.__print_invisible()

test_sub = Sub_class()
test_sub.new_print_invisible()