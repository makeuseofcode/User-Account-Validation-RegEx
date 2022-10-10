import re

def checkUsername(username):
    regex = "^[A-Za-z]\\w{5,29}$"
    r = re.compile(regex)

    if(re.search(r, username)):
        print("Valid")
    else:
        print("Not Valid")

username1 = "yuvraj_chandra"
checkUsername(username1)

username2 = "ja7&^%87"
checkUsername(username2)