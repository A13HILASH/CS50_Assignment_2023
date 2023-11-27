#A program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.


m=int(input("Enter mass in kilograms: "))
c=300000000
print(f"Energy E:{m*c*c}")