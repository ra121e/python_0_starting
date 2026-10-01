import sys


def main():
    """This program counts the number of characters in a given text and categorizes them into upper letters, lower letters, punctuation marks, spaces, and digits."""
    try:
        if (len(sys.argv) > 2):
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print("AssertionError: ", e)
        return
    if len(sys.argv) < 2:
        print("What is the text to count?")
        text = sys.stdin.read()
    else:
        text = sys.argv[1]
    
    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    digit = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower = lower + 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            digit += 1
        else:
            punctuation += 1
    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")

if __name__ == "__main__":
    main()

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


