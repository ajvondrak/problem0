import sys
for i in map(int,sys.stdin):
 c="cents";x="x";print i,c+":"
 if i/25:print i/25,x,25,c;i%=25
 if i/10:print i/10,x,10,c;i%=10
 if i/5:print i/5,x,5,c;i%=5
 if i:print i,x,1,c
 print
