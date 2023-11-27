from validator_collection import checkers

def main():

    print(valid(input("Whats your email? ")))

def valid(email):

    if checkers.is_email(email) == True:
        return "Valid"
    else:
        return "Invalid"
    
if __name__=="__main__":
    main()