class Invalid_ageException(Exception):
    pass 
number=18
try :
    numm=12
    if numm<=number:
        raise Invalid_ageException
    else:
        print("eligible for work")
except Invalid_ageException:
    print("the age  iss less than 18")