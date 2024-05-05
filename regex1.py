import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check (email):
    if (re.fullmatch(regex,email)):
        print("valid Email")
    else:
        print("Invalid Email")
if __name__ == '__main__':
    email = "ankitarutu326@gmail.com"
    check(email)
    email = "my.ownsite@our-earth.org"
    check(email)
    email = "ankitrai326.com"
    check(email)