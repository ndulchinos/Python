import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    oStr = test
    Str = ""
    for n in range(1, 100):
       for i in range(len(oStr) - 1,-1,-1):
           Str = Str + oStr[i]
       x = int(Str)
       y = int(oStr)
       if (x == y):
           print(str(n-1) + " " + Str)
           break
       else:
           oStr = str( x + y )
           Str = ""
test_cases.close()