
print("Please input a number :",end=" ")
b=(int)(input())

for _ in range(b):
    print("*",end=" ")
print("") 

for _ in range(b-2): 
    print("*",end=" ")
    for _ in range(b-2):
        print(" ",end=" ")
    print("*")
    
for _ in range(b):
    print("*",end=" ")
print('\n')    
