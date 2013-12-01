LBA11 = open("LBATrips11.txt","r") #opens the list of trips for LBA in 2011. the rest of these lines do the same for other partitions/years
LBA12 = open("LBATrips12.txt","r")
LBA13 = open("LBATrips13.txt","r")
EBA11 = open("EBATrips11.txt","r")
EBA12 = open("EBATrips12.txt","r")
EBA13 = open("EBATrips13.txt","r")
LBC11 = open("LBCTrips11.txt","r")
EBC11 = open("EBCTrips11.txt","r")
EBC12 = open("EBCTrips12.txt","r")
EBC13 = open("EBCTrips13.txt","r")
LBC12 = open("LBCTrips12.txt","r")
LBC13 = open("LBCTrips13.txt","r")

LBA = open("LBATrips.txt","wb") #opens the destination file 
LBC = open("LBCTrips.txt","wb")
EBA = open("EBATrips.txt","wb")
EBC = open("EBCTrips.txt","wb")

Trips11 = LBA11.readlines() #makes a list out of the lines of LBATrips11.txt
Trips12 = LBA12.readlines()
Trips13 = LBA13.readlines()

for i in range(64): #loop over the modules in a partitions. 
    l = Trips11[i]
    m = Trips12[i]
    n = Trips13[i]
    sNum11 = l[6:] #picks out the last characters in the line in consideration
    sNum12 = m[6:]
    sNum13 = n[6:]
    Num11 = int(sNum11) #converts the last characters into numbers so that we can use them as numbers
    Num12 = int(sNum12)
    Num13 = int(sNum13)
    Sum = Num11 + Num12 + Num13
    if i < 9: #when i is <9, we want the string to be "0i" not "i"
        num = str(i+1)
        num = "0" + num
    else:
        num = str(i+1)
    sum = str(Sum)
    LBA.write("LBA") #write to the data file
    LBA.write(num )
    LBA.write(" ")
    LBA.write(sum)
    LBA.write("\n")

Trips11 = EBA11.readlines() #restart the process, for EBA, then LBA, then LBC
Trips12 = EBA12.readlines()
Trips13 = EBA13.readlines()

for i in range(64):
    l = Trips11[i]
    m = Trips12[i]
    n = Trips13[i]
    sNum11 = l[6:]
    sNum12 = m[6:]
    sNum13 = n[6:]
    Num11 = int(sNum11)
    Num12 = int(sNum12)
    Num13 = int(sNum13)
    Sum = Num11 + Num12 + Num13
    if i < 9:
        num = str(i+1)
        num = "0" + num
    else:
        num = str(i+1)
    sum = str(Sum)
    EBA.write("EBA")
    EBA.write(num )
    EBA.write(" ")
    EBA.write(sum)
    EBA.write("\n")

Trips11 = LBC11.readlines()
Trips12 = LBC12.readlines()
Trips13 = LBC13.readlines()

for i in range(64):
    l = Trips11[i]
    m = Trips12[i]
    n = Trips13[i]
    sNum11 = l[6:]
    sNum12 = m[6:]
    sNum13 = n[6:]
    Num11 = int(sNum11)
    Num12 = int(sNum12)
    Num13 = int(sNum13)
    Sum = Num11 + Num12 + Num13
    if i < 9:
        num = str(i+1)
        num = "0" + num
    else:
        num = str(i+1)
    sum = str(Sum)
    LBC.write("LBC")
    LBC.write(num )
    LBC.write(" ")
    LBC.write(sum)
    LBC.write("\n")
  
Trips11 = EBC11.readlines()
Trips12 = EBC12.readlines()
Trips13 = EBC13.readlines()

for i in range(64):
    l = Trips11[i]
    m = Trips12[i]
    n = Trips13[i]
    sNum11 = l[6:]
    sNum12 = m[6:]
    sNum13 = n[6:]
    Num11 = int(sNum11)
    Num12 = int(sNum12)
    Num13 = int(sNum13)
    Sum = Num11 + Num12 + Num13
    if i < 9:
        num = str(i+1)
        num = "0" + num
    else:
        num = str(i+1)
    sum = str(Sum)
    EBC.write("EBC")
    EBC.write(num )
    EBC.write(" ")
    EBC.write(sum)
    EBC.write("\n")

LBA.close
EBA.close
EBC.close
LBC.close  
