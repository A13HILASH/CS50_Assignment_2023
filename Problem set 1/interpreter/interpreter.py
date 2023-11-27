userip=input('Expression: ')
x,y,z=userip.split(" ")
x=int(x)
z=int(z)
match y:
    case '+':
        print("{0:d}.0".format(x+z))
    case '-':
        print("{0:d}.0".format(x-z))
    case '*':
        print("{0:d}.0".format(x*z))
    case '/':
        print("{0:.1f}".format(x/z))
    



        