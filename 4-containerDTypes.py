#python container data types- list,tuple,range,set

#LIST
list_1=[1,2,3,'apple',"orange",'d'] #0,1,2,3,4,5,6
print(list_1)
print("4th index: ",list_1[4])

#add value to end of list
list_1.append(60)
print(list_1)

#modify a value to specific index
list_1[2]=70
print(list_1)

#delete value
list_1.remove('apple')
print(list_1)
del list_1[5] #index number
print(list_1)

#MultiDimentional LISTS
data=[[1,1,1],[2,2,2],[3,3,3]] #0,1,2 rows and 0,1,2, columns
print(data)
print(data[1][1])

data[1][1]=25
print(data)

data[1].append(5)
print(data)

#List operations
#Length
print(len(list_1))
#concatenation
a=[1,2,3]
b=[4,5,6]
print(a+b)
#repetition
print(['HI']*5)
#Membership
print(3 in [1,2,3]) #check if value available
#iteration
for x in[1,2,3]:
        print(x)

#Negative indices
L=['a','b','c'] #0,1,2 #-3,-2,-1
print(L[2])#c
print(L[-2])#b
print(L[1:])#bc  #1 and 2 indexes

num = [13, 16, 55, 43, 76]
print(num[1:4])
print(num[2:])