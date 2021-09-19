"""
Cvičení 4:

Použijte vhodné moduly v Pythonu (včetně jejich případné instalace) k tomu, abyste: 
1) vypsali aktuální datum a čas
2) vypsali datum velikonoční neděle (easter) v následujících 5 letech
3) vypsali nejbližší rok, v němž bude Štědrý den v neděli

K řešení prvního úkolu je možné doporučit importovat interní modul datetime
Řešení dalších dvou úkolů můžete odvodit z příkladů v dokumentaci k externímu modulu dateutil - viz https://pypi.org/project/python-dateutil/
"""

import datetime
import dateutil

print(f"{datetime.now()}\n")

year = datetime.now().year
for i in range(1,6):
    print(f"{dateutil.easter.easter(year + i,1)}")

sunday = False
i = 0
while not sunday:
    if (datetime(int(year) + int(i), 12, 24).weekday() == 6):
        print(f"\nChristmas is on sunday in the year {year + i}")
        sunday = True
    else:
        i += 1