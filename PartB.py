'''
CS121 Homework 1 PartB due Jan 25, 2017

Prompts the user for a two text file paths, then tokenizes the files
and outputs the tokens they have in common along with the total count
of said tokens.

The total time complexity is O(n) and explanations on why
this script runs in linear time can be found above the various
functions in this file.

@author: bryanoliande
'''
import re
import os.path
from datetime import datetime
import sys

'''
Reads in a text file and returns a list of tokens in the file.
Tokens are alphanumeric characters independent of capitalization.
This function is O(n) where n is the number of words in the text
file. We are only "visiting" each word once in re.split()
and the double for loop.
'''


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
Takes two text files as arguments and outputs
the number of tokens they have in common.

Time complexity is O(n) where n is the number of tokens:

tokenization of the two files is O(n),
list to set conversion is O(n)
set.intersection() function is O(min (len(set one),len(set two) ))
                                    => O(n)
'''


def intersection_of_files(file_one, file_two):
    file_one_token_list = tokenize(file_one)
    file_two_token_list = tokenize(file_two)

    file_one_token_set = set(file_one_token_list)
    file_two_token_set = set(file_two_token_list)
    intersection = file_one_token_set.intersection(file_two_token_set)

    out_file = open("partB.txt", "w")

    for item in intersection:
        out_file.write(item + '\n')
    print('# of common words: ' + str(len(intersection)))




text_file_one_path = sys.argv[1]
text_file_two_path = sys.argv[2]

if os.path.isfile(text_file_one_path) and os.path.isfile(text_file_two_path):
    file_one = open(text_file_one_path, "r", encoding = 'ascii', errors = 'ignore')
    file_two = open(text_file_two_path, "r",  encoding = 'ascii', errors = 'ignore')
    startTime = datetime.now()
    intersection_of_files(file_one, file_two)
    print("Wrote common words to partB.txt")
    print("TIME TAKEN: " + str(datetime.now() - startTime))

else:
    print("You entered an invalid file path. Re-run the program.")
