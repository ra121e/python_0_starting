def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    for it in iterable:
        if function(it):
            yield it


# def main():
#     if ft_filter.__doc__ != filter.__doc__:
#         print("ft_filter docstring is different from filter docstring")
#     else:
#         print("yes, doc are the same")
#     print(ft_filter.__doc__)
#     print(filter.__doc__)

#     x = ft_filter(lambda x: x % 2 == 0, range(11))
#     print(next(x))
#     return


# if __name__ == "__main__":
#     main()
