print("Amount Due: 50")
due=50
while True:
    userip=int(input("Insert Coin: "))
    if(userip==25 or userip==10 or userip==5):
     due=due-userip
     if(due>0):
         print(f"Amount Due: {due}")
     else:
         print(f"Change Owed: {-due}")
         break
    else:
       print(f"Amount Due: {due}")