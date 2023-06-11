from src.utils import trans_file
trans_file().sort(key=lambda x: x.name)

a = {}
for el in trans_file():
    if el.state_prof() == True:
        a[el.date] = el.get_descr()
d = sorted(a.items(), reverse=True)
for i in d[:5]:
    print(i[1])

