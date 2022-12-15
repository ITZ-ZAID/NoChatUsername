from telegram import ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.utils.helpers import mention_html
import re

def clean_blue_text_must_click(update: Update, context: CallbackContext):
    bot = context.bot
    chat = update.effective_chat
    message = update.effective_message
    users = update.effective_user
    links = re.findall(r'@[^\s]+', message.text)
    if not links:
        return
    chat_admins = dispatcher.bot.getChatAdministrators(chat.id)
    admin_list = [x.user.id for x in chat_admins]
    if users.id in admin_list:
       return
    if chat.get_member(bot.id).can_delete_messages:
       if message.text:
          for link in links:
             try:
                 user = bot.get_chat(link)
                 print(user.id)
                 if len(str(user.id)) > 12:
                    message.reply_text(f"{users.first_name}, your message was hidden, chat usernames not allowed in this group.")
                    message.delete()
             except:
                 return

USER = 110
CLEAN_BLUE_TEXT_HANDLER = MessageHandler(
    Filters.text & Filters.chat_type.groups,
    clean_blue_text_must_click,
    run_async=True,
)
dispatcher.add_handler(CLEAN_BLUE_TEXT_HANDLER, USER)
