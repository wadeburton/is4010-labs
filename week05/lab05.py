# lab05.py


def calculate_average_age(users):
    """Return the average numeric age, or 0.0 when none are valid."""
    valid_ages = []
    for user in users:
        if isinstance(user, dict):
            age = user.get("age")
            if isinstance(age, (int, float)) and not isinstance(age, bool):
                valid_ages.append(age)

    try:
        return sum(valid_ages) / len(valid_ages)
    except ZeroDivisionError:
        return 0.0


def get_active_user_emails(users):
    """Return email addresses belonging to active users."""
    emails = []
    for user in users:
        if isinstance(user, dict) and user.get("is_active") and "email" in user:
            emails.append(user["email"])
    return emails
