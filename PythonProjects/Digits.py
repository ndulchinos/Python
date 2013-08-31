import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    k = 0
    for i in range(0, len(test) - 1):
        k = k + int(test[i])
    print(k)

test_cases.close()