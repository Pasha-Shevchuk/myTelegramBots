from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp
import os

# YouTube audio downloader function
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

# Handle YouTube links
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "youtube.com" in text or "youtu.be" in text:
        await update.message.reply_text("Downloading audio, please wait...")
        try:
            file_path = download_audio(text)
            with open(file_path, 'rb') as audio:
                await update.message.reply_audio(audio)
            os.remove(file_path)  # Clean up after sending
        except Exception as e:
            await update.message.reply_text(f"Error: {e}")

# Main function
def main():
    application = Application.builder().token("7927008329:AAHjDDu7LiERoa-K4WA_M0a_hbIBzFWGc6A").build()

    # Add a handler for regular text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
