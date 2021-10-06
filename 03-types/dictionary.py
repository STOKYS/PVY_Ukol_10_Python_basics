# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''

skolni_zaznam = {
  "Pondeli": {
    "hodiny": [
      "MAT",
      "CJ",
      "ANJ"
    ],
    "zaku_pritomno": 15,
    "sluzba": "Marcel Novak",
    "sluzba_pritomna": True,
    "zaci_nepritomni": {"Filip Novak", "Tomas Tonemas"},
    "trida": ("IT0",)
  },
  "Streda": {
  "hodiny": [
      "CJ",
      "DEL",
      "PVY",
      "PVY"
    ],
    "zaku_pritomno": 16,
    "sluzba": "Tomas Tonemas",
    "sluzba_pritomna": False,
    "zaci_nepritomni": {"Tomas Tonemas"},
    "trida": ("IT0p1", "IT0p2")
  },
  "Ctvrtek": {
    "hodiny": [
      "ANJ",
      "ANJ",
      "FYZ"
    ],
    "zaku_pritomno": 16,
    "sluzba": "Honza Pritomen",
    "sluzba_pritomna": True,
    "zaci_nepritomni": {"Tomas Tonemas"},
    "trida": ("IT0",)
  }
}

def fnc_removeadd():
    skolni_zaznam.pop('Ctvrtek')
    skolni_zaznam['Patek'] = {
      "hodiny": [
        "PCS",
        "FYZ",
        "MAT"
      ],
      "zaku_pritomno": 16,
      "sluzba": "Honza Pritomen",
      "sluzba_pritomna": True,
      "zaci_nepritomni": {"Martin Vysoky"},
      "trida": ("IT0",)
    }


def fnc_write():
  print("Slovnik skolni_zaznam\n"
        "------------------------------------------------------------------------------------------------\n"
        "Den       Trida         Hodiny               Zaku Pritomno    Sluzba             Zaci Nepritomni\n"
        "------------------------------------------------------------------------------------------------")
  for key, value in skolni_zaznam.items():
    print(f"{key:<8}  {(len(value.get('trida'))*'%-6s') % value.get('trida'):<13} {', '.join(value.get('hodiny')):<20} {value.get('zaku_pritomno'):<17}"
          f"{value.get('sluzba'):<19}"
          f"{', '.join(value.get('zaci_nepritomni'))}")
  print("------------------------------------------------------------------------------------------------\n"
        f"Pocet zaznamu: {len(skolni_zaznam)}")


def main():
    fnc_removeadd()
    fnc_write()


if __name__ == "__main__":
    main()