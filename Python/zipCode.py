import re

def validateZIPCode(code):
    regex = "^[0-9]{5}(?:-[0-9]{4})?$"
    r = re.compile(regex)

    if(re.search(r, code)):
        print("Valid")
    else:
        print("Not Valid")

code1 = "76309"
validateZIPCode(code1)

code2 = "83468-2348"
validateZIPCode(code2)

code3 = "234445"
validateZIPCode(code3)