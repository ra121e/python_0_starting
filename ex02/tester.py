# いろいろなデータ型を作って、それを引数にして呼び出したら
# 1. いろいろな型を受け取れて
# 2. オリジナルの型を取り出す
# という関数を作る

from find_ft_type import all_thing_is_obj

# 右辺で型を作り、左辺がその型を指すポインタみたいなもの
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# ポインタみたいなものを引数として関数に渡す。
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
# 文字列リテラルは文字列オブジェクトとして渡している
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))

# expectd output
# List : <class 'list'>$
# Tuple : <class 'tuple'>$
# Set : <class 'set'>$
# Dict : <class 'dict'>$
# Brian is in the kitchen : <class 'str'>$
# Toto is in the kitchen : <class 'str'>$
# Type not found$
# 42$
