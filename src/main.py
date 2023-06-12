from src.func_prog import *
from src.make_class import trans_file

trans_file().sort(key=lambda x: x.name)


def __main__():
    """
    Основная функция
    Создает нужный словарь потом соритирует потом выводит
    :return:
    """
    finish_dict = {}
    for elem in trans_file():
        if elem.state_prof() == True:
            finish_dict[elem.date] = elem.get_descr()
    final_list = sorted(finish_dict.items(), reverse=True)
    for el in final_list[:5]:
        print(el[1])


if "__name__" == __main__():
    __main__()
