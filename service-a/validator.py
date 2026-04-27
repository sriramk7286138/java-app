import re
import validators

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if validators.email(email):
        return True
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def is_valid_name(name: str) -> bool:
    if not isinstance(name, str) or not name.strip():
        return False
    return re.match(r"^[A-Za-z\s]+$", name) is not None


def is_valid_age(age) -> bool:
    if age is None:
        return True
    try:
        age = int(age)
        return 15 <= age <= 100
    except:
        return False


def is_valid_cgpa(cgpa) -> bool:
    if cgpa is None:
        return True
    try:
        cgpa = float(cgpa)
        return 0.0 <= cgpa <= 10.0
    except:
        return False


def is_valid_roll_number(roll: str) -> bool:
    if not isinstance(roll, str):
        return False

    pattern = r"^[A-Z]{2}\d{7}$"
    return re.match(pattern, roll) is not None


def is_valid_record(record: dict) -> bool:
    return (
        is_valid_name(record.get("name")) and
        is_valid_email(record.get("email")) and
        is_valid_age(record.get("age")) and
        is_valid_cgpa(record.get("cgpa")) and
        is_valid_roll_number(record.get("rollNumber"))
    )