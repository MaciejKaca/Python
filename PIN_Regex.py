import re

def validatePIN(PIN):
    return bool(re.fullmatch(r'[0-9]{4}', PIN))

assert validatePIN("1234") == True, "Wrong validation!"
assert validatePIN("12345") == False, "Wrong validation!"
assert validatePIN("a234") == False, "Wrong validation!"
