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

# Add a user to the premium list with an expiration date and plan
def add_premium_user(user_id, days=30, plan='Basic'):
    premium_users = load_premium_users()
    expiration_date = datetime.now() + timedelta(days=days)
    premium_users[str(user_id)] = {
        "expiration_date": expiration_date.isoformat(),
        "plan": plan
    }
    save_premium_users(premium_users)

# Check if a user is premium and return their plan
def get_user_plan(user_id):
    premium_users = load_premium_users()
    user_data = premium_users.get(str(user_id))
    if user_data:
        expiration_date = datetime.fromisoformat(user_data['expiration_date'])
        if datetime.now() < expiration_date:
            return user_data["plan"]
    return None

# Remove expired users
def remove_expired_premium_users():
    premium_users = load_premium_users()
    current_time = datetime.now()
    premium_users = {user_id: data for user_id, data in premium_users.items() if datetime.fromisoformat(data['expiration_date']) > current_time}
    save_premium_users(premium_users)

# Get storage limit based on plan
def get_storage_limit(user_id):
    plan = get_user_plan(user_id)
    if plan == 'Platinum':
        return 10 * 1024  # 10 GB
    elif plan == 'Basic':
        return 2 * 1024   # 2 GB
    return 0  # Non-premium users have 0 GB limit
