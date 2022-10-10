import re

def checkPasswordStrength(password):
    regex = "(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,})"
    r = re.compile(regex)

    if(re.search(r, password)):
        print("Strong Password")
    else:
        print("Weak Password")

password1 = "Hiuahd$5jawd"
checkPasswordStrength(password1)

password2 = "my_password"
checkPasswordStrength(password2)