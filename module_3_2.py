def send_email(message, recipient, *, sender="university.help@gmail.com"):
    variants = ('.com', '.ru', '.net')            # создала кортеж с вариантами окончания строк
    if not recipient.lower().endswith(variants):  # проверяем без учета регистра заканчивается ли строка recipient заданными аргументами
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if not sender.lower().endswith(variants):  # проверяем без учета регистра заканчивается ли строка sender заданными аргументами
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if not ('@' in recipient) or not ('@' in sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return

    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!Письмо отправлено с адреса {sender} на адрес {recipient}.')
        return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')

