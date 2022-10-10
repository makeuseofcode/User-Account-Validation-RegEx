import re

def checkEmailId(username):
    regex = "^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$"
    r = re.compile(regex)

    if(re.search(r, username)):
        print("Valid")
    else:
        print("Not Valid")

email1 = "abc@gmail.com"
checkEmailId(email1)

email2 = "abc@def@gmail.kahscg"
checkEmailId(email2)