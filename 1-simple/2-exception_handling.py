def spam(divideBy):
    try:    #Exception Handling
        return 42 / divideBy
    except ZeroDivisionError as e:
        print(e)    #prints default error message of ZeroDivisionError


print(spam(2))
print(spam(12))
print(spam(0)) #ZeroDivisionError
print(spam(1))
