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

def valid_email(email):
    pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-z]+\.[a-zA-Z]{2,}$"
    match=re.match(pattern,email)
    if not match :
        raise InvalidInput("the email you entered is invalid ")
    return True


try:
    first_name=input("enter the first name : ")
    validate_first_name(first_name)
    print("Valid")

    last_name=input("enter the last name : ")
    valid_last_name(last_name)
    print("valid")
        
    email=input("enter the email : ")
    valid_email(email)
    print("valid")
        
except InvalidInput as e:
    print(f"invalid input {e}")


