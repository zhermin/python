import telegram, logging, requests, random, re, time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

class RunBot():

    def __init__(self, TOKEN):
    
        self.bot = telegram.Bot(token=TOKEN)
        #print(self.bot.get_me())

        self.updater = Updater(token=TOKEN, use_context=True)
        dispatcher = self.updater.dispatcher

        # receives command messages, ie. messages starting with "/"
        start_handler = CommandHandler("start", self.start)
        dispatcher.add_handler(start_handler)

        dice_handler = CommandHandler("dice", self.dice)
        dispatcher.add_handler(dice_handler)

        ask_handler = CommandHandler("ask", self.ask)
        dispatcher.add_handler(ask_handler)

        location_handler = CommandHandler("location", self.location)
        dispatcher.add_handler(location_handler)

        boop_handler = CommandHandler("boop", self.boop)
        dispatcher.add_handler(boop_handler)

        # receives normal messages, ie. messages WITHOUT "/"
        echo_handler = MessageHandler(Filters.text, self.echo)
        dispatcher.add_handler(echo_handler)

    def start_polling(self):

        self.updater.start_polling()

    def start(self, update, context):

        user = update.message.from_user.first_name
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        #time.sleep(3)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Hi, {user}! How can I help you today?")

    def dice(self, update, context):

        context.bot.send_message(chat_id=update.message.chat_id, text=f"You've rolled a {random.randint(1,7)}!")

    def build_menu(self, buttons, n_cols, header_buttons=None, footer_buttons=None):

        menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
        if header_buttons:
            menu.insert(0, [header_buttons])
        if footer_buttons:
            menu.append([footer_buttons])
        return menu

    def ask(self, update, context):

        #telegram.ut
        button_list = [
            telegram.InlineKeyboardButton("col1", callback_data="..."),
            telegram.InlineKeyboardButton("col2", callback_data="..."),
            telegram.InlineKeyboardButton("row 2", callback_data="...")
        ]
        reply_markup = telegram.InlineKeyboardMarkup(self.build_menu(button_list, n_cols=2))
        context.bot.send_message(chat_id=update.message.chat_id, text="A two-column menu", reply_markup=reply_markup)

    def location(self, update, context):

        location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)
        contact_keyboard = telegram.KeyboardButton(text="send_contact", request_contact=True)
        custom_keyboard = [[ location_keyboard, contact_keyboard ]]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.message.chat_id, text="Would you mind sharing your location and contact with me?", reply_markup=reply_markup)

        reply_markup = telegram.ReplyKeyboardRemove()
        context.bot.send_message(chat_id=update.message.chat_id, text="I'm back.", reply_markup=reply_markup)

    def boop(self, update, context):

        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.message.chat_id, text=self.get_doggo())

    def get_doggo(self):

        exts = ["jpg","jpeg","png"]
        while True:
            
            doggo_url = requests.get("https://random.dog/woof.json").json()["url"]
            urlext = re.search("([^.]*)$",doggo_url).group(1).lower()

            if urlext not in exts:
                continue
                
            return doggo_url

    def echo(self, update, context):

        context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

if __name__ == "__main__":
    TOKEN = "765431250:AAELDaqtJ8th4ukHwEGlx00Ztdb2bwWnpj0"
    RunBot(TOKEN).start_polling()