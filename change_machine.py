import sys
for i in map(int,sys.stdin.readlines()):
 print i,"cents:"
 if i/25:print i/25,"x 25 cents";i%=25
 if i/10:print i/10,"x 10 cents";i%=10
 if i/5:print i/5,"x 5 cents";i%=5
 if i:print i,"x 1 cents"
 print
