try:
    even_number = [2,4,6,8,5,8,8]
    print(even_number[5])
except ZeroDivisionError :
    print("denominator can't be zero")
except IndexError :
    print("Index out of Bound")