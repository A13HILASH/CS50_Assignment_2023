def main():
#Get input.
    plate = input("Plate: ")
#Print output based in is_valid fn.
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
#Define is_valid.
def is_valid(s):
#Check for length.
    if len(s)>6 or len(s)<2:
        return False
#Check if first two digits are alphabet.
    if s[0].isalpha()==False or s[1].isalpha()==False:
        return False
#Check for space,period and punctuations.
    if s.isalnum()==False:
        return False
    for i in s:
        if i==" ":
            return False
#Check if first digit occuring is 0.
    for i in s:
        if i.isdigit()==True:
            if i=='0':
                return False
            else:
                break
#Check if digits are occuring in middle.
    for i in range(len(s)):
        if s[i].isdigit()==True:
            if not s[i:].isdigit():
                return False
#True if all above conditions are satisfied.
    return True
    

if __name__=="__main__":
    main()