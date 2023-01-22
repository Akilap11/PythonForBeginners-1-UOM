print("Hello World")
print (123)

x=5 #assignment statement
x=x+5  #assignment with statement
print(x)  #print statement

#numeric operations + - * / //(floor division-no decimal) % **power 

y=1+2**3/4*5
#paranthesis->Power->Multiply/divition->Addition/subtract->left to right
print(y) #11.0

q=2+1*(8-3)
print(q)

name=input("enter your name: ")
print(name)
greeting="welcome"
print("greeting {}".format(name))

#data types
#int, float, complex(complex numbers), bool(sub type of int), str,
#compound data types(basic data structures)
#list,tuple,dict,set  

p="abc"+'xyz'
print(p)
print(type(p)) #class 'str'

o=64
print(type(o)) #class 'int'      float, bool, 

c=10>5
print(c) #true

#i,j complex data types 2+5j

#variable names are case sensitive, can start with _

#value can change-mutable (numbers,strings,tuples,sets)
#value cannot change-immutable (lists,dictionaries)

n=88
print(id(n))
m=n
print(id(m))
n=80
print(id(n))
print(id(m))
#id of n chamges. not m. gbecause its mutable

t="abcxyz"
print(t[2]) #c

print (type("10.5")) #this is a string because of the quotations

_age="d"
print(_age)

agee=20
print(id(agee))
agee=21
print(id(agee))

v=5
b=10
z=0.0
print(bool(x==y),bool(x))