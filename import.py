import requests
import threading
from time import gmtime, strftime
#
#1Record HomeAwayDraw odds every 60seconds
resHAD = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=HAD&isLiveBetting=false')
resHAD.raise_for_status()
playFile = open('1HAD.txt', 'wb')
playTime = open('1HADtime.txt', 'wb')

def printit():
  threading.Timer(60.0, printit).start()
  print "Hello, World!"
  time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print time
  for chunk in resHAD.iter_content():
    playFile.write(chunk)
    playTime.write(time)
printit()
#
#3Record FirstHalfHomeAwayDraw odds every 60seconds
resFHA = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=FHA&isLiveBetting=false')
resFHA.raise_for_status()
playFile = open('3FHA.txt', 'wb')
playTime = open('3FHAtime.txt', 'wb')

def printit():
  threading.Timer(60.0, printit).start()
  print "Hello, World!"
  time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print time
  for chunk in resFHA.iter_content():
    playFile.write(chunk)
    playTime.write(time)
printit()
#
#4Record HandicapHomeAwayDraw odds every 60seconds
resHHA = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=HHA&isLiveBetting=false')
resHHA.raise_for_status()
playFile = open('4HHA.txt', 'wb')
playTime = open('4HHAtime.txt', 'wb')

def printit():
  threading.Timer(60.0, printit).start()
  print "Hello, World!"
  time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print time
  for chunk in resHHA.iter_content():
    playFile.write(chunk)
    playTime.write(time)
printit()
#
#5 Record Handicap odds every 60seconds
resHDC = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=HDC&isLiveBetting=false')
resHDC.raise_for_status()
playFile = open('5HDC.txt', 'wb')
playTime = open('5HDCtime.txt', 'wb')

def printit():
  threading.Timer(60.0, printit).start()
  print "Hello, World!"
  time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print time
  for chunk in resHDC.iter_content():
    playFile.write(chunk)
    playTime.write(time)
printit()
#
#6 Record HighLow odds every 60seconds
resHIL = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=HIL&isLiveBetting=false')
resHIL.raise_for_status()
playFile = open('6HIL.txt', 'wb')
playTime = open('6HILtime.txt', 'wb')

def printit():
  threading.Timer(60.0, printit).start()
  print "Hello, World!"
  time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print time
  for chunk in resHIL.iter_content():
    playFile.write(chunk)
    playTime.write(time)
printit()
#
#7 Record FirstHalfHighLow odds every 60seconds
resFHL = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=FHL&isLiveBetting=false')
resFHL.raise_for_status()
playFile = open('7FHL.txt', 'wb')
playTime = open('7FHLtime.txt', 'wb')

def printit():
  threading.Timer(60.0, printit).start()
  print "Hello, World!"
  time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print time
  for chunk in resFHL.iter_content():
    playFile.write(chunk)
    playTime.write(time)
printit()
#
#8 Record CornerHighLow odds every 60seconds
resCHL = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=CHL&isLiveBetting=false')
resCHL.raise_for_status()
playFile = open('8CHL.txt', 'wb')
playTime = open('8CHLtime.txt', 'wb')

def printit():
  threading.Timer(60.0, printit).start()
  print "Hello, World!"
  time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print time
  for chunk in resCHL.iter_content():
    playFile.write(chunk)
    playTime.write(time)
printit()
#
#10 Record Correct Score odds every 60seconds
resCRS = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=CRS&isLiveBetting=false')
resCRS.raise_for_status()
playFile = open('10CRS.txt', 'wb')
playTime = open('10CRStime.txt', 'wb')

def printit():
  threading.Timer(60.0, printit).start()
  print "Hello, World!"
  time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print time
  for chunk in resCRS.iter_content():
    playFile.write(chunk)
    playTime.write(time)
printit()
#
#11 Record FirstHalfCorrectScore odds every 60seconds
resFCS = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=FCS&isLiveBetting=false')
resFCS.raise_for_status()
playFile = open('11FCS.txt', 'wb')
playTime = open('11FCStime.txt', 'wb')

def printit():
  threading.Timer(60.0, printit).start()
  print "Hello, World!"
  time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print time
  for chunk in resFCS.iter_content():
    playFile.write(chunk)
    playTime.write(time)
printit()
#
#12 Record FirstTeamToScore odds every 60seconds
resFTS = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=FTS&isLiveBetting=false')
resFTS.raise_for_status()
playFile = open('12FTS.txt', 'wb')
playTime = open('12FTStime.txt', 'wb')

def printit():
  threading.Timer(60.0, printit).start()
  print "Hello, World!"
  time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print time
  for chunk in resFTS.iter_content():
    playFile.write(chunk)
    playTime.write(time)
printit()
#
#13 Record TotalGoals odds every 60seconds
resTTG = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=TTG&isLiveBetting=false')
resTTG.raise_for_status()
playFile = open('13TTG.txt', 'wb')
playTime = open('13TTGtime.txt', 'wb')

def printit():
  threading.Timer(60.0, printit).start()
  print "Hello, World!"
  time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print time
  for chunk in resTTG.iter_content():
    playFile.write(chunk)
    playTime.write(time)
printit()
#
#14 Record OddsEven odds every 60seconds
resOOE = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=OOE&isLiveBetting=false')
resOOE.raise_for_status()
playFile = open('14OOE.txt', 'wb')
playTime = open('14OOEtime.txt', 'wb')

def printit():
  threading.Timer(60.0, printit).start()
  print "Hello, World!"
  time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print time
  for chunk in resOOE.iter_content():
    playFile.write(chunk)
    playTime.write(time)
printit()
#
#16 Record HalfFull odds every 60seconds
resHFT = requests.get('http://bet.hkjc.com/football/getXML.aspx?pooltype=HFT&isLiveBetting=false')
resHFT.raise_for_status()
playFile = open('16HFT.txt', 'wb')
playTime = open('16HFTtime.txt', 'wb')

def printit():
  threading.Timer(60.0, printit).start()
  print "Hello, World!"
  time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print time
  for chunk in resHFT.iter_content():
    playFile.write(chunk)
    playTime.write(time)
printit()
