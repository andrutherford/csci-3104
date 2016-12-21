import sys
import math
import random
import os

'''
def main():
    #print(wordDict.keys())
    for key in wordDict:
        for otherkeys in wordDict:
            x= 0
            if (key != otherkeys) and (len(key)<len(otherkeys)):
                    for keyindex in range(0,len(key)):

                        if key[keyindex] in otherkeys:
                            x = x + 1
                        elif(key[keyindex]not in otherkeys):
                            continue
                        if x == len(key):
                            wordDict[key].append(otherkeys)

    print("done with setting values")
    chain_length=0
    chain = []
    keys = []
    longest_chain = []
    for word in wordDict:
        count = 0
        for value in wordDict[word]:
            count = count + 1
        if count >= chain_length:
            chain_length= count
            keys.append(word)

    for index in range(0,len(keys)):
        longest_chain.append(keys[index])
        for value in wordDict[keys[index]]:
            longest_chain.append(value)
        print((longest_chain))
'''
def remove_key(dicts,word):
    dicts.pop(word,None)
    return dicts

def short_words(dicts,length):
    length_word = length
    word =""
    for key in dicts:
        if len(key)<length_word:
            length_word = len(key)
            word = key
    return word
def longest_word(dicts):
    length_word = 0
    word = ""
    for key in dicts:
        if len(key)>length_word:
            length_word = len(key)
            word = key
    return word
def small_in_big(small,big):
    x = 0
    leaf =""
    for index in range(0,len(small)):
        if small[index] in big:
            x = x +1
        if x == len(small):
            leaf = big
    return leaf

def leaves(dicts,words,counter,chain,longest_chain_array,longest_chain):
    #print(words)
    length = 20
    starter = 0
    branchs = []
    empty_array = []
    words_seq = []
    if len(words) != 0:
        chain.append(words[0])
    if len(dicts)==0 and len(words)==0:
        return counter,longest_chain_array
    elif len(words)==0 and len(dicts)!=0:
        if (counter>=longest_chain):
            longest_chain= counter
            longest_chain_array.append(chain)
        words_seq.append(short_words(dicts,length))
        updated_dicts = remove_key(dicts,words_seq[0])
        return leaves(updated_dicts,words_seq,starter,empty_array,longest_chain_array,longest_chain)
    x = 1
    for word in range(0,len(words)):#remove_key(dicts,words[word])
        for key in dicts:
            if x==length:
               continue
            elif len(key)==(len(words[word])+x):

                leaf = small_in_big(words[word],key)
                if len(leaf)!= 0:
                    branchs.append(leaf)
            if (len(branchs)==0)and ((dicts.keys().index(key))== (len(dicts)-1)):
                x = x +1
            '''elif(len(branchs)==0 and words ==len(words)):

            '''
                #key = dicts.key()[0]
        counter = counter + 1
        return leaves(dicts,branchs,counter,chain,longest_chain_array,longest_chain)






def main():
    length = 20
    counter = 0
    init_word=[]
    chain = []
    empty_chain = []
    small_word =short_words(wordDict,length)
    longest_words = longest_word(wordDict)
    updated_dict= remove_key(wordDict,small_word)
    init_word.append(small_word)
    longest_possible_chain = len(longest_words)-len(small_word)+1
    print longest_possible_chain
    length_tree,longest_chain_array = leaves(updated_dict,init_word,counter,chain,empty_chain,counter)
    #print length_tree
    print (longest_chain_array)





if __name__ == "__main__":
    wordDict = dict((x.strip(), []) for x in open("wordlist.txt"))
    #wordDict2 =dict((x.strip(), []) for x in open("wordlist.txt"))
    main()
    #print(wordDict)
