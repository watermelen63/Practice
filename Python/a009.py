import sys
n = sys.stdin.readline()
print(''.join(chr(ord(a) - 7) for a in n))