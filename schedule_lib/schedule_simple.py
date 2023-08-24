import schedule
import time


def worker():
    # Здесь запускается программа
    print("Запустилась функция")


# каждые 3 секунды
schedule.every(3).seconds.do(worker)
# минуты-minutes, часы-hours, дни-days, недели-weeks

# каждую минуту
schedule.every().minute.do(worker)

# каждую минуту на 23 секунде
schedule.every().minute.at(":23").do(worker)
schedule.every().hour.at(":42").do(worker)

# каждый 5ый час в 20 минут 30 секунд
schedule.every(5).hours.at("20:30").do(worker)

# в определенное время
schedule.every().day.at("10:30").do(worker)  # без указания секунд (будет в 00 срабатывать)
schedule.every().day.at("10:30:42").do(worker)  # с указанием секунд
schedule.every().day.at("12:42", "Europe/Amsterdam").do(worker)  # с указанием часового пояса

# по дням недели
schedule.every().monday.do(worker)
schedule.every().wednesday.at("13:15").do(worker)

while True:
    schedule.run_pending()
    time.sleep(1)
