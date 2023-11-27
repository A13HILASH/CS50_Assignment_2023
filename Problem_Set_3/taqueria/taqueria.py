# Declare dict of menu.
menu={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
#Initialize bill to 0.
bill=0

#Start loop.
while True:
 
#Try,except for KeyError-pass and EOFError.
 try:
  choice=input("Item: ")
  choice=choice.title() 

#To calculate bill if user choice is in menu and print it.   
  if choice in menu:
    bill=bill+((menu[choice]))
    print("Total: $"+f"{bill:.2f}")

#Except KeyError promt user again Item.
 except(KeyError):
   pass
 
#Except EOFError xit loop.
 except EOFError:
   break

    