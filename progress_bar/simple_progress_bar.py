import time
from progress.bar import Bar

mylist = [1, 2, 3, 4, 5, 6, 7, 8]

bar = Bar('Countdown', max=len(mylist), color="red")

for item in mylist:
    bar.next()
    time.sleep(1)

bar.finish()


# ВНИМАНИЕ!!! Не отображается (или только у меня) в терминале программы Pycharm.
# Работает через командную строку.
