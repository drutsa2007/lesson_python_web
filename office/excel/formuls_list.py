from openpyxl.utils import FORMULAE

list_formuls = list(FORMULAE)
list_formuls.sort()
for f in list_formuls:
    print(f)
