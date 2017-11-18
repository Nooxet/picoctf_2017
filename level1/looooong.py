#!/usr/bin/python3

import sys

lett = sys.argv[1]
rep = int(sys.argv[2])
num = sys.argv[3]

print (''.join(lett for i in range(rep)) + num)
