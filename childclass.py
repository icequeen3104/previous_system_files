from oops import calculator

class ChildImpl(calculator):
    n2= 200

    def __init__(self):
        calculator.__init__(self, 2, 10)
    def getcompletedata(self):
        return self.n2 + self.n + self.summation()

obj = ChildImpl()
print(obj.getcompletedata())