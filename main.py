import random

from datetime import datetime

# Task 1

def get_days_from_today(user_input):
    try:
        user_date = datetime.strptime(user_input, '%Y-%m-%d')
    except ValueError:
        try:
            user_date = datetime.strptime(user_input, '%Y')
            user_date = datetime(user_date.year, 1, 1)
        except ValueError:
            return None

    current_date = datetime.now()

    delta_days = (user_date - current_date).days
    return delta_days

# Task 2

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 100 or quantity < 1 or quantity > (max - min + 1):
        return []
    unique_nums = random.sample(range(min, max + 1), quantity)
    return sorted(unique_nums)
lottery_numbers = get_numbers_ticket(1, 100, 10)
