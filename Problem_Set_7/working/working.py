import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    
    pattern = r"^(\d{1,2}):?(\d{2})? ([A-P]M) to (\d{1,2}):?(\d{2})? ([AP]M)$"
    match = re.match(pattern,s)
    if match:
        matches=match.groups()
        if int(matches[0]) > 12 or int(matches[3]) > 12 :
            raise ValueError
        if matches[1] !=  None or matches[4] != None:
            if int(matches[1]) >59 or int(matches[4]) > 59 :
                raise ValueError
        first_time = _24hr_format(int(matches[0]),(matches[1]),matches[2])
        second_time = _24hr_format(int(matches[3]),(matches[4]),matches[5])
        
        return f"{first_time} to {second_time}"

    else:
        raise ValueError
    
def _24hr_format(hours,min,am_pm):

    if hours == 12:
            hours = 0
    if am_pm == 'PM':
            hours = hours + 12

    if min == None:
        min = 0
    else:
        min = int(min)
    time_24_hour = f"{hours:02d}:{min:02d}"
    return time_24_hour


if __name__ == "__main__":
    main()