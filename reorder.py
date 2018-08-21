import re

def reorder_substrings(sentence):
    new_sentence=[0]*len(sentence.split())
    count=0
    final_sentence=""
    for word in sentence.split():
        for char in word:
            if char.isdigit():
                number=int(char)
                new_sentence[number-1]=word
                count+=1
    final_sentence = ' '.join(str(x) for x in new_sentence)
    return(final_sentence)

assert reorder_substrings("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est", "Failed!"
