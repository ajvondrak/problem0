import sys
for i in map(int,sys.stdin.readlines()):
 print i,"cents:"
 if (i/25):print i/25,"x 25 cents"
 if (i%25/10):print i%25/10,"x 10 cents"
 if (i%25%10/5):print i%25%10/5,"x 5 cents"
 if (i%25%10%5):print i%25%10%5,"x 1 cents"
 print
