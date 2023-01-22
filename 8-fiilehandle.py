#fhandle=open("abc.txt") #default mode read r

fhandle=open("abc.txt","r") #r-read is the mode (optional)

fcontents=fhandle.read()

print(fcontents)

fhandle.close()


#read line by line
fhandle=open("abc.txt")
print(fhandle.readline())
print(fhandle.readline())
print(fhandle.readline())

#writing to a file in pyton
fhandle=open("abc.txt","w") #w-write
my="Python is great \n no its not"
fhandle.write(my)
fhandle.close()
