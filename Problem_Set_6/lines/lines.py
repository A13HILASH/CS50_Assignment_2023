import sys

file_name=sys.argv[1:]

#Exit if no filename or path.
if len(file_name)==0:
   sys.exit("Too few command-line arguments")

#Exit if too many arg.
if len(file_name)>1:
    sys.exit("Too many command-line arguments")

#Exit if file is not a python file.
if not '.py' in file_name[0]:
    sys.exit("Not a Python file")

#Open file.    
try:
    file=open(file_name[0],"r")
    lines=file.readlines()
    no_lines=len(lines)
    #Check if line is a comment or blank line.
    for line in lines:
        if line.lstrip().startswith("#") or not line.strip():
            no_lines-=1
    #Print no of lines excluding comment and blank line.        
    print(no_lines)

except FileNotFoundError:
    sys.exit("File does not exist")

file.close()