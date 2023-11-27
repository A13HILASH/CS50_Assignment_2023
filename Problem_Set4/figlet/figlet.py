#Import neccessary modules.
import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

#Get command line argument.
userip=sys.argv[1:]

#If len of argument is>2 then exit.
if len(userip)>2:
     sys.exit("Invalid usage")

#Check if length of argument is 0.
elif len(userip)==0:

#If length is 0,Get user input and print it in random format.
    name=input("Input: ")

#Setting random font from list of of font using choice function.
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(name))

#Check if first string is '-f' or '--f'.
elif (userip[0]=='-f' or userip[0]=='--f'):

#Check if second string is in list of fonts and  print it in demanded format.   
    if  userip[1] in figlet.getFonts():
            name=input("Input: ")
            figlet.setFont(font=userip[1])
            print(figlet.renderText(name))

#If none of above condition is satisfied then exit.
    else:
         sys.exit("Invalid usage")
else:
     sys.exit("Invalid usage")        
            
            
    

           

        
        