import sys


def main():
    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "0": "----- ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. "
                    }
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print("AssertionError:", e)
        return
    try:
        code = ""
        for char in sys.argv[1]:
            if char.upper() not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
            code += NESTED_MORSE[char.upper()]
        print(code)
    except AssertionError as e:
        print("AssertionError:", e)
        return


if __name__ == "__main__":
    main()

# must use the dictionary defined in morse.py
# NESTED_MORSE = { " ": "/ ",
# "A": ".- ",
# ...

# expected output:
# $> python sos.py "sos" | cat -e
# ... --- ...$
# $> python sos.py 'h$llo'
# AssertionError: the arguments are bad
# $>
