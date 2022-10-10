import re

def checkDateFormat(username):
    regex = "^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$"
    r = re.compile(regex)

    if(re.search(r, username)):
        print("Valid")
    else:
        print("Not Valid")

date1 = "abc@gmail.com"
checkDateFormat(date1)

date2 = "abc@def@gmail.kahscg"
checkDateFormat(date2)