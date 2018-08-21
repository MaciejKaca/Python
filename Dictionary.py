dict = {"Test" : 1, "Test2" : 2}

print(dict)

print(dict['Test'])
print(dict['Test2'])


del  dict['Test']

if "Test3" in dict:
    print("Found")
else:
    dict['Test3']=5

dict['Test2']+=3

print(dict)