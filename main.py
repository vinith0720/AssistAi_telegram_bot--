from telegram.ext import *
import constant as key
import google.generativeai as geai
import gemini as gem

print('Starting a bot....')


async def start_command(update, context):
    await update.message.reply_text('Hello! Welcome To Assist AI')


async def website(update, context):
    await update.message.reply_text("AssistAi website : https://assist-ai-pi.vercel.app/signin")


async def help(update, context):
    await update.message.reply_text("""
    /start -> start the bot
    /website -> provide the link for website
    /help -> to help you
    """)

async def gemini_handler(update, context):
    user_message = update.message.text.strip()
    
    try:
        gem.convo.send_message(user_message)
        await update.message.reply_text(gem.convo.last.text)

    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")



if __name__ == '__main__':
    application = Application.builder().token(key.API_key).build()

    # Commands
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('website', website))
    application.add_handler(CommandHandler('help', help))

    # Message Handler for Gemini
    #application.add_handler(MessageHandler(filters.Text & ~ filters.Command, gemini_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gemini_handler))

    #application.add_handler(MessageHandler(Filters.text & ~Filters.command, gemini_handler))


    # Run bot
    application.run_polling(1.0)
