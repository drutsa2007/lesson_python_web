from schedule import every, repeat, run_pending
import time


@repeat(every(10).minutes)
def job():
    print("Небольшая программа")


while True:
    run_pending()
    time.sleep(1)
