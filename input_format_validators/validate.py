from sys import stdin
import sys

MAXK = 100
MAXINT = 10000
cases = 0
line0 = stdin.readline()
num_cases = int(line0)
assert 1 <= num_cases <= 100, "invalid number of cases %d not in [1, 100]" % num_cases

while True:
    line1 = stdin.readline()
    line2 = stdin.readline()
    if len(line1) == 0 or len(line2) == 0:
        break
    num = int(line1)
    fv = [int(ele) for ele in line2.split(' ')]
    assert 1 <= num <= MAXK, "%s  not in [0, %s]" % (num, MAXK)
    cases += 1

assert 1 <= cases <= 100, "invalid number of cases %d not in [1, 100]" % cases

# Nothing to report
sys.exit(42)