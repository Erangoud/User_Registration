import re 

class InvalidName(Exception):
    pass

class InvalidPhoneNum(Exception):
    pass

class Invalidemail(Exception):
    pass 

class InvalidPassword(Exception):
    pass 


def validate_first_name(first_name):
    pattern =r"^[A-Z][a-zA-Z]{2,}$"
    match = re.match(pattern,first_name)
    if not match:
        raise InvalidName("\nfirst letter should be CAPITAL and minimum 3 letters required")
    return True 

def valid_last_name(last_name):
    pattern=r"^[A-Z][a-zA-Z]{2,}$"
    match=re.match(pattern,last_name)
    if not match :
        raise InvalidName("\nfirst letter should be CAPITAL and minimum 3 letters required")
    return True 

def valid_email(email):
    pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-z]+\.[a-zA-Z]{2,}$"
    match=re.match(pattern,email)
    if not match :
        raise Invalidemail("the email you entered is invalid ")
    return True

def validate_phone_number(number):
    pattern=r"^\+\d{1,3} \d{10}$"
    match=re.match(pattern,number)
    if not match:
        raise InvalidPhoneNum("the entered number is invalid ")
    return True

def validate_password(password):
    if len(password)<8:
        raise InvalidPassword("the password length must me above 8 characters")
    if not re.search(r"[A-Z]",password):
        raise InvalidPassword("password must contain atleast one uppercase ")
    if not re.search(r"\d",password):
        raise InvalidPassword("password must contain atleast one numeric character")
    if len(re.findall(r'[!@#$%^&*()_+]', password)) != 1:
        raise InvalidPassword("Password must have exactly one special character.")
    
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

    number=input("enter the mobile number : ")
    validate_phone_number(number)
    print("valid number ")

    passwd=input("enter the password : ")
    validate_password(passwd)
    print("valid password")
    
except InvalidPassword as e:
    print(f"invalid input {e}")
except InvalidName as e:
    print(f"invalid input {e}")
except InvalidPhoneNum as e:
    print(f"invalid input {e}")
except Invalidemail as e:
    print(f"invalid input {e}")
