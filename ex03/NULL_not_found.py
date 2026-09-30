from typing import Any

def NULL_not_found(x: Any) -> int:
    if x is None:
        print("Nothing: None ", type(x))
    elif x != x:
        print("Cheese: nan ", type(x))
    elif x == 0 and type(x) is int:
        print("Zero: 0 ", type(x))
    elif x == "":
        print("Empty: " , type(x))
    elif x == False:
        print("Fake: False ", type(x))
    else:
        print("Type not Found")
    return (1)
