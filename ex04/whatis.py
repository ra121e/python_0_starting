import sys

print(sys.argv[0])

if len(sys.argv) != 2:
    print("wrong argument number")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("wrong argument type. Need an integer.")
    sys.exit(1)
if n % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")

# expected output
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