import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    # Check if re matches the ip.
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip):

        # Create a list of numbers by splitting at "."
        num_list=ip.split(".")
        
        # Check if num is > 255 or < 0.
        for num in num_list:
            if int(num)>255 or int(num)<0:
                return(False)
        return(True)
    else:
        return(False)


if __name__ == "__main__":
    main()