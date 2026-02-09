
def validate_age(age):
    return 18 <= age <= 25


def validate_name(name):
    return bool(name.strip()) and len(name.strip()) >= 2

