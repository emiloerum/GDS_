class MyInfo:
    '''Class representing a linear regression model'''
    
    def __init__(self, firstname, lastname, age): #This is a constructor in python
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def print(self):
        '''print info'''
        str = "name: {0} {1}\nage: {2}".format(self.firstname, self.lastname, self.age) 
        print(str)

info = MyInfo("Barack", "Obama", 59)
info.print()
    