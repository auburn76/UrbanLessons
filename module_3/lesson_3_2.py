
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if recipient.in('@') == False or sender.in('@'):
        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ',recipient)
