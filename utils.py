def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

def validate_date(date):
    if len(date) != 10:
        raise ValueError("Invalid date format")
