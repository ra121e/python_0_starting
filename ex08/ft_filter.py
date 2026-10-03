def ft_filter(function, iterable):
    """
    This function takes a function and an iterable as arguments
    and returns a new iterable containing only the elements
    for which the function returns True
    """
    for it in iterable:
        if function(it):
            yield it

def main():
    print(ft_filter.__doc__)

    x = ft_filter(lambda x: x % 2 == 0, range(11))
    print(next(x))
    return




if __name__ == "__main__":
    main()
