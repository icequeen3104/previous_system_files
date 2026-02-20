class calculator:
    n = 10
    #default constructor
    def __init__(self, a, b):
        self.firstnum= a
        self.secondnum= b
        print("i am called automatically when the object created")

    def getdata(self): #This is a method (function inside a class)
                        #self refers to the current object
                        #Every non-static method must have self
        print("i am executing as method in class")

    def summation(self):
        return self.firstnum + self.secondnum

#obj = calculator()
#obj.getdata()
#print(obj.n)

obj1 = calculator(2,3)
obj1.getdata()
print(obj1.summation())
