# from enum import Enum
# from typing import List
from typing import Dict, Literal, Any, Optional

SEX = Literal['муж', 'жен']


def my_function(
        param1: int = 23,
        param2: float = 4.4,
        param3: str = '',
        param4: bool = True,
        param5: SEX = 'Муж',
        param6: Optional[Dict] = None,
        param7: Optional[Any] = None

) -> dict[str, str, SEX]:
    """Эта простая функция которая возвращает словарь\n
        Стиль написания Docstrings - reStructuredText

        Keyword arguments:\n
        -ывавыа\n
        -sdwerq\n


        :param param1: Первый параметр - какое-то описание
        :type param1: int

        :param param2: Второй параметр
        :type param2: bool

        :param param3: Третий параметр
        :type param3: bool

        :param param4: Четвертый параметр
        :type param4: bool

        :param param5: Пятый параметр
        :type param5: bool

        :param param6: Шестой параметр
        :type param6: bool

        :param param7: Последний параметр
        :type param7: bool

        :return: что возвращается
        :rtype: какой тип возращается

        :raises ValueError: If `param2` is equal to `param1`.

        https://alex.ivanov.ru/

        .. Note::
            Небольшая текстовая информация, типа че делает функция

        """