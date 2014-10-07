"""
Write a program, wordcount.py, that opens a file named on the command line 
and counts how many times each space-separated word occurs in that file. 
Your program should then print those counts to the screen. For example:

"""

import string
from operator import itemgetter

def cleanup_str(item, letter):
    new_str = string.replace(item, letter, "")
    #new_str = new_str.lower()
    return new_str

def count_word_instances():
    filename = open("twain.txt")
    document = filename.read()
    word_list = document.split()
    punct_chars = string.punctuation

    #searching chars in each string in list
    for i in range(len(word_list)):
        for letter in word_list[i]:
            
            if letter in punct_chars:
                word_list[i] = cleanup_str(word_list[i], letter)

    word_count = {}

    for word in word_list:
        word = word.lower()
        word_count.setdefault(word, 0)
        word_count[word] += 1

    list_o_tuples = word_count.items()
    #print list_o_tuples
    list_o_tuples.sort(key=lambda x: x[1])
    list_o_tuples.reverse()
    print list_o_tuples


    # for value in word_count.sort(key=lambda x: x[1]):
        
    # print word_count.items()

    # # for key, value in word_count.iteritems():
    #     print key, value

if __name__ == "__main__":
    count_word_instances()


