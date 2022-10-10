import re

def checkEmptyString(str):
    regex = "^\s*$"
    r = re.compile(regex)

    if(re.search(r, str)):
        print("The given string is empty and it only contains whitespaces")
    else:
        print("The given string is not empty")

str1 = "              "
checkEmptyString(str1)

str2 = "This is not an empty string"
checkEmptyString(str2)