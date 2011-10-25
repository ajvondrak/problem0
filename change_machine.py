import sys

for cents in map(int, sys.stdin.readlines()):
    print cents, "cents:"
    if (cents/25): print cents/25, "x 25 cents"
    if (cents%25/10): print cents%25/10, "x 10 cents"
    if (cents%25%10/5): print cents%25%10/5, "x 5 cents"
    if (cents%25%10%5): print cents%25%10%5, "x 1 cents"
    print
