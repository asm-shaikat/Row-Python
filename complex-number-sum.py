class Complex():
        def initComplex(self):
            self.real = int(input('Enter real number: '))
            self.imag = int(input('Enter imag number: '))
        def display(self):
            print(self.real,"+",self.imag,"i")
        def sum(self,obj,obj1):
            self.real = obj.real+obj1.real
            self.imag = obj.imag+obj1.imag


obj = Complex()
obj1 = Complex()
obj2 = Complex()

print("Enter first complex  number")
obj.initComplex()
obj.display()

print("Enter second complex number")
obj1.initComplex()
obj1.display()

print("Sum of two complex numbers")
obj2.sum(obj,obj1)
obj2.display()