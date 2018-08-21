import re
def validate_input(word):
    return bool(re.fullmatch(r'[a-z0-9_]{5,20}', word))

assert validate_input("Summer Academmy") == False, "Bad validation!"
assert validate_input("Summer_Academmy") == False, "Bad validation!"
assert validate_input("summer_academmy") == True, "Bad validation!"

