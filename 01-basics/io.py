"""
Cvičení 3:

Vytvořte originální aplikaci v Pythonu, v níž požádáte uživatele o různé vstupní údaje a
využijete na maximum možností výstupů do konzole. Může to být vtipný dotazník, jednoduchý znalostní test (např. 
z matematiky...), průvodce fiktivní instalací atd. Fantazii se meze nekladou a vtipnější vyhrává :-)
Aplikaci uložte do samostatného souboru myapp.py.     
"""

def calculate (grades):
    sum = 0
    for i in range (0, len(grades)):
        sum += int(grades[i])
    avg = sum / len(grades)
    print(f"Your average grade is {avg}")
    if avg < 1 or avg > 5:
        print("What? That's impossible, you must have typed something wrong")
    elif 1 <= avg < 2:
        print("I can see you're pretty good, keep it up!")
    elif 2 <= avg < 3.5:
        print("Meh, you should try harder")
    else:
        print("You're pretty dumb, consider changing schools")


def main ():
    grades = []
    print("Calculate average grade")
    grades.append(int(input("Add your grade:  ")))
    another = True
    while another:
        temp = input("Do you want to add another? (Write number or 'no'):  ")
        if temp == 'no':
            another = False
        else:
            grades.append(temp)
    calculate(grades)

main()