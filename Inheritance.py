class student:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def getdata(self):
        print('Accepting Data')
        self.name = input("Enter your name")
        self.contact = input("Enter Contact")

    def putdata(self):
        print('this is the name:' + self.name, 'this is contact:' + self.contact)


class sciencestudent(student):

    def __init__(self,age):
        self.age = age

    def science(self):
        print('I am science Student')


rob = sciencestudent(20);
rob.science()
rob.getdata()
rob.putdata()