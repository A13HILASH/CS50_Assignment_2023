import sys
import requests
import json

#Check for command line,if it doesnt exist,exit with appropriate message.
if len(sys.argv)<2:
    sys.exit("Missing command-line argument")

#Store argument in var.
userip=sys.argv[1]

#Check if argument is float type.
if(float(userip)):
    try:
#Get response for API.
       response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

#Store formatted response in var.
       store=response.json()

#Store dict corresponding to key-"bpi" in dict_store in another a var.
       dict_bpi=store["bpi"]

#Store dict corresponding to key-"USD" in dict_bpi, in another a var.
       dict_USD=dict_bpi["USD"]

#Iterate over dict_USD.
       for keys in dict_USD:

#If key==rate_float,store its corresponding value in a var.
           if keys=="rate_float":
               rate_float=(dict_USD[keys])

#Find amount and print it.
       amount=float(userip)*rate_float
       print(f"${amount:,.4f}")

#Check for  ambiguous exception and exit with appropriate message.
    except requests.RequestException:
       sys.exit("There was an ambiguous exception that occurred while handling your request")

#Exit if cmd arg is not a num with appropriate message.
else:
    sys.exit("Command-line argument is not a number")
