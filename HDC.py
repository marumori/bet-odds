# -*- coding: utf-8 -*-
"""
parse hkjc real time odds data in txt format
maybe use mongolDB to build database
"""
#Insert Code here
import requests
import threading
import pandas as pd
import numpy as np
from time import gmtime, strftime

"""
//Stage 1: Initialisation
#Importing Data 
assign path of getXML_odds_pooltype to variable pooltype[1-16]
Write a function to call on pooltype (for loop)
"""
#Insert Code here
#Export all pooltypes data to a txt file
playFileInitial = open('fileInitialHDC.txt', 'wb')
playFileCurrent = open('fileCurrentHDC.txt', 'wb')

#Get XML info for each pooltype
def get_pooltype(pooltype):
    if pooltype  == 'HDC':
        resHDC = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=HDC&isLiveBetting=false')
        return resHDC
    return null
    
"""
#Storing Data
Please create two dataframes dataInitial and dataCurrent respectively
Please store individual pooltype data as individual variable[1-16] in dataInitial and dataCurrent and record the timestamp for each extraction
"""
#Insert Code here
def loop():
    columnVariable = {'HDC'}
    for x in columnVariable:
        pooltype = x
        #print pooltype
        for chunk in get_pooltype(pooltype):
          #print pooltype
          playFileInitial.write(chunk)    
    print 'fileInitial completed'
    playFileCurrent.write(chunk)
    print 'fileCurrent completed'
loop()

fileInitial = "fileInitialHDC.txt"
#fileCurrent = "2CURR.txt"
#filePrevious = "3PREV.txt"

def readdata(path):
#------read in data ----------
    temp = []
    f = open (path, "r").read().split('\r\n')
    for line in f:
        temp.append (line.split(','))
    return temp

dataInitial = readdata(fileInitial)
#dataInitial, dataCurrent = readdata(fileInitial), readdata(fileCurrent)
print len(dataInitial)
#print len(dataCurrent)
print dataInitial


