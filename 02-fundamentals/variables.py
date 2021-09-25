students_count = 1000
rating = 4.99
is_published = False

'''Úkol A'''
# ? Najděte na Internetu, jakými funkcemi lze v Pythonu zjistit
# ? a) typ objektu
# ? b) identitu objektu (jeho adresu v paměti)
# ? Ukažte to na příkladech proměnných students_count, rating, is_published a vypište výstupy do konzole


def fnc_type_id():
    print(f"Variable 'stundents_count' is a/an {type(students_count)} in memory at address {hex(id(students_count))}")
    print(f"Variable 'rating' is a/an {type(rating)} in memory at address {hex(id(rating))}")
    print(f"Variable 'is_published' is a/an {type(is_published)} in memory at address {hex(id(is_published))}\n")


'''Úkol B'''
# ? Vypište do poznámky všechny bitové operátory, které nabízí Python
# & | ~ ^ >> <<
# ? Do proměnné myself_binary uložte binární číslo vytvořené na základě osmi prvních znaků z vašeho jména a příjmení (souhláska = 1, samohláska 0)
# ? Příklad - HildaDok: 10110101
# ? Vypište toto binární číslo v desítkové soustavě
# ? Pro toto binární číslo proveďte nejprve bitový posun o 2 bity vpravo, poté vypište výsledek v desítkové soustavě
# ? Proveďte bitový součin hexadecimálního čísla "1A" a vašeho binárního čísla a opět vypište v desítkové soustavě
# ? Výsledek zobrazte jako formátovaný řetězec - např. "Binární součin čísla 0b11010 a 0b10110101 je 0b10000"


def fnc_name_to_binary(name):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    name = name.replace(" ", "")
    myself_binary = ""
    for i in range (0, 8):
        if name[i].lower() in vowels:
            myself_binary += "0"
        else:
            myself_binary += "1"
    print(f"{name[:8]}: {myself_binary}")
    decimal = int(myself_binary, 2)
    print(f"{myself_binary} in decimal: {decimal}")
    print(f"{int(myself_binary, 2)} right shifted by 2 places is {decimal >> 2}")
    # Nebyl jsem si jisty zda jsem mel pouzit to puvodni binarni cislo, nebo to binarni cislo posunute (jinak by stacilo vymenit "decimal" za "decimal >> 2)
    print(f"Binary addition of {bin(int('1A', 16))} and {bin(decimal)} is {bin(decimal + int('1A', 16))}")


def main():
    fnc_type_id()
    fnc_name_to_binary(input("Your full name: "))


if __name__ == "__main__":
    main()
