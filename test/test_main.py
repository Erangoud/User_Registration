import pytest
from source.main import validate_first_name,valid_email,valid_last_name,validate_password,validate_phone_number, Invalidemail,InvalidPhoneNum,InvalidName,InvalidPassword

def test_valid_first_name():
    assert validate_first_name("Eran") == True  
    with pytest.raises(InvalidName):
        validate_first_name("eran")

def test_valid_last_name():
    assert valid_last_name("Goud") == True
    with pytest.raises(InvalidName):
        valid_last_name("goud")

def test_valid_email():
    assert valid_email("egoud83@gmail.com") == True 
    with pytest.raises(Invalidemail):
        valid_email("egoudgmail.com")

def test_valid_phone_number():
    assert validate_phone_number("+91 7795796117") == True
    with pytest.raises(InvalidPhoneNum):
        validate_phone_number("788878")

def test_valid_password():
    assert validate_password("Meer@09876") == True
    with pytest.raises(InvalidPassword):
        validate_password("awawa")
