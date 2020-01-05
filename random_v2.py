import sys
from random import randint

if sys.argv[1] == "-nish" and sys.argv[3] == "-qanak":
    i = int(sys.argv[2])
    range_start = int(10**(i-1))
    range_end = int((10**i)-1)
    q = int(sys.argv[4])
    if q == 0:
        while True:
            print(str(randint(range_start, range_end)) + " ")
    else:
        b = 0
        while b < q:
            print(str(randint(range_start, range_end)) + " ")
            b += 1

else:
    print("error")