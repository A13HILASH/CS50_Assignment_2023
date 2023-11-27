def main():
    
    op=fuel()
    if op=='F'or op=='E':
     print(op)
    else:
     print(f"{op}"+"%")

def fuel():
    while True:
         try:
            userip=input("Fraction: ")
            x,y=userip.split(sep='/')
            x=int (x)
            y=int (y)
            per=round(x/y*100)
            if per<=1:return("E")
            elif 99<=per<=100:return("F")
            elif 1<per<99:return(per)
         except:
            pass

main()