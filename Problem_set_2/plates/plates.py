def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2<=len(s)<=6 or s[:2].isdigit() or s.isspace() or not s.isalnum():return False
    for i in range(len(s)):
     if s[i].isdigit():
      if s[i]=='0':return False
      flag=i+1
      while flag<=len(s)-1:
       if s[flag].isalpha():return False
       flag=flag+1
      else:return True

    else:return True
    
main()