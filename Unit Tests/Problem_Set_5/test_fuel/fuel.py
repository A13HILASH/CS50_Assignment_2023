def main():
  userip=input("Fraction: ")
  per=convert(userip)
  ind=gauge(per)
  print(ind)


def convert(userip):
    while True:
        try:
            x,y=userip.split(sep='/')
            x=int (x)
            y=int (y)
            p=x/y
            if p<=1:return int(p*100)
            else:userip=input("Fraction: ")   
        except(ValueError,ZeroDivisionError):
           raise

def gauge(per):
    if per<=1:return("E")
    elif 99<=per<=100:return("F")
    elif 1<per<99:return str(per) +"%"


if __name__ == "__main__":
    main()