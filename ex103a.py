import datetime

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

        
    def __str__(self):
        """Returns self's name"""
        return self._name

me = Person('Gus Cavanaugh')
him = Person('Jon Bon Jovi')
her = Person('Rihanna')
print(him.get_last_name())
him.set_birthday(datetime.date(1961, 8,4))
her.set_birthday(datetime.date(1968, 8, 16))
print(him.get_name(), 'is', him.get_age(), 'days old')

pList = [me, him, her]
for p in pList:
    print(p)

pList.sort()
for p in pList:
    print(p)