def main():
#Get input.
    greeting=input("Greeting: ")
    ret_val=value(greeting)
    print("$"+ret_val)
#Define value fn.
def value(greeting):
    if(greeting.lower().strip()== 'hello'or greeting.strip().lower().startswith('hello')):
        return(0)
    elif(greeting.strip().lower().startswith('h')):
        return(20)
    else:
        return(100)

if __name__=="__main__":
    main()