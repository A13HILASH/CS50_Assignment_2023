userip=(input("camelCase: "))
print("snake_case: ",end="")
for c in userip:
    if(c.islower()):
        print(f"{c}",end="")
    else:
        print("_",end="")
        print(f"{c.lower()}",end="")
        


    