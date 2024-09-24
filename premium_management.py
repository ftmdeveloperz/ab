import json
from datetime import datetime, timedelta

PREMIUM_FILE = 'premium_users.json'

# Define subscription plans and their features
SUBSCRIPTION_PLANS = {
    'Basic': {
        'max_upload': '2GB',
        'max_processing': '2GB',
        'features': [
            'Basic support',
            'Access to standard features'
        ]
    },
    'Platinum': {
        'max_upload': '10GB',
        'max_processing': '10GB',
        'features': [
            'Priority support',
            'Access to premium features',
            'Advanced tools'
        ]
    }
}

# Load premium users from JSON file
def load_premium_users():
    try:
        with open(PREMIUM_FILE, 'r') as f:
            data = json.load(f)
            return data.get("premium_users", [])
    except FileNotFoundError:
        return []

# Save premium users to JSON file
def save_premium_users(premium_users):
    with open(PREMIUM_FILE, 'w') as f:
        json.dump({"premium_users": premium_users}, f, indent=4)

# Add or update a premium user
def add_premium_user(user_id, days=30, plan='Basic'):
    if plan not in SUBSCRIPTION_PLANS:
        raise ValueError("Invalid subscription plan.")

    premium_users = load_premium_users()
    expiration_date = (datetime.now() + timedelta(days=days)).isoformat()

    # Check if the user already exists, update if found
    for user in premium_users:
        if user['user_id'] == user_id:
            user['expiration_date'] = expiration_date
            user['plan'] = plan
            break
    else:
        # Add new user
        premium_users.append({
            "user_id": user_id,
            "expiration_date": expiration_date,
            "plan": plan
        })

    save_premium_users(premium_users)

# Check if the user is premium and retrieve their plan and features
def is_user_premium(user_id):
    premium_users = load_premium_users()
    for user in premium_users:
        if user['user_id'] == user_id:
            if datetime.fromisoformat(user['expiration_date']) > datetime.now():
                plan = user['plan']
                return True, plan, SUBSCRIPTION_PLANS[plan]  # Return plan and its features
    return False, None, None
#ftmonly
def check_premium_status(user_id):
    """
    Check the premium status of a user.

    Args:
        user_id (str): The user ID to check.

    Returns:
        dict: A dictionary containing the premium status and expiration date.
    """
    return user_premium_status.get(user_id, {"is_premium": False})
# Remove a premium user from the list
def remove_premium_user(user_id):
    premium_users = load_premium_users()
    updated_users = [user for user in premium_users if user['user_id'] != user_id]
    save_premium_users(updated_users)
    return f"User {user_id} removed from premium list."

# Clean up expired users
def remove_expired_users():
    premium_users = load_premium_users()
    premium_users = [user for user in premium_users if datetime.fromisoformat(user['expiration_date']) > datetime.now()]
    save_premium_users(premium_users)

# Example function to regularly clean up expired users
if __name__ == "__main__":
    remove_expired_users()
