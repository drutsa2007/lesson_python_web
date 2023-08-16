from send_email import send_email
from Message import Message

# Варианты заполнения кому:
# ["user@mail.ru"] - если одному человеку
# ["user1@mail.ru", "user2@mail.ru", "user3@mail.ru"] - если нескольким адресатам
to_users = ["user@mail.ru"]
to_users = ",".join(to_users)

# Варианты заполнения вложения:
# ["/path/to/file"] - если один файл
# ["/path/to/file1", "/path/to/file2", "/path/to/file3"] - если несколько файлов
files = ["fff.pdf", "fff1.pdf"]

# создаем объект письма
message = Message(
    subject="Тема письма",  # Тема письма
    to_users=to_users,  # если не указывать, то письмо себе
    files=files
)

# Можно в формате HTML, можно просто текст
text_message = """
<h2 style="color:#45da5c;">Текст сообщения</h2>"
"""

if __name__ == "__main__":
    send = send_email(message.create_message(text_message), to_users)
    if send['result']:
        print(send['text'])
    else:
        print(send['text'])
        print(send['error'])



