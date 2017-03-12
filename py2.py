#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:52:27 2017

@author: tyoung12
"""

import sys

def createDictionary():
    
    userInput = input("Enter the name of a text file")
    infile = open(userInput)
    lines = infile.read()
    unwanted = ".,-:"
    words = lines.split()
    infile.close()
    
    
    wordfreq = {}
    realDict = {}
    firstWord = words[0]
    secondWord = words[1]
    #for raw_word in words:
        #word = raw_word.strip(unwanted)
        #if word not in wordfreq:
            #wordfreq[word] = 0
        #wordfreq[word] += 1
        
    
    for i in range(len(words)-2):  ##length of words
        if (words[i], words[i+1]) not in realDict: #if the two word key is not in the dictionary
            key = words[i], words[i+1]  #store two word value as a key in the dictionary
            realDict.setdefault(key, []) #create a list for the values of the two word key
            realDict[key].append(words[i+2])  #store the word after the two word pair as a value
        elif (words[i], words[i+1]) in realDict and realDict.get((words[i], words[i+1])) != words[i+2]:  #if the key is already in the dictionary but the value is different, add the value to the value list
            realDict[words[i], words[i+1]].append(words[i+2])
           
        elif (words[i], words[i+1]) in realDict and realDict.get((words[i], words[i+1])) == words[i+2]:
            realDict[words[i], words[i+1]].append(words[i+2])
        
        else:
            realDict = realDict
    
            
   
    print (firstWord + " " + secondWord)
    for i in range(len(words)-2):
        print (str(realDict[words[i], words[i+1]]))
        
        
        
        
    #for key in realDict:
        #if realDict[key] not in wordfreq:
            #wordfreq[realDict[key]] = 0
        #wordfreq[realDict[key]] += 1
        
        
    #for key in realDict:
        #print (key, realDict[key])
        
    #for key in wordfreq:
        #print (key, wordfreq[key])
        
    
createDictionary()



        
