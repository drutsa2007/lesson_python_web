print("number %.4f" % 1.34444444)
print("number %c" % 121)
print("number %5d%7d" % (121, 12))

print("%(1)s, %(2).3f" % {'1': 'AB', '2': 1.34444444})

print('{}, {} and {}'.format('one', 1, 4 + 6))
print('{1}, {2} and {0}'.format('one', 1, 4 + 6))

d = {'name': 'Alex', 'age': 56}
print('{name}, {age}'.format(**d))

print('{0}'.format(4 / 3))
print('{0:f}'.format(4 / 3))
print('{0:.2f}'.format(4 / 3))
print('{0:10.2f}'.format(4 / 3))

print("Меня зовут {name}. Мне {age} лет".format(name="Alex", age=34))

name = "Alex"
age = 34
print(f"Меня зовут {name}. Мне {age} лет")
