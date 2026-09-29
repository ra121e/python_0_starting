from typing import Any


def all_thing_is_obj(x: Any):
    # listは型を表す値で、type()は型を返す関数
    if type(x) is list:
        print("list :", type(x))
    # isは型の判定結果を返す
    elif type(x) is tuple:
        print("tuple :", type(x))
    elif type(x) is set:
        print("set :", type(x))
    elif type(x) is dict:
        print("dict :", type(x))
    elif type(x) is str:
        print(f"{x} is in the kitchen :", type(x))
    else:
        print("Type not found")
    return (42)
