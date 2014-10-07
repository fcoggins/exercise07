"""
Write a program, wordcount.py, that opens a file named on the command line 
and counts how many times each space-separated word occurs in that file. 
Your program should then print those counts to the screen. For example:

"""

import string

def cleanup_str(item, letter):
    new_str = string.replace(item, letter, "")
    return new_str

def count_word_instances():
    filename = open("twain.txt")
    document = filename.read()
    document_stripped = document.strip()
    word_list = document.split()

    punct_chars = string.punctuation

    #searching chars in each string in list
    for i in range(len(word_list)):
        for letter in word_list[i]:
            
            if letter in punct_chars:
                word_list[i] = cleanup_str(word_list[i], letter)

    dictionary = {}

    for word in word_list:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    for key, value in dictionary.iteritems():
        print key, value

if __name__ == "__main__":
    count_word_instances()


