from math import factorial


def sum_of_digits(num):
    print(sum(int(i) for i in str(factorial(num))))


sum_of_digits(100)
