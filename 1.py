class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary

    def add(self, other):
        return ComplexNumber(self.real+other.real, self.imaginary+other.imaginary)

    def subtract(self, other):
        return ComplexNumber(self.real-other.real, self.imaginary-other.imaginary)

    def multiply(self, other):
        real=self.real*other.real-self.imaginary*other.imaginary
        imaginary=self.real*other.imaginary+self.imaginary*other.real
        return ComplexNumber(real,imaginary)

    def divide(self,other):
        denom=other.real**2+other.imaginary**2
        real=(self.imaginary*other.real+self.imaginary*other.imaginary)/denom
        imaginary=(self.imaginary*other.real-self.real*other.imaginary)/denom
        return ComplexNumber(real,imaginary)

    def display(self):
        print(f"{self.real}+{self.imaginary}i")


c1=ComplexNumber(4,3)
c2=ComplexNumber(2,1)

print("Addition")
c1.add(c2).display()

print("Subtraction")
c1.subtract(c2).display()

print("Multiplication")
c1.multiply(c2).display()

print("Division")
c1.divide(c2).display()

    

    
