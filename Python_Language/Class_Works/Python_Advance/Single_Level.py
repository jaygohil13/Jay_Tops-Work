"""
1) single level inheritance :
      
           A
           |
        ----------  
           |
           B

"""

class person: # Parent Class :
    def input(self,fname,subject):
        self.fname = fname
        self.subject = subject

class faculty(person): # Child Class :
    def display(self):
        print("fname = ",self.fname)
        print("subject = ",self.subject)



f = faculty() # Here Object is called :
f.input("Jay","Python")

f.display() # Here display the class and object :
