#!/usr/bin/env python3

def return_evens(num_list):
    return[number for number in num_list if number % 2 ==0 ]
    
print(return_evens([2,6,7]))


def make_exclamation(sentence_list):
    return[sentence + "!" for sentence in sentence_list]
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))