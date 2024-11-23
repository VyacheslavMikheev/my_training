def send_email(message,recipient,*,sender = "university.help@gmail.com"):
     #Функция, с двумя обычными аргументами и одним, обязательно именованным.
     a = ("@" in recipient) and  ("@" in sender)
     #Переменная, для проверки содержания "@" в аргументах "recipient" и "sender".
     b =   sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net")
     # Переменная, для проверки окончания "sender", согласно условию.
     c =   recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")
     # Переменная, для проверки окончания "recipient", согласно условию.
     if  a == False or b == False or c == False   == False :  # Первое условие.
        print("Невозможно отправить письмо с адреса " ,sender , "на адрес"  , recipient )  # Вывод при соответствии.
     elif recipient == sender : # Проверка условия совпадения аргументов.
          print ("Нельзя отправить письмо самому себе!")  # Вывод при соответствии.
     elif sender == "university.help@gmail.com" :  # Проверка соответствия аргумента.
          print("Письмо успешно отправлено с адреса " ,sender, "на адрес" , recipient)  # Вывод при соответствии.
     else:
          print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса" , sender , "на адрес" , "recipient")
     # Вывод в ином случае.

# Далее пример выполнения.

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')