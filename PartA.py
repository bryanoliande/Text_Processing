'''
CS121 Homework 1 PartA due Jan 25, 2017

Prompts the user for a text file path, then tokenizes the file 
and computes the word frequencies.

The total time complexity is O(nlogk) where n is the number of tokens
and k is the count of the highest occuring tokens.

@author: bryanoliande 13179240
'''
from datetime import datetime
import re
from collections import Counter
import os
import sys
'''
Reads in a text file and returns a list of tokens in the file.
Tokens are alphanumeric characters independent of capitalization.
This function is O(n) where n is the number of words in the text
file. We are only "visiting" each word once in re.split()
and the double for loop.
'''
import unicodedata

def tokenize(text_file):
    token_list = []
    lines = text_file.readlines()

    for line in lines:
        tempList = re.split('[^a-zA-Z0-9]', line)
        for word in tempList:
            if word != '':
                token_list.append(word.lower())

    text_file.close()
    return token_list

'''
Counts the number of occurences of each word in a token list.
Again, this is O(n)  because we only "visit" each word once.
'''


def compute_word_frequencies(token_list):
    token_frequencies = Counter()

    for token in token_list:
        token_frequencies[token] += 1

    return token_frequencies


'''
Writes the word frequency counts into a file in descending order

O(nlogk) because of the .most_common() function call where
n is the total number of tokens and k is the count of most common elements
(i.e. if you had 1000 total elements with 3 elements occuring
 100 times n = 1000, k = 3)
'''


def print_frequencies(token_frequencies):
    out_file = open("partA.txt", "w")
    for key, value in token_frequencies.most_common():
        out_file.write(key + ": " + str(value) + "\n")




text_file_path = sys.argv[1]

if os.path.isfile(text_file_path):


    text_file = open(text_file_path, "r", encoding = 'ascii', errors = 'ignore')
    startTime = datetime.now()
    token_list = tokenize(text_file)
    token_frequencies = compute_word_frequencies(token_list)
    print_frequencies(token_frequencies)
    print("Wrote to file: partA.txt")
    print("TIME TAKEN: " + str(datetime.now() - startTime))
else:
    print("You entered an invalid file path")