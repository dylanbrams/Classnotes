

CONTINUE_PROCESSING_CHARACTERS = ['y', 'Y']
class Class_Roster (object):
    def __init__(self, students_in, instructor_in):
        """
        >>> x = Class_Roster([Student('Sydney Sommerfield', 'sydney@sommerfield.com')], Instructor('nimwit', 'dylan@typo.com'))
        >>> x.__repr__()
        'Class_Roster([Student(Sydney Sommerfield,sydney@sommerfield.com)], Instructor(nimwit,dylan@typo.com))'

        :param students:
        :param instructor:
        """
        self.students = students_in
        self.instructor = instructor_in

    def __repr__(self):
        # return 'AddressBookEntry({!r}, {!r})'.format(
        #     self.name,
        #     self.phone_number)
        #return ('Class_Roster(' + str(self.students) + ',' + str(self.instructor))
        return('Class_Roster({!r}, {!r})'.format(
            self.students,
            self.instructor
        ))

    def send_class_intro_email(self):
        text = ''
        for curr_student in self.students:
            text += 'In the class there is: ' + curr_student.name + '\n'
        text +=  'The instructor is: ' + self.instructor.name
        for curr_student in self.students:
            send_email(curr_student.email_address, text)
        send_email(self.instructor.email_address, text)

class Student (object):
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
    def __repr__(self):
        return ('Student(' + self.name + ',' + self.email_address + ')' )
    def __eq__(self, other):
        return ((self.name == other.name) and (self.email_address == other.email_address))

class Instructor (object):
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
    def __repr__(self):
        return ('Instructor(' + self.name + ',' + self.email_address + ')' )

def send_email(email_address, text):
    print ('Email Sent, text: "' + text + '"')

def main():
    run_again_flag = True
    while (run_again_flag == True):
        Sydney = Student('Sydney Sommerfield', 'sydney@sommerfield.com')
        Justin = Student('Justin Tomlinson', 'justin@tomlinson.com')
        Dylan = Instructor('nimwit', 'dylan@typo.com')
        Students = [Sydney, Justin]
        CurrentClass = Class_Roster(Students, Dylan)
        print(Students)
        print(Dylan)
        print(CurrentClass)
        CurrentClass.send_class_intro_email()
        run_again = input('Run Again.')
        if run_again.lower() not in CONTINUE_PROCESSING_CHARACTERS:
            run_again_flag = False
if __name__ == '__main__':
    main()