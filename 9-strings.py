word="Help"+'A' 
print(word) #HelpA 0,1,2,3,4

x=word*5 # + , both same
print(x)

print(word[4]) #A

print(word[0:2]) #He

print(word[2:4]) #lp

print(word[-1]) #A

print(word[-2]) #p

print(word[-2:]) #pA

print(word[-3:-1]) #lp

#word[0]="g" type error. cant update strings like int
#just concat
woord="HelpA"
print('x'+woord[1:]) #xHelpa

print('x'+woord[4]) #xA

#len() length of a string
a="Hello"
print(len(a)) #5

print("H" in woord)  #true
print("Z" in woord)  #false