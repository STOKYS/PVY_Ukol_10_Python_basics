'''
Programátorská výzva:
Použijte kombinaci různý možností pro práci s řetězci (včetně různých funkcí) i jiných prvků jazyka Python 
(ternární operátor, matematické funkce atd.) k co nejefektivnějšímu řešení následujících cvičení (čím kratší
funkční kód, tím lepší).

1. Převeďte "česky" zadané datum - např. 12. 10. 2020 - do podoby "databázové" podoby - např. 2020-10-12
2. Vytvořte funkci, která vyrobí ze zadaného sousloví:
   a) identifikátor pro proměnné používané v Pythonu - např. To je proměnná v Pythonu = to_je_promenna_v_pythonu
   b) identifikátor pro camel syntax v JS - např. To je proměnná v Pythonu = toJePromennaVPythonu 
   Obě možnosti by měly být vyřešeny v jedné funkci s využitím parametrů.
   Kdo si chce úkol trochu zjednodušit, nemusí řešit znaky s českou diakritikou. 
3. Vytvořte funkci, která vygeneruje náhodná hesla pro počet osob zadaný v parametru tak, aby heslo začínalo
   3 velkými písmeny, pokračovalo 3 malými písmeny, jedním speciálním znakem (-/+*) a končilo 3 náhodnými číslicemi.
'''


def fnc_date_converter():
    date = (input("Type in a valid date(dd.mm.yyyy):  ")).split(".")
    print(f"{date[2]}-{date[1]}-{date[0]}")


def fnc_snake_case():
    vstup = (input("Type in a short sentence:  ")).split(" ")
    fin = ''
    for i in range(0, len(vstup)):
        fin += (f"{vstup[i].lower()}")
        if (i + 1) != len(vstup):
            fin += ("_")
    print(fin)


def fnc_camel_case():
    vstup = (input("Type in a short sentence:  ")).split(" ")
    fin = ''
    for i in range(0, len(vstup)):
        if not i:
            fin += ((f"{vstup[i].lower()}"))
        else:
            fin += (f"{vstup[i][0].upper()}{vstup[i][1:].lower()}")
    print(fin)


def main():
    fnc_date_converter()
    fnc_snake_case()
    fnc_camel_case()


if __name__ == "__main__":
    main()


