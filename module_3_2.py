
def send_email(message, recipient, sender = "university.help@gmail.com"):
    valid_sender = sender.endswith((".com",".ru",".net")) and "@" in sender
    valid_recipient = recipient.endswith((".com",".ru",".net")) and "@" in recipient
    if not valid_sender or not valid_recipient:
           message = "Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient
           print(message)
    elif sender == recipient:
       message = "Нельзя отправить письмо самому себе!"
       print(message)
    elif sender == "university.help@gmail.com":
       message = "Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient
       print(message)
    else:
       message = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient
       print(message)

    return message



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
