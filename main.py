import re 

def validate_first_number(first_name):
    pattern =r"^[A-Z][a-zA-Z]{2,}$"
    match = re.match(pattern,first_name)
    return match is not None

first_name=input("enter the first name : ")
if validate_first_number(first_name):
    print("Valid")
else :
    print("invalid \nfirst letter should be CAPITAL and minimum 3 letters required")