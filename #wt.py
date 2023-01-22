#for and else break--__--
numbers = [3,2,5,7,8]
count = 0
for number in numbers:
    count+=1
    if number==5:
        break
else:
    count=-1
print(count)

#idiota
num = 5
while (num !=0):
    num = num - 1 
    print(num)
    if (num == 2): 
        continue
    print ("Hello World!") 
