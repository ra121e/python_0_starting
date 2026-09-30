import sys

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])

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