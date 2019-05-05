


class Error(Exception):
    pass

class ValueLargeError(Error):
    pass

class ValueSmallError(Error):
    pass


value = 10

try:
    my_value = int(input("Enter your value: "))
    if my_value < value:
        raise ValueSmallError
    elif my_value > value:
        raise ValueLargeError

    print("Congratulations buddy, u got it right!!!")

except ValueSmallError:
    print("This value is smaller than the default by {}".format(value-my_value))

except ValueLargeError:
    print("This value is larger than the default by {}".format(my_value-value))

