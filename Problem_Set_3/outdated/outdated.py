months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    
    try:
        date=input("Date: ")
        month,day,year=date.split('/')
        if(int(day)>=1 and int(day)<=31 and int(month)>=1 and int(month)<=12):
            break
        
    except:
        try:
          month,day,year=date.split(' ')
          if not day.endswith(","):continue
          day=day.replace(',','')
          for i in range(len(months)):
              if months[i]==month:
                  month=i+1
          if(int(day)>=1 and int(day)<=31 and int(month)>=1 and int(month)<=12):
              break 
        except:
    
            pass
        
print(f"{year}-{int(month):02}-{int(day):02}")        
 
      

        
        
