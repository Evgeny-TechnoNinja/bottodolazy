import data.settings_ui as ui
import utils.db
import utils.todo
from loader import BOT as bot, COLLECTION, KEYBOARD_MENU_MAIN as MENU_MAIN # noqa
import schedule


@bot.message_handler(commands=['start'])
def todo_start(message):
    user_registered_status = utils.db.add_user(message, COLLECTION)
    user_first_name = message.from_user.first_name
    if not user_registered_status:
        sticker = open(ui.sticker_path['returned'], 'rb')
        bot.send_sticker(message.from_user.id, sticker)
        quantity = utils.todo.quantity_tasks(utils.db.user_get_tasks(message, COLLECTION))
        text = ui.dialogue['user_returned'] \
            .format(user_first_name, ui.menu_list_items['important'].replace('й', 'х'),
                    quantity['important'],
                    ui.menu_list_items['ordinary'].replace('й', 'x'),
                    quantity['ordinary'])
        bot.send_message(message.from_user.id, text, reply_markup=MENU_MAIN,
                         parse_mode='HTML')
    else:
        bot_name = ui.bot_name
        sticker = open(ui.sticker_path['hello'], 'rb')
        bot.send_sticker(message.from_user.id, sticker)
        text = ui.dialogue['welcome_text'].format(user_first_name, bot_name)
        bot.send_message(message.from_user.id, text, reply_markup=MENU_MAIN)
    notifi_data = utils.db.user_get_notifications(message, COLLECTION)
    if notifi_data['notifications']:
        schedule.clear(message.from_user.id)
        job = utils.todo.run_notifi(message, notifi_data['notification_interval'])
    else:
        schedule.clear(message.from_user.id)

