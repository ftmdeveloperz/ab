import json
from telegram import Update
from telegram.ext import CallbackContext
from premium_management import is_user_premium

CLONE_FILE = 'cloned_bots.json'

# Load cloned bots from JSON file
def load_cloned_bots():
    try:
        with open(CLONE_FILE, 'r') as f:
            data = json.load(f)
            return data.get("cloned_bots", [])
    except FileNotFoundError:
        return []

# Save cloned bots to JSON file
def save_cloned_bots(cloned_bots):
    with open(CLONE_FILE, 'w') as f:
        json.dump({"cloned_bots": cloned_bots}, f, indent=4)

# Clone a bot
def clone_bot(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    bot_token = context.args[0] if context.args else None

    # Check if the user is premium
    is_premium, plan, features = is_user_premium(user_id)
    
    if not is_premium:
        update.message.reply_text("This feature is available for premium users only.")
        return

    if bot_token is None:
        update.message.reply_text("Please provide the bot token to clone.")
        return

    # You can add additional logic to validate the bot token here

    cloned_bots = load_cloned_bots()
    
    # Check if the bot is already cloned
    for bot in cloned_bots:
        if bot['token'] == bot_token:
            update.message.reply_text("This bot has already been cloned.")
            return

    # Add the new cloned bot to the list
    cloned_bots.append({
        "user_id": user_id,
        "token": bot_token
    })

    save_cloned_bots(cloned_bots)
    update.message.reply_text("Bot cloned successfully!")

# Example Usage
if __name__ == "__main__":
    print("Clone module ready.")
