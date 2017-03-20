
class Person (object):
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
    def __repr__(self):
        return ('Student(' + self.name + ',' + self.email_address + ')' )
    def __eq__(self, other):
        return ((self.name == other.name) and (self.email_address == other.email_address))

class Student (Person):
    def __init__(self, name, email_address, instructor_in):
        Person.__init__ (self, name, email_address)
        self.instructor = instructor_in
    def __repr__(self):
        return ('Student(' + self.name + ',' + self.email_address + ',' + str(self.instructor) + ' )' )
    def __eq__(self, other):
        return ((self.name == other.name) and (self.email_address == other.email_address)
                and self.instructor == other.instructor)

class Instructor (Person):
    def __init__(self, name, email_address):
        Person(self, name, email_address)
    def __repr__(self):
        return ('Instructor(' + self.name + ',' + self.email_address + ')' )

def main():
    dylan = Instructor('Dylan', 'ThatGuy@thatguy.com')
    print(repr(dylan))

if __name__ == '__main__':
    main()

