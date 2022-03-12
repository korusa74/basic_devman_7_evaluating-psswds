import urwid


def is_very_long(password):
    return len(password) >= 12


def has_digit(password):
    return any(letter.isdigit() for letter in password)


def has_letters(password):
    return any(letter.isalpha() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    return any((not l.isalpha() and not l.isdigit()) for l in password)


def on_ask_change(edit, new_edit_text):
    function_list = [
        is_very_long, 
        has_digit, 
        has_letters, 
        has_upper_letters, 
        has_lower_letters, 
        has_symbols,
    ]
    score = 0
    for function in function_list:
        if function(new_edit_text):
            score += 2
    new_edit_text = score
    reply.set_text("Рейтинг пароля: %s" % new_edit_text)


if __name__ == '__main__':
    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
