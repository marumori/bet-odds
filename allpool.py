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
playFileInitial = open('fileInitial.txt', 'wb')
playFileCurrent = open('fileCurrent.txt', 'wb')

#Get XML info for each pooltype
def get_pooltype(pooltype):
    if pooltype == 'HAD':
        resHAD = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=HAD&isLiveBetting=false')
        return resHAD
    elif pooltype == 'FHA':
        resFHA = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=FHA&isLiveBetting=false')
        return resFHA
    elif pooltype == 'HHA':
        resHHA = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=HHA&isLiveBetting=false')
        return resHHA
    elif pooltype == 'HDC':
        resHDC = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=HDC&isLiveBetting=false')
        return resHDC
    elif pooltype == 'HIL':
        resHIL = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=HIL&isLiveBetting=false')
        return resHIL
    elif pooltype == 'FHL':
        resFHL = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=FHL&isLiveBetting=false')
        return resFHL
    elif pooltype == 'CHL':
        resCHL = requests.get( 'http://bet.hkjc.com/football/getXML.aspx?pooltype=CHL&isLiveBetting=false')
        return resCHL
    elif pooltype == 'CRS':
        resCRS = requests.get( 'http://bet.hkjc.com/football/getXML.aspx?pooltype=CRS&isLiveBetting=false')
        return resCRS
    elif pooltype == 'FCS':
        resFCS = requests.get( 'http://bet.hkjc.com/football/getXML.aspx?pooltype=FCS&isLiveBetting=false')
        return resFCS
    elif pooltype == 'FTS':
        resFTS = requests.get( 'http://bet.hkjc.com/football/getXML.aspx?pooltype=FTS&isLiveBetting=false')
        return resFTS
    elif pooltype == 'TTG':
        resTTG = requests.get( 'http://bet.hkjc.com/football/getXML.aspx?pooltype=TTG&isLiveBetting=false')
        return resTTG
    elif pooltype == 'OOE':
        resOOE = requests.get( 'http://bet.hkjc.com/football/getXML.aspx?pooltype=OOE&isLiveBetting=false')
        return resOOE
    elif pooltype == 'HFT':
        resHFT = requests.get( 'http://bet.hkjc.com/football/getXML.aspx?pooltype=HFT&isLiveBetting=false')
        return resHFT
    
"""
#Storing Data
Please create two dataframes dataInitial and dataCurrent respectively
Please store individual pooltype data as individual variable[1-16] in dataInitial and dataCurrent and record the timestamp for each extraction
"""
#Insert Code here
def loop():
    columnVariable = {'HAD','FHA','HHA','HDC','HIL','FHL','CHL','CRS','FCS','FTS','TTG','OOE','HFT'}
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

fileInitial = "fileInitial.txt"
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


