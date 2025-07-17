from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    keyboard = [
        [InlineKeyboardButton("Каталог", callback_data='catalog')],
        [InlineKeyboardButton("Корзина", callback_data='cart')],
        [InlineKeyboardButton("Помощь", callback_data='help')]
    ]
    return InlineKeyboardMarkup(keyboard)

def catalog_keyboard(items):
    keyboard = []
    for item in items:
        keyboard.append(
            [InlineKeyboardButton(item['name'], callback_data=f"item_{item['id']}")]
        )
    keyboard.append([InlineKeyboardButton("Назад", callback_data='main_menu')])
    return InlineKeyboardMarkup(keyboard)
