import sys
import csv
import os.path
from PIL import Image,ImageOps

arg=sys.argv

#Exit if no filename or path.
if len(arg)<3:
   sys.exit("Too few command-line arguments")

#Exit more than two input arg.
if len(arg)>3:
    sys.exit("Too many command-line arguments")

#Check if input path exixts.
if not os.path.exists(arg[1]):
    sys.exit("Input does not exist")

#Convert path to lowercase.          
input_path = os.path.normcase(arg[1])    
output_path = os.path.normcase(arg[2])

#Split path into root and extension.
root1,ext1 = os.path.splitext(input_path)
root2,ext2 = os.path.splitext(output_path)

#Check for invalid extensions in input and output file.
extension=[".jpg", ".jpeg",".png"]

if ext1 not in extension:
    sys.exit("Invalid input")
or ext2 not in extension:
    sys.exit("Invalid output")

#Check if input and output have different extension.
if ext1!=ext2:
    sys.exit("Input and output have different extensions")

#Open image to overlay on.
before1 = Image.open(arg[1])

#Open Overlaying image.
shirt = Image.open("shirt.png")

#Get size of overlaying image.
size = shirt.size

#Perform overlaying operation and save it in output
after1 = ImageOps.fit(before1,size)
after1.paste(shirt,shirt)
after1.save(arg[2])





