import random


def main():
#Get level from get_level().
    level=get_level()
#Set counter for score.
    flag=0
#Start outer loop for 10 problems.
    for x in range(10):
#Set counter for 3 chance in case of entering wrong answer.
        count=0
#Get 2 random number from generate_integer().
        num1,num2=generate_integer(level)
#Start inner loop.
        while True:
            ans=num1+num2
            try:
#Output answer if wrong answer entered 3 times.
                if(count==3):
                    print(f"{num1} + {num2} = {ans}")
                    break
#Get answer from user.
                sum=int(input(f"{num1} + {num2} = "))
#Increment counter for chance.
                count+=1
                if (sum==ans):
#Increment counter for score.
                    flag+=1
                    break
                else:
                    raise ValueError
            except ValueError:print("EEE")
#Print score.
    print(f"Score: {flag}")


def get_level():

#Start loop.
    while True:
        try:

#Get level from user.
            lvl=int(input("Level: "))

#Reprompt if level not 1,2 or 3 by raising exception.
            if(lvl<=0 or lvl>3):
                raise ValueError
#Return level.
            else:return(lvl)

        except:
            pass




def generate_integer(level):
#If level=1,set upper limit=9 and lower limit =0.
    if(level==1):
        upr_limit=9
#Return 2 random num.
        return(random.randint(0,upr_limit),(random.randint(0,upr_limit)))

#If level=1,set upper limit=99 and lower limit =10.
    elif(level==2):
        upr_limit=99
#Return 2 random num.
        return(random.randint(10,upr_limit),(random.randint(10,upr_limit)))

#If level=1,set upper limit=999 and lower limit =100.
    else:
        upr_limit=999
#Return 2 random num.
        return(random.randint(100,upr_limit),(random.randint(100,upr_limit)))



if __name__ == "__main__":
    main()