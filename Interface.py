
from pdb import set_trace
from backend import SubjectDetails, name_check, phone_check, email_check
from sys import *


def main():
    set_trace()
    def whatis(info):
        print('If known, enter the target\'s %s:' % info)

    def invalidentry(error_message):
        n = 'That is not a valid '
        name = n + 'name may not contain numbers or special character.'
        phone = n + 'phone number. Please enter a ten digit phone number with no spaces or special characters.'
        email = n + 'email address. Please enter a valid email address.'
        if error_message == 'name':
            print(name)
            name_check()
        elif error_message == 'phone':
            print(phone)
            phone_check()
        elif error_message == 'email':
            print(email)
            email_check()

#    def entry():
#        x = input()
#        while x is not None:
#            return x
#        else:
#            return argv

    def entry(check, error_message):
        if check is not None and check is not "invalid":
            return check
        elif check == 'invalid':
            invalidentry(error_message)
        else:
            return

    def f(*argv):
        whatis('first name')
        #set_trace()
        return entry(name_check(), 'name')

    def l(*argv):
        whatis('last name')
        return entry(name_check(), 'name')

    def p(*argv):
        whatis('phone number')
        return entry(phone_check(), 'phone')


    def e(*argv):
        whatis('email address')
        return  entry(email_check(), 'email')

    subject = f()
    subject = SubjectDetails(subject, l(), p(), e())

    SubjectDetails.getFirst(subject)

    print(subject.getLast())
    print(vars(subject))
main()


#--------------------- To Do ------------------------
# modify email_check() regex to allow .net, .info, etc.
# collapse all checks into one function
# make name input and check intelligent
