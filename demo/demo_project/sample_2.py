def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 100:
        raise ValueError("Age cannot be greater than 100")