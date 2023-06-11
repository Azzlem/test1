import json
from class_transation import *



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


def change_(name: str):
    if name == None:
        return ""
    if len(name.split()) == 2:
        return name.split()[0]
    if len(name.split()) == 3:
        return name.split()[0] + " " + name.split()[1]

def change_two(name: str):
    if name == None:
        return ""
    if len(name.split()) == 2:
        acc_num = name.split()[1]
        return acc_num[:4] + " " + acc_num[4:6] + "** **** " + acc_num[12:]
    if len(name.split()) == 3:
        acc_num_2 = name.split()[2]
        return acc_num_2[:4] + " " + acc_num_2[4:6] + "** **** " + acc_num_2[12:]

