import math #this is to use the square root function

EBATrips=open("EBATrips.txt","r") #opens "data" file for trips in EBA
EBCTrips=open("EBCTrips.txt","r")
LBATrips=open("LBATrips.txt","r")
LBCTrips=open("LBCTrips.txt","r")

EBAList=EBATrips.readlines() #makes a list of strings using the lines of EBATrips.txt
EBCList=EBCTrips.readlines()
LBAList=LBATrips.readlines()
LBCList=LBCTrips.readlines()

fo = open("output.txt","wb") #opens a file to write out the results

#Compute averages
Sum=0
for line in EBAList:
  x=line[6:] #get the last lines in the string, which should be the number of trips
  y=int(x)   #convert this string into a number, so that we can use it like a number
  Sum=Sum+y
EBAavg = Sum / 64
SigmaEBA = 0 #initialize the calculation for SigmaEBA
for line in EBAList:
  x=line[6:]
  y=int(x)
  z = y - EBAavg #start computation of the standard deviation
  z = z**(2) #this notation means to square z
  SigmaEBA = SigmaEBA + z
SigmaEBA = SigmaEBA / 64
SigmaEBA = math.sqrt(SigmaEBA)
print SigmaEBA #debug info
print EBAavg
TwoSigma = 2*(SigmaEBA)+ EBAavg #this is the number 2 sigma above the average
fo.write("greater than 2 sigma \n")
for line in EBAList:
  x=line[6:]
  y=int(x)
  if y >= TwoSigma: #picks out the modules with number of trips 2 sigma above average
    fo.write(line[:5])
    fo.write("\n") 
ThreeSigma = 3*(SigmaEBA) + EBAavg #repeat the above work, but for 3 sigma
fo.write("greater than 3 sigma \n")
for line in EBAList:
  x=line[6:]
  y=int(x)
  if y >= ThreeSigma:
    fo.write(line[:5])
    fo.write("\n")
    
Sum=0 #reset this variable, redo all computations for EBC, LBC, LBA:
for line in EBCList:
  x=line[6:]
  y=int(x)
  Sum=Sum+y
EBCavg = Sum / 64
SigmaEBC = 0
for line in EBCList:
  x=line[6:]
  y=int(x)
  z = y - EBCavg
  z = z**(2)
  SigmaEBC = SigmaEBC + z
SigmaEBC = SigmaEBC / 64
SigmaEBC = math.sqrt(SigmaEBC)
print SigmaEBC
print EBCavg
TwoSigma = 2*(SigmaEBC)+ EBCavg
fo.write("greater than 2 sigma \n")
for line in EBCList:
  x=line[6:]
  y=int(x)
  if y >= TwoSigma:
    fo.write(line[:5])
    fo.write("\n")
ThreeSigma = 3*(SigmaEBC) + EBCavg
fo.write("greater than 3 sigma \n")
for line in EBCList:
  x=line[6:]
  y=int(x)
  if y >= ThreeSigma:
    fo.write(line[:5])
    fo.write("\n")
    
Sum=0
for line in LBAList:
  x=line[6:]
  y=int(x)
  Sum=Sum+y
LBAavg = Sum / 64
SigmaLBA = 0
for line in LBAList:
  x=line[6:]
  y=int(x)
  z = y - LBAavg
  z = z**2
  SigmaLBA = SigmaLBA + z
SigmaLBA = SigmaLBA / 64
SigmaLBA = math.sqrt(SigmaLBA)
print SigmaLBA
print LBAavg
TwoSigma = 2*(SigmaLBA)+ LBAavg
fo.write("greater than 2 sigma \n")
for line in LBAList:
  x=line[6:]
  y=int(x)
  if y >= TwoSigma:
    fo.write(line[:5])
    fo.write("\n")
ThreeSigma = 3*(SigmaLBA) + LBAavg
fo.write("greater than 3 sigma \n")
for line in LBAList:
  x=line[6:]
  y=int(x)
  if y >= ThreeSigma:
    fo.write(line[:5])
    fo.write("\n")
    
Sum=0
for line in LBCList:
  x=line[6:]
  y=int(x)
  Sum=Sum+y
LBCavg = Sum / 64
SigmaLBC = 0
for line in LBCList:
  x=line[6:]
  y=int(x)
  z = y - LBCavg
  z = z**(2)
  SigmaLBC = SigmaLBC + z
SigmaLBC = SigmaLBC / 64
SigmaLBC = math.sqrt(SigmaLBC)
print SigmaLBC
print LBCavg
TwoSigma = 2*(SigmaLBC)+ LBCavg
fo.write("greater than 2 sigma \n")
for line in LBCList:
  x=line[6:]
  y=int(x)
  if y >= TwoSigma:
    fo.write(line[:5])
    fo.write("\n")
ThreeSigma = 3*(SigmaLBC) + LBCavg
fo.write("greater than 3 sigma \n")
for line in LBCList:
  x=line[6:]
  y=int(x)
  if y >= ThreeSigma:
    fo.write(line[:5])
    fo.write("\n")
fo.close()
