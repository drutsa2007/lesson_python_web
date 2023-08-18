import jmespath


# Получаем определенный элемент
d = {"foo": {"bar": "baz"}}
print(jmespath.search('foo.bar', d))
# baz

# С помощью подстановочного знака получаем все названия
d = {"foo": {"bar": [{"name": "one"}, {"name": "two"}]}}
print(jmespath.search('foo.bar[*].name', d))
# [“one”, “two”]

