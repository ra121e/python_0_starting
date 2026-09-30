import sys


def main():
    """This program counts the number of characters in a given text and categorizes them into upper letters, lower letters, punctuation marks, spaces, and digits."""
    try:
        if (len(sys.argv) != 2):
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print("AssertionError: ", e)
        return


if __name__ == "__main__":
    main()
    help(main)

# expected output
# $>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward
# compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
# The text contains 171 characters:
# 2 upper letters
# 121 lower letters
# 7 punctuation marks
# 26 spaces
# 15 digits
# $>


