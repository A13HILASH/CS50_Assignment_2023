userip=input("Greeting: ")
if(userip.lower().strip()== 'hello'or userip.strip().lower().startswith('hello')):
    print('$0')
elif(userip.strip().lower().startswith('h')):
    print('$20')
else:
    print("$100")