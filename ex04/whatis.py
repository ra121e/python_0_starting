import sys

if len(sys.argv) != 2:
    print("wrong argument number")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Argument should be interger")

if n % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")


# $> python whatis.py 14
# I'm Even.
# $>
# $> python whatis.py -5
# I'm Odd.
# $>
# $> python whatis.py
# $>
# $> python whatis.py 0
# I'm Even.
# $>
