import schedule


def some_task():
    print('Hello world')


job = schedule.every().second.do(some_task)
# отменяем задание
schedule.cancel_job(job)
