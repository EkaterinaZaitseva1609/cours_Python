from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


def hi_comand(update: Update, context: ContextTypes.DEFAULT_TYPE): update.message.reply_text(f'Hi {update.effective_user.first_name} !')

def help_comand(update: Update, context: ContextTypes.DEFAULT_TYPE): update.message.reply_text(f'/hi\n/time\n/help')

def time_comand(update: Update, context: ContextTypes.DEFAULT_TYPE): update.message.reply_text(f'{datetime.datetime.now().time()}')

# def help_comand(update: Update, context: ContextTypes.DEFAULT_TYPE): update.message.reply_text(f'')



