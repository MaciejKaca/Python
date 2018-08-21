# Write a Python program to count the occurrences of each word in a given sentence.
def word_counter(sentence):
    dict = {}
    for word in sentence.split():
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    return dict

answer = {"Ala": 2, "ma": 2, "kota.": 1, "psa.": 1}
assert word_counter("Ala ma kota. Ala ma psa.") == answer
