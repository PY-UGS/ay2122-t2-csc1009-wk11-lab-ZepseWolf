
# Online Python - IDE, Editor, Compiler, Interpreter

def avg(a, b):
    return (a + b)/2

def course(i):
        switcher={
                "CSC1006":"Course 1006",
                "CSC1007":"Course 1007",
                "CSC1008":"Course 1008",
                "CSC1009":"Object-Oriented Programming",
                "CSC1010":"Course 1010",
             }
        return switcher.get(i,"Invalid input")

a = float(input('Enter 1st number: '))
b = float(input('Enter 2nd number: '))
c = input('Enter course: ')

         
print("Hello Glasgow!")
print("Average :" ,avg(a,b))
print("Course :" ,course(c))
for i in range(67,101,2):
    print(168-i);   
