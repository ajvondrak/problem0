import sys
for i in map(int,sys.stdin):
 x="x %s cents";print i,"cents:"
 if i/25:print i/25,x%25;i%=25
 if i/10:print i/10,x%10;i%=10
 if i/5:print i/5,x%5
 if i%5:print i%5,x%1
 print
