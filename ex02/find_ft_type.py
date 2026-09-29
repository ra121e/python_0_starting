from typing import Any


def all_thing_is_obj(x: Any):
    # listは型を表す値で、type()は型を返す関数
    if type(x) == list:
        print("list:", type(x))
    # isは型の判定結果を返す
    elif type(x) is tuple:
        print("tuple:", type(x))
    else:
        print(type(x))
    return (42)
