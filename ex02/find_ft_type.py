from typing import Any


# type関数は値オブジェクトが指している型オブジェクトを取り出して返す
# isは左右のポインタが指している型が同一かどうかをチェックする
def all_thing_is_obj(x: Any):
    # listは型を表す型オブジェクト
    if type(x) is list:
        print("list :", type(x))
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
