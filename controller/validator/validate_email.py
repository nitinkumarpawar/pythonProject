import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def valid_email(email):
    if re.fullmatch(regex, email):
        print("Valid email")
        return email
    else:
        print("Invalid email")
        print("Please try again")
