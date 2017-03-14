#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:52:27 2017

@author: tyoung12
"""

##Tyler Young and Mark Malburg

def createStory():
    
    userInput = input("Enter the name of a text file")
    infile = open(userInput)
    lines = infile.read()
    words = lines.split()
    infile.close()
    
    realDict = {}
    firstWord = words[0]
    secondWord = words[1]
    
    #counter = {}
    #maxItemCount = 0
   

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
            
    
            
    
    #prints the story using the 1st item in every list
    print (firstWord + " " + secondWord)
    for i in range(len(words)-2):
        print (str(realDict[words[i], words[i+1]][0]))
      
 
createStory()  

   
    
    #for i in range(len(words)-2):
        #if len(realDict[words[i], words[i+1]]) > 2:
            #print(str(realDict[words[i], words[i+1]]) + ": Yes!!!")
        #else:
            #print(str(realDict[words[i], words[i+1]]) + ": NOOO")
     
        
        
            
    #for key in realDict:
        #print (key, realDict[key])
        
    #for key in wordfreq:
        #print (key, wordfreq[key])
        

        
   ##gets the most frequent value from each value list     
   #counter = {}
   #maxItemCount = 0
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

        
