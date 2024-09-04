import re


def name_validator(name):
    return re.match(r"^[a-zA-Z\s]{1,30}$", name)

def national_id_validator(national_id):
    return re.match("^[0-9]{1,10}$", national_id)