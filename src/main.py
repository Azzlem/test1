from src.utils import trans_file
trans_file().sort(key=lambda x: x.name)

for el in trans_file():
    if el.state_prof() == True:
        print(el.get_descr())

# el.state() == True: