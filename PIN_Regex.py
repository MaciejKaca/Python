import re

def validatePIN(PIN):
    if re.fullmatch(r'[0-9]{4}', PIN):
        return True
    else:
        return False

assert validatePIN("1234") == True, "Wrong validation!"
assert validatePIN("12345") == False, "Wrong validation!"
assert validatePIN("a234") == False, "Wrong validation!"
