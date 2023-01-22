a=input("Enter your name ") 

print("Your name is "+a)  # .a or +a both works

#a=int(a) #to chnage the data type of a. str to int # but input has to be a int

print(type(a))

#seperator
print(1,2,3,4, sep="-")

print(1,2,3,4, sep="*",end="#")

b=1 
c=2
print("\nb is {} and c is{} ".format(1,2))
print("b is {1} and c is{0} ".format(1,2))

str(input("Enter a number:"))  
int(input("Enter a number:"))   #default str ganne. eka nisa print(a+b) karoth function weda na. ee nisa int kranna numbers--____--

a = input("Enter number 1: ")
b = input("Enter number 2: ") 
print(a+b)