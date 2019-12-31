import random
import time
correct = int(random.random()*100)
print("Welcome to (Say it with me)GUESS THAT NUMBER THINGYMAJIGA")
for i in range(0,10):
    print ("Please input your guess(numbers)you have",11-i-1,"more guess(es):",end="")
    b=(int)(input())
    if b!=correct:
        fail=1
        if b>correct:
            print("The number is lower than",b) 
        else:
            print("The number is higher than",b)        
        if 1==9:
            print("YOU LOSE")
    else:
        print("CONGRATS")
        fail=0
        break
if fail==1:
    print("YOU LOSE")
    print("The answer was",correct)
    e = int(random.random()*100)
    print("you could of won $",e)
else:
    print("YOU WIN")
    print("The answer was",correct)
    print("Please wait the wheel is spinning how much money you won(3 sec)")
    a = int(random.random()*100)
    time.sleep(3)
    print("you won $",a)
    