print("Hello")

x=min(5,10)
print(x)

y=max(5,10)
print(y)

#defined functions
def greet(name):
    "Greet a person with name "
    print("Heloo, ",name)    
    return

greet("AA");
greet("BB"); # ; after the code also works--__--

#If you do not know how many arguments that will be passed into your function, add an asterisk (*) before the parameter name in the function definition

def greet(*names):
    for name in names:
             print("Hello", name)

greet("Jane", "Monica", "Joe", "Andrew")

#
def add(a, b):
    return a+5, b+5
print(add(3, 2))