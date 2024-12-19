import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define the '/start' command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome! Send me a list of YouTube links separated by spaces or new lines, and I’ll process them."
    )

# Define the message handler to process YouTube links
async def process_links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.strip()

    # Split by spaces or new lines using regex
    links = text.split()

    for link in links:
        if "youtube.com" in link or "youtu.be" in link:
            await update.message.reply_text(f"Publishing: {link.strip()}")
        else:
            await update.message.reply_text(f"Invalid link: {link.strip()}")

# Main function to set up the bot and run it
def main() -> None:
    BOT_TOKEN = "8113355922:AAHA20T2XRTD6DtBp6SmgmqsR-1khOzu7pI"  # Replace with your actual token

    # Create the Application instance
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_links))

    # Run the bot
    application.run_polling()

# Entry point of the script
if __name__ == "__main__":
    main()
