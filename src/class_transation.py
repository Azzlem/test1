from func_prog import *


class Transaction_():
    """
    Класс транзакций
    """
    def __init__(self, id_, state, date, amount, name, code, description, to_, from_=""):
        self.id = id_
        self.state = state
        self.date = date
        self.amount = amount
        self.name = name
        self.code = code
        self.description = description
        self.to_ = to_
        self.from_ = from_

    def get_descr(self):
        """
        метод класса формирующий конечный вывод
        :return: Строки текста для пользователя
        """
        date = self.date[8:10] + "." + self.date[5:7] + "." + self.date[:4]
        from_one = change_(self.from_)
        from_two = change_two(self.from_)
        to_to = 2 * "*" + self.to_[-4:]
        return f'{date} {self.description}\n' \
               f'{from_one} {from_two} -> Счет {to_to}\n' \
               f'{self.amount} {self.name}\n'

    def state_prof(self):
        """
        Проверка на успешность операции
        :return: верность сравнения
        """

        return True if self.state == "EXECUTED" else False

    def date_up(self):
        """
        Функция формирования даты в формате хх.хх.хххх
        :return: Дата в нужном нам формате
        """

        return self.date[8:10] + "." + self.date[5:7] + "." + self.date[:4]
