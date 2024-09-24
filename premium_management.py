import json
from datetime import datetime, timedelta

# Load premium users from JSON file
def load_premium_users():
    try:
        with open('premium_users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save premium users to JSON file
def save_premium_users(premium_users):
    with open('premium_users.json', 'w') as file:
        json.dump(premium_users, file, indent=4)

# Add a user to the premium list with an expiration date
def add_premium_user(user_id, days=30):
    premium_users = load_premium_users()
    expiration_date = datetime.now() + timedelta(days=days)
    premium_users[str(user_id)] = expiration_date.isoformat()
    save_premium_users(premium_users)

# Check if a user is premium
def is_premium_user(user_id):
    premium_users = load_premium_users()
    expiration_date_str = premium_users.get(str(user_id))
    if expiration_date_str:
        expiration_date = datetime.fromisoformat(expiration_date_str)
        return datetime.now() < expiration_date
    return False

# Remove expired users
def remove_expired_premium_users():
    premium_users = load_premium_users()
    current_time = datetime.now()
    premium_users = {user_id: exp for user_id, exp in premium_users.items() if datetime.fromisoformat(exp) > current_time}
    save_premium_users(premium_users)
