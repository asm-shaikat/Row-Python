class Subtraction():
    def getInput(self):
        self.real  = int(input("Enter the real number:"))
        self.imag = int(input("Enter the imag number:"))
    def display(self):
        print("Complex number:",end=" ")
        print(self.real,"+",self.imag,"i")
    def sub(self,obj,obj1):
        print("Subtraction of complex number: ")
        self.real = obj.real - obj1.real
        self.imag = obj.imag - obj1.imag
obj = Subtraction()
obj1 = Subtraction()
obj2 = Subtraction()

print("Enter first complex number")
obj.getInput()
obj.display()

print("Enter second complex number")
obj1.getInput()
obj1.display()

obj2.sub(obj,obj1)
obj2.display()