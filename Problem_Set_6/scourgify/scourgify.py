
"""
import sys
import csv

arg=sys.argv[1:]

#Exit if no filename or path.
if len(arg)==0:
   sys.exit("Too few command-line arguments")

#Exit if too many arg.
if len(arg)>2:
    sys.exit("Too many command-line arguments")

#Exit if file is not a csv file.
if not '.csv' in arg[0] or not '.csv' in arg[1]:
    sys.exit("Not a CSV file")

try:
    list=[]
    fieldnames=["first","last","house"]
    with open(arg[0],"r",newline='') as file1:
        reader=csv.DictReader(file1)
        for line in reader:
            last,first=line["name"].split(",")
            first=first.strip()
            house=line["house"].lstrip()
            list.append({'first':first,'last':last,'house':line["house"]})
    with open(arg[1],"w",newline='') as file2:
            writer=csv.DictWriter(file2,fieldnames=fieldnames)
            writer.writeheader()
            for row in list:
                writer.writerow({'first':row['first'],'last':row['last'],'house':row['house']})

except FileNotFoundError:
    sys.exit("File does not exist")
"""

import sys
import csv

arg=sys.argv

#Exit if no filename or path.
if len(arg)<3:
   sys.exit("Too few command-line arguments")

#Exit if too many arg.
if len(arg)>3:
    sys.exit("Too many command-line arguments")

#Exit if file is not a csv file.
if '.csv' not in arg[1] or '.csv' not in arg[2]:
    sys.exit("Not a CSV file")

list=[]
fieldnames=["first","last","house"]

try:
    with open(arg[1],"r",newline='') as file1:
        reader=csv.DictReader(file1)
        for line in reader:
            last,first=line["name"].split(",")
            first=first.strip()
            list.append({'first':first,'last':last,'house':line["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {arg[1]}")

with open(arg[2],"w",newline='') as file2:
    writer=csv.DictWriter(file2,fieldnames=fieldnames)
    writer.writerow({"first":'first',"last":'last',"house":'house'})
    for row in list:
        writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})