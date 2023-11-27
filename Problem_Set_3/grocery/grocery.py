#Declare empty dict.
grocery={}

#Loop start.
while True:
    try:
#Get user input and initialise them in dict in uppercase.
      for i in range(10):
        item=input()
        grocery[i]=item.upper()

    except EOFError: 
#List of sorted values. 
       grocery=sorted(grocery.values())

#Count repeated items in list and create a new dict.
       grocery = {i:grocery.count(i) for i in grocery}

#Obtain Key Value tuples list of dict grocery with .item() and Print output.
       for value,key in grocery.items():
          print(key,value)

#Stop loop.
       break
      
        
