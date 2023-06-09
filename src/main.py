import json
from class_transation import Transaction


def open_file():
    with open("operations.json") as file:
        file_json = json.loads(file.read())
        return file_json


def trans_file():
    list_of_transactions = []
    for elem in open_file():
        list_of_transactions.append(Transaction(
            elem.get("id"),
            elem.get("state"),
            elem.get("date"),
            elem.get("operationAmount"),
            elem.get("operationAmount"),
            elem.get("operationAmount"),
            elem.get("description"),
            elem.get("to"),
            elem.get("from")
        ))
    return list_of_transactions


list_of_transactions_ = trans_file()


print(list_of_transactions_[0].amount)
