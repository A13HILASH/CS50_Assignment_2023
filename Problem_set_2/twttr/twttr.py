userip=input("Input: ")
for i in userip:
    if(i=='a' or i=='A'):
        i=i.replace("a","").replace("A","")
    elif(i=='e' or i=='E'):
        i=i.replace("e","").replace("E","")
    elif(i=='i'or i=='I'):
        i=i.replace("i","").replace("I","")
    elif(i=='o' or i=='O'):
        i=i.replace("o","").replace("O","")
    elif(i=='u' or i=='U'):
        i=i.replace("u","").replace("U","")
    print(i,end="")
      