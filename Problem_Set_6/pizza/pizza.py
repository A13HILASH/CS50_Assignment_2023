from tabulate import tabulate
import sys
import csv

file_name=sys.argv[1:]

#Exit if no filename or path.
if len(file_name)==0:
   sys.exit("Too few command-line arguments")

#Exit if too many arg.
if len(file_name)>1:
    sys.exit("Too many command-line arguments")

#Exit if file is not a csv file.
if not '.csv' in file_name[0]:
    sys.exit("Not a CSV file")

#Open csvfile and read it.    
try:
    with open(file_name[0],"r") as file:
        reader = csv.reader(file)
        list_lines=[]
        #Create list of lines with each line from reader(Each line is a list).
        for line in reader:
            list_lines.append(line)
    #Coose first element of list as header for table and delete it from the list
    header=list_lines[0]
    list_lines.pop(0)
    print(list_lines)
    #Print list(list of lists) in table format.
    print(tabulate(list_lines,headers=header,tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")

file.close()