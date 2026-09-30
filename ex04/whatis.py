import sys

print(sys.argv[0])

if len(sys.argv) != 2:
    print("wrong argument number")
    sys.exit(1)

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