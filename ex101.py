class Toy:
    def __init__(gus):
        gus._elems = []
    def add(gus, new_elems):
        """new_elems is a list"""
        gus._elems += new_elems
    def size(gus):
        return len(gus._elems)

print(type(Toy))
print(type(Toy.__init__), type(Toy.add), type(Toy.size))

t1 = Toy()
print(type(t1))
print(type(t1.add))
t2 = Toy()
print(t1 is t2) #test for object identity

print ("now consider...")


t1.add([3,4])
t2.add([4])
print ("print size of: ")
print(t1.size() + t2.size())

print("don't pass list")

t3 = Toy()
t3.add("foo")
print(t3.size())

print("try passing dict")

t4 = Toy()
t4.add({"foo": "bar"})
print(t4.size())

class Int_set():
    """An Int_set is a set of integers"""
    #Information about the implementation (not the abstraction):
      #Value of a set is represented by a list of ints, self._vals.
      #Each int in a set occurs in self._vals exactly once.

    def __init__(self):
        """Create an empty set of integers"""
        self._vals = set()

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self._vals:
            self._vals.add(e)
    
    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self._vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    
    def get_members(self):
        """Returns a list containing the elements of self._
           Nothing can be assumed about the order of the elements"""
        return self._vals[:]

    def __str__(self):
        """Returns a string representation of self"""
        if self._vals == []:
            return '{}'
        self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ','
        return f'{{{result[:-1]}}}'
    
    def union(self, other):
        """other is an Int_set
           mutates self so that it contains exactly the elements in self
           plus the elements in other"""
        return self._vals.union(other)