import sys

def print_denom(n, denom):
    if n > 0: print "%d x %d cents" % (n, denom)

def change_machine(cents):
    quarters, dimes, nickels, pennies = 0, 0, 0, 0

    while cents >= 25:
        cents -= 25
        quarters += 1
    print_denom(quarters, 25)

    while cents >= 10:
        cents -= 10
        dimes += 1
    print_denom(dimes, 10)

    while cents >= 5:
        cents -= 5
        nickels += 1
    print_denom(nickels, 5)

    while cents >= 1:
        cents -= 1
        pennies += 1
    print_denom(pennies, 1)

for line in sys.stdin.readlines():
    cents = int(line)
    print "%d cents:" % cents
    print 
