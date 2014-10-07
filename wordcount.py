"""
Write a program, wordcount.py, that opens a file named on the command line 
and counts how many times each space-separated word occurs in that file. 
Your program should then print those counts to the screen. For example:

"""

import string

def cleanup_str(item, letter):
    new_str = string.replace(item, letter, "")
    return new_str

def output_word_freq(word_count):
    list_o_tuples = word_count.items()
    list_o_tuples.sort(key=lambda x: x[1])
    list_o_tuples.reverse()

    for word in range(len(list_o_tuples)):
        print "Word:%s, Frequency:%r" % (list_o_tuples[word][0], list_o_tuples[word][1])


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

    output_word_freq(word_count)


if __name__ == "__main__":
    count_word_instances()


