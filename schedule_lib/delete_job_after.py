import schedule
import time


def job_that_executes_once():
    # Что то делаем
    return schedule.CancelJob


schedule.every().seconds.do(job_that_executes_once)

while True:
    schedule.run_pending()
    time.sleep(1)
