import updater as updater
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Updater
from bots_comand import *




updater = Updater('5667924218:AAHZHJShM7KDNX0ueIBf83Ptxz64yvoZZwM')



updater.dispacher.add_handler(CommandHandler("hello", hi_comand))
updater.dispacher.add_handler(CommandHandler("time", time_comand))
updater.dispacher.add_handler(CommandHandler("help", help_comand))
# app.add_handler(CommandHandler("sum", sum_comand))

print('server stsrt')

# app.run_polling()






