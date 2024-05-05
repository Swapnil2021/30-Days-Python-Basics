# program to find sum of multiple numbers Atribute Arguments
def find_sum(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print("sum = " , result)
find_sum(1,2,3)
find_sum(1,2,3,4,5,6)    
    