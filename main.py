from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Salom')

def main():
    updater=Updater('6276492469:AAEbp6gAqx12oWNW2ENlCrx6zDhXQyYjtb8', context=True)

    dispatcher=updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

main()
