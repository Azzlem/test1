from utils import *


class Transaction():
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
        date = self.date[8:10] + "." + self.date[5:7] + "." + self.date[:4]
        from_one = change_(self.from_)
        # from_one = "" if self.from_ == None else self.from_.split()[0]
        # from_two = "" if self.from_ == None else self.from_.split()[1][:6] + 6 * "*" + self.from_.split()[1][-4:]
        from_two = change_two(self.from_)
        to_to = 2 * "*" + self.to_[-4:]
        return f'{date} {self.description}\n' \
               f'{from_one} {from_two} -> {to_to}\n' \
               f'{self.amount} {self.name}\n'

    def state_prof(self):
        return True if self.state == "EXECUTED" else False

    def date_up(self):
        return self.date[8:10] + "." + self.date[5:7] + "." + self.date[:4]
