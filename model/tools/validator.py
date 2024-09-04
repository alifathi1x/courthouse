import re


def name_validator(name):
    return re.match(r"^[a-zA-Z\s]{1,30}$", name)
