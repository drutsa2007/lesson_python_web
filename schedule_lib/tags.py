import schedule


def greet():
    print('working')


sh = schedule.Scheduler()
sh.every(5).seconds.do(greet).tag('daily-tasks', 'friend')
sh.every(10).seconds.do(greet).tag('hourly-tasks', 'friend')
sh.every(15).seconds.do(greet).tag('hourly-tasks', 'customer')
sh.every(20).seconds.do(greet).tag('daily-tasks', 'guest')

friends = sh.get_jobs('friend')
for job in friends:
    # остановить задачу
    schedule.cancel_job(job)

# остановить все задачи по тегу
sh.clear('daily-tasks')

while 1:
    sh.run_pending()



