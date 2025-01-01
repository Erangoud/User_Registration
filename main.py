import re 

class InvalidInput(Exception):
    pass

def validate_first_name(first_name):
    pattern =r"^[A-Z][a-zA-Z]{2,}$"
    match = re.match(pattern,first_name)
    if not match:
        raise InvalidInput("invalid \nfirst letter should be CAPITAL and minimum 3 letters required")
    return True 

def valid_last_name(last_name):
    pattern=r"^[A-Z][a-zA-Z]{2,}$"
    match=re.match(pattern,last_name)
    if not match :
        raise InvalidInput("invalid \nfirst letter should be CAPITAL and minimum 3 letters required")
    return True 

try:
    first_name=input("enter the first name : ")
    validate_first_name(first_name)
    print("Valid")

    last_name=input("enter the last name : ")
    valid_last_name(last_name)
    print("valid")
        
except InvalidInput as e:
    print(f"invalid input {e}")


