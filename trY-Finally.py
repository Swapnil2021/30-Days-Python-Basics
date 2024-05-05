try :
    num1 = 12
    num2=0
    c=num1/num2
    print(c)
except ZeroDivisionError:
    print("num 2 should not be zero")
finally:
    print("the divisor is")
    exit()    
    print("the divisor is ")