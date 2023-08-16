from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.mime.text import MIMEText
from email import encoders
from typing import List

from settings import USER


class Message():

    def __init__(self, to_users: str = USER, subject: str = "Без заголовка", files: List = None):
        self.to_user = to_users
        self.subject = subject
        self.files = files

    # создаем сообщение типа MIMEMultipart и возвращаем его
    def create_message(self, text: str = "") -> MIMEMultipart:
        message = MIMEMultipart()
        message["From"] = USER
        message["Subject"] = self.subject
        message["Date"] = formatdate(localtime=True)
        message["To"] = self.to_user
        if text:
            message.attach(MIMEText(text, "html"))
        if self.files:
            for file in self.files:
                message.attach(self.add_file_in_message(file))
        message["Charset"] = "utf-8"
        return message

    # добавляем файл к письму
    def add_file_in_message(self, file: str) -> MIMEBase:
        attachment = MIMEBase('application', "octet-stream")
        header = 'Content-Disposition', f'attachment; filename="{file}"'
        with open(file, "rb") as fh:
            data = fh.read()
        attachment.set_payload(data)
        encoders.encode_base64(attachment)
        attachment.add_header(*header)
        return attachment

