import schedule


def ring(music):
    # такого варианта нет, это только для понимания
    play(music)


schedule.every().day.at("08:00").do(ring, music='start_lesson.mp3')
schedule.every().day.at("08:40").do(ring, music='end_lesson.mp3')

schedule.every().day.at("08:50").do(ring, music='start_lesson.mp3')
schedule.every().day.at("09:30").do(ring, music='end_lesson.mp3')

schedule.every().day.at("09:40").do(ring, music='start_lesson.mp3')
schedule.every().day.at("10:20").do(ring, music='end_lesson.mp3')

while True:
    schedule.run_pending()
