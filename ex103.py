class Person():

    def __init__(self, name):
        """Assumes name a string. Create a person"""
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank+1:]
        except:
            self._last_name = name
        self.birthday = None
    
    def get_name(self):
        """Returns self's full name"""
        return self._name
    
    def get_last_name(self):
        """Returns self's last name"""
        return self._last_name
    
    def set_birthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
           Sets self's birthday to birthdate"""
        self._birthday = birthdate

    def get_age(self):
        """Returns self's current age in days"""
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days


    def __lt__(self, other):
        """Assume other Person
           Returns True if self precedes other
           in alphabetical order, and False
           otherwise. Comparison is based on
           last names, but if these are the
           same full names are compared."""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name

    def __str__(self):
        """Returns self's name"""
        return self._name

class MIT_person(Person):

    _next_id_num = 0 #identification number

    def __init__(self, name):
        super().__init__(name)
        self._id_num = MIT_person._next_id_num
        MIT_person._next_id_num += 1

    def get_id_num(self):
        return self._id_num

    def __lt__(self, other):
        return self._id_num < other._id_num

    def is_student(self):
        return isinstance(self, Student)

class Politician(Person):
    """A politician is a person who can belong to a political party"""
    def __init__(self, name, party=None):
        """name and party are strings"""
        super().__init__(name)
        self.party = party
    def get_party(self):
        """returns the party to which self belongs"""
        return self.party
    def might_agree(self, other):
        """returns True if self and other belong to the same party
           or at least one of them does not belong to a party"""
        if self.get_party() and other.get_party():
            return self.get_party() == other.get_party()
        else:
            return True

p1 = Politician("TJ", "Democrat")
p2 = Politician("JM", "Democrat")
p3 = Politician("AH", "Federalist")
p4 = Politician("NP")

print("p1 to p2", p1.might_agree(p2))
print("p1 to p4", p1.might_agree(p4))
print("p1 to p3", p1.might_agree(p3))

class Student(MIT_person):
    pass

class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self._year = class_year
    def get_class(self):
        return self._year

class Grad(Student):
    pass

class Transfer(Student):
    def __init__(self, name, from_school):
        MIT_person.__init__(self, name)
        self._from_school = from_school


ug1 = UG("Gus", 1988)
ug1.is_student()


class Dog:
    def __init__(self, name):
        self._name = name

class Grades():

    def __init__self(self):
        """Create empty grade book"""
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        pass

    def add_grade(self, student, grade):
        pass

    def get_grades(self, student):
        pass

    def get_students(self):
        pass
