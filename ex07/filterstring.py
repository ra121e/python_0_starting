import sys


def main():
    """This program filters a string by the given number"""
    try:
        if (len(sys.argv) != 3):
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print("AssertionError:", e)
        return
    try:
        n = int(sys.argv[2])
    except Exception:
        print("AssertionError: the arguments are bad")
        return

if __name__ == "__main__":
    main()

# expected output
# $> python filterstring.py 'Hello the World' 4
# ['Hello', 'World']
# $>

# $> python filterstring.py 'Hello the World' 99
# []
# $>

# $> python filterstring.py 3 'Hello the World'
# AssertionError: the arguments are bad
# $>

# $> python filterstring.py
# AssertionError: the arguments are bad
# $>
