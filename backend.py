from pdb import set_trace
from re import match, search
from sys import *
# from Interface import *



class SubjectDetails(object):
    def __init__(self, firstname, lastname, phonenumber, email):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.email = email

    def getFirst(self):
        return self.firstname

    def getLast(self):
        return self.lastname

    def getPhone(self):
        return self.phonenumber

    def getEmail(self):
        return self.email

def name_check():
    #set_trace()
    x = input() or "empty"
    if x is not "empty" and match('[A-z]+', x):
        return x
    elif x is not "empty" and not match(r'[A-z]+', x):# == False:
        return "invalid"
    else:
        return

def phone_check():
    x = input()
    if x is not None and match(r'\d+', x):
        return x
    elif x is not None and not match(r'\d+', x):
        return "invalid"
    else:
        return

def email_check():
    x = input()
    if x is not None and match(r'.+@.+\.com', x):
        return x
    elif x is not None and not match(r'.+@.+\.com', x):
        return "invalid"
    else:
        return


