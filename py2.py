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
    #unwanted = ".,-:"
    words = lines.split()
    infile.close()
    
    
    #wordfreq = {}
    realDict = {}
    firstWord = words[0]
    secondWord = words[1]
    
    counter = {}
    maxItemCount = 0
   
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
            #add +1 to counter
            #if key not in wordfreq:
                #wordfreq[key] = 0
            #wordfreq[key] += 1
        elif (words[i], words[i+1]) in realDict and realDict.get((words[i], words[i+1])) != words[i+2]:  #if the key is already in the dictionary but the value is different, add the value to the value list
            realDict[words[i], words[i+1]].append(words[i+2])
            #add +1 to counter
           
        elif (words[i], words[i+1]) in realDict and realDict.get((words[i], words[i+1])) == words[i+2]:
            realDict[words[i], words[i+1]].append(words[i+2])
            #add nothing to counter
        
        else:
            realDict = realDict

    #return realDict
            
    
    #prints the story using the 1st item in every list
    print (firstWord + " " + secondWord)
    for i in range(len(words)-2):
        print (str(realDict[words[i], words[i+1]][0]))
        
   

   
    #for x in realDict:
        #keyValues = realDict[x]
        #for i in range(len(keyValues)-1):
            #for k in keyValues[i]:  #for each value
                #try:
                    #counter[k]
                    #counter[k] += 1
                #except KeyError:
                    #counter[k] = 1
                
            #if counter[k] > maxItemCount:
                #maxItemCount = counter[k]
                #mostFrequent = k
        
                #print (mostFrequent)

    #for i in range(50):
        #for k in realDict[words[i], words[i+1]]:
             #try:
                #counter[k]
                #counter[k] += 1
             #except KeyError:
                #counter[k] = 1
                
        #if counter[k] > maxItemCount:
            #maxItemCount = counter[k]
            #mostFrequent = k
        
    #print (mostFrequent)
    
    
    
    #for i in range(len(words)-2):
        #if len(realDict[words[i], words[i+1]]) > 2:
            #print(str(realDict[words[i], words[i+1]]) + ": Yes!!!")
        #else:
            #print(str(realDict[words[i], words[i+1]]) + ": NOOO")
     
        
                    
    #for x in realDict:
        #key = realDict[x] ##list of values
        #print(key[0])
        
    #for key in realDict:
        #if realDict[key] not in wordfreq:
            #wordfreq[realDict[key]] = 0
        #wordfreq[realDict[key]] += 1
        
        #print((len(realDict[words[0],words[1]])))
               
    #print (realDict[words[0],words[1]])
     

            
    #for key in realDict:
        #print (key, realDict[key])
        
    #for key in wordfreq:
        #print (key, wordfreq[key])
        
    
createDictionary()




   #counter = {}
   #maxItemCount = 0
    #for word in realDict
    #for k in realDict[words[223], words[224]]:
            #try:
                #counter[k]
                #counter[k] += 1
            #except KeyError:
                #counter[k] = 1
                
        #if counter[k] > maxItemCount:
            #maxItemCount = counter[k]
            #mostFrequent = k
        
    #print (mostFrequent)

        
