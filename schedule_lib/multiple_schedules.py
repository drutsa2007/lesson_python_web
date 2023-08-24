import time
import schedule


def work1():
    print("start work1")


def work2():
    print("start work2")


# Create a new scheduler
scheduler1 = schedule.Scheduler()
# Add jobs to the created scheduler
scheduler1.every().hour.do(work1)
scheduler1.every().hour.do(work2)

# Create as many schedulers as you need
scheduler2 = schedule.Scheduler()
scheduler2.every().second.do(work1)
scheduler2.every().second.do(work2)

while True:
    # run_pending needs to be called on every scheduler
    scheduler1.run_pending()
    scheduler2.run_pending()
    time.sleep(1)
