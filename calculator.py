class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def adder(self):
        data = self.num1 + self.num2
        return data  

    def subtractor(self):
        data = self.num1 - self.num2 
        return data 

    def multiplier(self):
        data = self.num1 * self.num2 
        return data 

    def divider(self):
        data = self.num1 / self.num2 
        return data

    def clear(self):
        self.num1 = 0 
        self.num2 = 0 
        return self.num1, self.num2 


in1 = int(input('Enter 1st number: '))
in2 = int(input('Enter 2nd number: '))

cal = Calculator(in1, in2)
print("\n==========================================\n")
print("Added " + str(in1) + " + " + str(in2) + " : " + str(
    cal.adder()))
print("Subtracted " + str(in1) + " - " + str(in2) + " : " + str(
    cal.subtractor()))
print("Mutliplied " + str(in1) + " * " + str(in2) + " : " + str(
    cal.multiplier()))
print("Divided " + str(in1) + " / " + str(in2) + " : " + str(
    cal.divider()))
print("Cleared " + str(in1) + " and " + str(in2) + " : " + str(
    cal.clear()))
