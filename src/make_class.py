from src.class_transation import Transaction_
from src.func_prog import fix_dict


def trans_file():
    """
    Функция создания списков объектов класса
    :return: список экземпляров класса
    """
    list_of_transactions = []
    for elem in fix_dict():
        list_of_transactions.append(Transaction_(
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
