

import PersonTypes


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

    def __init__(self, students_in):
        self.students = students_in
        self.instructor = PersonTypes.Instructor("", "")

    def __init__(self):
        return

    def add_students(self, students_in):
        self.students = students_in

    def add_instructor(self, instructor_in):
        self.instructor = instructor_in

    # def __init__(self, hand_in):
    #     for tuple in hand_in:
    #         hand.add(card(tuple))

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

def send_email(email_address, text):
    print ('Email Sent, text: "' + text + '"')

def main():
    run_again_flag = True
    while (run_again_flag == True):
        Dylan = PersonTypes.Instructor('nimwit', 'dylan@typo.com')
        Sydney = PersonTypes.Student('Sydney Sommerfield', 'sydney@sommerfield.com', Dylan)
        Justin = PersonTypes.Student('Justin Tomlinson', 'justin@tomlinson.com', Dylan)
        Students = [Sydney, Justin]
        CurrentClass = Class_Roster(Students)
        print(Students)
        print(Dylan)
        print(CurrentClass)
        CurrentClass.send_class_intro_email()
        run_again = input('Run Again.')
        if run_again.lower() not in CONTINUE_PROCESSING_CHARACTERS:
            run_again_flag = False

if __name__ == '__main__':
    main()