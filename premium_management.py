import json
from datetime import datetime, timedelta

PREMIUM_FILE = 'premium_users.json'

# Define subscription plans and features
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

# Add or update premium user to the JSON file
def add_premium_user(user_id, days=30, plan='Basic'):
    if plan not in SUBSCRIPTION_PLANS:
        raise ValueError("Invalid subscription plan.")

    premium_users = load_premium_users()
    expiration_date = (datetime.now() + timedelta(days=days)).isoformat()

    # Check if the user already exists
    for user in premium_users:
        if user['user_id'] == user_id:
            user['expiration_date'] = expiration_date
            user['plan'] = plan
            break
    else:
        premium_users.append({
            "user_id": user_id,
            "expiration_date": expiration_date,
            "plan": plan
        })

    save_premium_users(premium_users)

# Check if a user is premium and get their features
def is_user_premium(user_id):
    premium_users = load_premium_users()
    for user in premium_users:
        if user['user_id'] == user_id:
            if datetime.fromisoformat(user['expiration_date']) > datetime.now():
                plan = user['plan']
                return True, plan, SUBSCRIPTION_PLANS[plan]  # Return plan and features
    return False, None, None

# Remove expired users
def remove_expired_users():
    premium_users = load_premium_users()
    premium_users = [user for user in premium_users if datetime.fromisoformat(user['expiration_date']) > datetime.now()]
    save_premium_users(premium_users)

# Example Usage
if __name__ == "__main__":
    remove_expired_users()  # Call this to clean up expired users regularly
