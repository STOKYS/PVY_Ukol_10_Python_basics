'''
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.
'''

EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu


def fnc_weight(weight):
    """
    Calculates how much would you weight on the moon
    """
    calc = float(weight) / EARTH_GRAVITY * MOON_GRAVITY
    print(f"Your weight on the moon would be: {round(calc, 3)}kg\n")


def fnc_how_far(time):
    """
    Calculates how far away from you is the source of sound,
    can be useful for finding out how far a thunder is from you
    """
    calc = SPEED_OF_SOUND * float(time)
    print(f"The source of the sound is about {round(calc, 3)}m away from you\n")


def fnc_how_long(distance):
    """
    Calculates how long would it take for light to travel there
    """
    calc = (float(distance) / SPEED_OF_LIGHT)
    print(f"It would take {round(calc, 10)} seconds for light to travel there\n")


def main():
    fnc_weight(input("Input your weight (kg):  "))
    fnc_how_far(input("How long did it take for you to hear the sound (s):  "))
    fnc_how_long(input("How far would you like to travel (m):  "))


if __name__ == "__main__":
    main()
