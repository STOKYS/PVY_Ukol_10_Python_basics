'''
 Set je množina jedinečných hodnot
 Set je kolekce ktera je neserazena and neindexovana
 V Pythonu sety jsou psany do kulatych zavorek
'''
my_set = {2, 3, 9, 7}
print('Množina my_set: ', my_set)
print('Typ my_set: ', type(my_set))

# Vytvoření množiny ze seznamu hodnot (list)
numbers = [1, 4, 1, 5, 3, 3, 1, 2, 8, 2]
print(f'Proměnná numbers - seznam (list): {numbers}')
set_numbers = set(numbers)
print(f'Proměnná set_numbers - množina (set): {set_numbers}')

# Vytvoření množiny jedinečných znaků z řetězce
chars = sorted(list('Hello world'))
set_chars = set(chars)
print(f'Uspořádaná množina (set) jedinečných hodnot: {set_chars}')

# Jakmile je set vytvoren, nemuzete zmenit jeho polozky, ale muzete pridavat nove.
# Pro pridani jedne polozky pouzijeme metodu add()
set_chars.add('V')

# Pro pridani vice nez jedne polozky, pouzijeme metodu update()
set_chars.update('X', 'Y', 'Z')

# Pro odstraneni polozky ze setu, pouzijeme metodu remove() nebo discard()
set_chars.remove('H')
print(f'Proměnná set_chars: {set_chars}')

# Metoda clear() set vycisti
set_chars.clear()

# klicove slovo del uplne smaze set
del set_chars

# Přístup k hodnotám množiny
# Nemuzete vybat polozku v setu pomoci indexu, protoze sety jsou neindexovane
# my_set[1]

# Ale muzeme prochazet set pomoci for loopu, nebo se zaptat zda specificka hodnota existuje uvnitr setu.
for x in my_set:
  print(x)

'''
Množinové operace
'''
# Sjednocení množin
print(f'set_numbers | my_set: {set_numbers | my_set}')
print(f'set_numbers.union(my_set): {set_numbers.union(my_set)}')
# Průnik množin
print(f'set_numbers & my_set: {set_numbers & my_set}')
print(f'set_numbers.intersection(my_set): {set_numbers.intersection(my_set)}')
# Rozdíl množin
print(f'set_numbers - my_set: {set_numbers - my_set}')
print(f'set_numbers.difference(my_set): {set_numbers.difference(my_set)}')
# Doplněk množin
print(f'set_numbers ^ my_set: {set_numbers ^ my_set}')
print(f'set_numbers.symmetric_difference(my_set): {set_numbers.symmetric_difference(my_set)}')
# Zjištění zda množina obsahuje hodnotu
print(f'1 in set_numbers: {1 in set_numbers}')
