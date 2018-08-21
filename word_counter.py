# Write a Python program to count the occurrences of each word in a given sentence.
def word_counter(sentence):
    dict = {}
    for word in sentence.split():
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    return dict

def word_counter2(sentence):
    new_sentence = "".join(c for c in sentence if (c.isalnum() or c.isspace()) )
    another_chars = [c for c in sentence if not(c.isalnum() or c.isspace()) ]
    dict = {}
    for word in new_sentence.split():
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1

    for word in another_chars:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    return dict

print(word_counter2("Ala ma kota. )))))))))Ala ma psa."))

#answer = {"Ala": 2, "ma": 2, "kota.": 1, "psa.": 1}
#assert word_counter("Ala ma kota. Ala ma psa.") == answer
