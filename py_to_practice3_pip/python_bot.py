from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *
import logging


logging.basicConfig(filename='botlog.txt',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logging.info('Started')
logging.info('Finished')

updater = Updater('5240692324:AAHuC2QwXpx2vIL8Sxd3TR8lTZSMFDn5p1g')
print('server start')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('mylove', love_command))

updater.start_polling()
updater.idle()
