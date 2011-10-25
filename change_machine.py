import sys

def deduct(cents, denom):
    n = 0
    while cents >= denom:
        cents -= denom
        n += 1
    if n > 0:
        print "%d x %d cents" % (n, denom)
    return cents

def change_machine(cents):
    print "%d cents:" % cents
    cents = deduct(cents, 25)
    cents = deduct(cents, 10)
    cents = deduct(cents, 5)
    deduct(cents, 1)

for line in sys.stdin.readlines(): change_machine(int(line))
