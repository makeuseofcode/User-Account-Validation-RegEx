import re

def checkDateFormat(date):
    regex = "^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d$"
    r = re.compile(regex)

    if(re.search(r, date)):
        print("Valid")
    else:
        print("Not Valid")

date1 = "03/21/2002"
checkDateFormat(date1)

date2 = "21-03-2002"
checkDateFormat(date2)