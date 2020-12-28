#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 00:41:46 2020

@author: parthxparab
"""

from stat_parser import Parser
import nltk
from multiprocessing import Process
import time 

parser = Parser()
print('CKY algorithm on Book the cooks who cook the books. \n')
print(parser.parse("Book the cooks who cook the books."))


moby_dick = nltk.corpus.gutenberg.raw('melville-moby_dick.txt')
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = sent_tokenizer.tokenize(moby_dick)

val = ""
word_count = 0
for sentence in sentences:
    w = len(nltk.tokenize.word_tokenize(sentence))
    if w > word_count:
        word_count = w
        val = sentence
        
print("\nThis is the longest sentence: \n\n" + val)
print('\n')
print('CKY Algorithm on longest sentence: \n')
def def1():
    print("Parsing 1/4")
    parser = Parser()
    print(parser.parse(val[0:702]))
    print("Parsing 1/4: finished")

def def2():
    print("Parsing 2/4")
    parser = Parser()
    print(parser.parse(val[702:1404]))
    print("Parsing 2/4: finished")
    
def def3(): 
    print("Parsing 3/4")
    parser = Parser()
    print(parser.parse(val[1404:2106]))
    print("Parsing 3/4: finished")
    
def def4(): 
    print("Parsing 4/4")
    parser = Parser()
    print(parser.parse(val[2106:]))
    print("Parsing 4/4: finished")
    
    
    
if __name__ == "__main__": 
    start_time = time.time()
    p1 = Process(target = def1)
    p1.start()
    
    p2 = Process(target = def2)
    p2.start()
    
    p3 = Process(target = def3)
    p3.start()
    
    p4 = Process(target = def4)
    p4.start()
    
    print('-----')
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    
    print("Total time ran: " + str(time.time()-start_time) + " seconds")