import telegram.ext as tg
from telegram import ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.utils.helpers import mention_html
import re

def start(update: Update, _) -> None:
    chat = update.effective_chat
    msg = update.effective_message
    keyb = []
    keyb.append([InlineKeyboardButton(text="Add me to your chat ✅", url="http://t.me/MrsNiaBot?startgroup=true")])
    msg.reply_text("Heya\nI'm AntiChatUsernameBot\nI can restrict which contains public chat username messages", reply_markup=InlineKeyboardMarkup(keyb))

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
START = CommandHandler(["start", "ping"], start)
CLEAN_BLUE_TEXT_HANDLER = MessageHandler(
    Filters.text & Filters.chat_type.groups,
    clean_blue_text_must_click,
    run_async=True,
)
dispatcher.add_handler(CLEAN_BLUE_TEXT_HANDLER, USER)
dispatcher.add_handler(START)

updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)
