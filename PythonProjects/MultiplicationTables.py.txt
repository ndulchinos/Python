for i in range(1, 13):
   Str = ""
   for j in range(1, 13):
       if(len(str(i*j)) == 1):
           Str = Str + "   " + str(i*j)
       elif(len(str(i*j)) == 2):
           Str = Str + "  " + str(i*j)
       else:
           Str = Str + " " + str(i*j)
   print(Str)