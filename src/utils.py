import json
from class_transation import Transaction
import operator


def open_file():
    with open("operations.json", encoding="utf-8") as file:
        return json.loads(file.read())


def fix_dict():
    a = []
    b = []
    for el in open_file():
        if type(el.get("id")) == int:
            a.append(el)
        else:
            b.append(el)

    return a


def trans_file():
    list_of_transactions = []
    for elem in fix_dict():
        list_of_transactions.append(Transaction(
            elem["id"],
            elem["state"],
            elem["date"],
            elem["operationAmount"]["amount"],
            elem["operationAmount"]["currency"]["name"],
            elem["operationAmount"]["currency"]["code"],
            elem["description"],
            elem["to"],
            elem.get("from")
        )
        )

    return list_of_transactions

def sort_date():
    a = {}
    for el in trans_file():
        if el.state_prof() == True:
            a[el.date] = el.get_descr()
    b = sorted(a.keys(), reverse=True)
    b = b[:5]
    return b

