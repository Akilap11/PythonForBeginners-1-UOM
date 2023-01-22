#for
for counter in [1,2,3,4,5]:
    print("This is a loop:= ",counter)

#range()
print(list(range(5))) #0-4
print(list(range(5,10))) #5-9
print(list(range(0,10,3))) #0,3,6,9
print(list(range(-10,-100,30)))
print(list(range(100,105,3)))

for i in range(5):
    print("I will not")

total=0
for counter in range(0,101,2):
    total=total+counter
print('total= ',total)

#while
num=int(input("Enter how manyntime to repeat")) #dont type minus number--__--
while(num!=0):
    print("Hello World")
    num=num-1
print("End")

#nested loops
for x in range(0,5):
    for y in range(0,10):
        print("$ ",end='' )
    print('')

num1=2
while (num1>0):
    num2=2
    while (num2>0):
        print("Sri Lanka")
        num2=num2-1
    num1=num1-1

#break #continue #pass(when if not finished, just pass)

numbers = [3,2,5,7,8]
count = 0
for number in numbers:
    count+=1
    if number==5:
        break
else:
    count=-1
print(count)



num = 5
while (num !=0):
    num = num - 1 
    if (num == 2): 
        continue
    print ("Hello World!") 
