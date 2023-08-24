import schedule
import time
from schedule import every, repeat

#
# # здесь есть аргумент функции
# def greet(name):
#     print('Привет', name)
#
#
# # передаем параметр в виде именованного параметра **kwargs
# schedule.every(2).seconds.do(greet, name='Alice')


# передача через декоратор
@repeat(every().second, "World", 5)
@repeat(every(2).seconds, "Mars", 88)
def hello(planet, number):
    print("Hello", planet, number)


while True:
    schedule.run_pending()
    # time.sleep(1)
