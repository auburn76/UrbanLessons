
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if (recipient.find('@') == -1 or
        (recipient.find('.com') != (len(recipient)-4) and
         recipient.find('.ru') != (len(recipient)-3) and
         recipient.find('.net') != (len(recipient)-4))):
        print('Невозможно отправить письмо на адрес',recipient, '.')
    elif (sender.find('@') == -1 or
          (sender.find('.com') != (len(sender)-4) and
           sender.find('.ru') != (len(sender)-3) and
           sender.find('.net') != (len(sender)-4))):
        print('Невозможно отправить письмо с адреса', sender, '.')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес',recipient, '.')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient, '.')
    return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Вы посылаете письмо за границу. Может, Вы шпион?', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')