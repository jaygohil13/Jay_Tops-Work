"""
1) Hierarchical inheritance :
 
           A
           |
           V
    -----------------
    |               |
    B               C



"""
class person: # Parent Class :
    def input(self,fname,subject):
        self.fname = fname
        self.subject = subject

class faculty(person): # Child Class :
    def display(self):
        print("fname = ",self.fname)
        print("subject = ",self.subject)

class student(person): # Child Class z;
    def display(self):
        print("fname = ",self.fname)
        print("subject = ",self.subject)

f = faculty()
f.input("Jay","Python")

s = student()
s.input("Kaushal","Python")

f.display()
s.display()