import smtplib
from email.mime.multipart import MIMEMultipart
from settings import *


def send_email(message: MIMEMultipart, to_users: str):
    smtp_object = smtplib.SMTP(SERVER, PORT)
    sent = False
    try:
        smtp_object.starttls()
        smtp_object.login(USER, PASS)
        smtp_object.sendmail(USER, to_users, message.as_string())
        sent = True
    except smtplib.SMTPException as err:
        return {'text': "Письмо не отправлено. Возникла ошибка.", 'error':  err, 'result': False}
    finally:
        smtp_object.quit()
        if sent:
            return {'text': "Письмо успешно отправлено.", 'result': True}
        return {'text': "Письмо не отправлено. Что-то пошло не так.", 'result': True}

