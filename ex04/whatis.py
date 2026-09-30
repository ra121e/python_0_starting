import sys

if len(sys.argv) != 2:
    print("wrong argument number")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except Exception as e:
    try:
        raise AssertionError("hello")
    except AssertionError as e:
        print("AssertionError:", e)
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

# assertionError output
# $> python whatis.py Hi!
# AssertionError: argument is not an integer
# $>
# $> python whatis.py 13 5
# AssertionError: more than one argument is provided
# $>