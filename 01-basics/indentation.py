"""
Cvičení 2:

Vytvořte libovolně pojmenovanou vlastní funkci s minimálně jedním parametrem, v níž využijete cyklus for, Da
aspoň jednu podmínku if a funkci print(). Dodržte správné odsazování kódu a opatřete funkci stručnou dokumentací.
Do konzole vypište nejprve docstring vaší funkce a potom zavolejte funkci samotnou.   
"""

def function(base, exponent):
    """
    This function will do magic stuff and calculate the result
    """
    res = base
    for i in range(1, exponent):
        res *= base
    print(f"{base} to the power of {exponent} is equal to {res}")

def main():
    print("I will calculate exponent of x")
    base = float(input("Please set your base number:  "))
    exponent = int(input("Please set your exponent:  "))
    print(f"\n{function.__doc__}\n")
    function(base, exponent)

main()