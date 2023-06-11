import json
from class_transation import *


def open_file():
    """
    Функция открытия файла
    :return: json
    """
    with open("operations.json", encoding="utf-8") as file:
        return json.loads(file.read())


def fix_dict():
    """
    Функция исправления словаря
    :return: dict
    """
    true_list = [el for el in open_file() if type(el.get("id")) == int]

    return true_list


def trans_file():
    """
    Функция создания списков объектов класса
    :return: list
    """
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


def change_(account_details: str):
    """
    Функция преобразования реквизитов карты или счёте
    :param name: str
    :return:
    """
    if account_details is None:
        return ""
    if len(account_details.split()) == 2:
        return account_details.split()[0]
    if len(account_details.split()) == 3:
        return account_details.split()[0] + " " + account_details.split()[1]


def change_two(account_details: str):
    """
    Функция преобразования реквизитов карты или счёте
    :param name:str
    :return:
    """
    if account_details == None:
        return ""
    if len(account_details.split()) == 2:
        acc_num = account_details.split()[1]
        return acc_num[:4] + " " + acc_num[4:6] + "** **** " + acc_num[12:]
    if len(account_details.split()) == 3:
        acc_num_2 = account_details.split()[2]
        return acc_num_2[:4] + " " + acc_num_2[4:6] + "** **** " + acc_num_2[12:]
