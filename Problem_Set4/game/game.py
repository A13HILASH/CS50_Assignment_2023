import random
#Start outer loop.
while True:
#Set flag to stop outer loop.
    flag=0

    try:
#Get level from user.
        lvl=int(input("Level: "))

#Raise exception if level<1.
        if(lvl<1):
            raise ValueError
        
#Generate random num between 1 and level.
        rand=random.randint(1,lvl)

#Start inner loop.
        while True:

            try:
#Get geuss from user.
                guess=int(input("Guess: "))

#Raise exception if guess<1.
                if(guess<1):
                    raise ValueError 
                
#If guess=random num set flag to 1(to kill outer loop) and break out of inner loop.
                if(guess==rand):
                    print("Just right!")
                    flag=1
                    break

#Reprompt if guess<random num, after neccessary o/p message.
                elif(guess<rand):
                    print("Too small!")

#Reporompt if guess>random num,after neccessary o/p message.
                elif(guess>rand):
                    print("Too large!")
            except:pass
            
#Kills outer loop. 
        if(flag==1):break
    except:
        pass