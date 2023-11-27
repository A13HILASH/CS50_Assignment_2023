from datetime import date
import re
import sys
import inflect


def is_valid_date(dob):
    matches = re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",dob)
    if matches != None: 
        return True
    else: 
        return False
    
def cal_age_in_minutes(dob):
    #Get today's date.
    today_date =  date.today()

    #Convert input DOB into int .Find num of days btw today and DOB and convert it to minutes.
    year,month,day = dob.split("-")
    date_of_birth = date(int(year),int(month),int(day))
    
    date_difference = today_date - date_of_birth
    date_in_minutes = date_difference.days * 24 *60
    return date_in_minutes

def main():
    
    #Get the date of birth & check if its in the correct format.Exit if wrong format.
    dob = input("Date of Birth: ").strip()
    if is_valid_date(dob) == False:
        sys.exit("Invalid date")

    #Calculate age in minutes.
    age_in_minutes = cal_age_in_minutes(dob)
    #print age in words.
    p = inflect.engine()
    age_in_words = p.number_to_words(age_in_minutes, andword="")
    print(age_in_words.capitalize(),"minutes")
    


if __name__ == "__main__":
    main()