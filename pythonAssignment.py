#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:28:32 2017

@author: tyoung12
"""
import sys

def createDictionary():
    
    userInput = input("Enter the name of a text file")
    infile = open(userInput)
    lines = infile.read()
    words = lines.split()
    infile.close()
    
    unwanted = ".,-:"
    wordfreq = {}
    for raw_word in words:
        word = raw_word.strip(unwanted)
        if word not in wordfreq:
            wordfreq[word] = 0
        wordfreq[word] += 1
    
    
    #for key in wordfreq:
        #print (key, wordfreq[key])
        
    
createDictionary()


def groupAnagrams(words):
    realDict = {}
    for i in range(len(words)):  ##length of words
        realDict[words[i], words[i+1]] = words[i+2]
        
    for key in realDict:
        print(key)
        
