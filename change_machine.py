import sys
for i in map(int,sys.stdin):
 print i,"cents:"
 for c in(25,10,5,1):
  if i/c:print i/c,"x",c,"cents";i%=c
 print