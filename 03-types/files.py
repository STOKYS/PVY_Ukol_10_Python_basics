import csv
import json


'''
Editing .txt
'''


def textfile_read(path, encoding='utf-8'):
    try:
        with open(path, mode='r', encoding=encoding) as file:
            return file.read()
    except FileNotFoundError as error:
        return f"Soubor nebyl nalezen: {error}"
    except Exception as error:
        return f"Doslo k nejakemu problemu pri nacitani souboru: {error}"
    finally:
        file.close()
    return data


def textfile_write(path, data='', encoding='utf-8'):
    try:
        with open(path, mode='w', encoding=encoding) as file:
            file.write(data)
    except FileNotFoundError as error:
        return f"Soubor nebyl nalezen: {error}"
    except Exception as error:
        return f"Doslo k nejakemu problemu pri nacitani souboru: {error}"
    finally:
        file.close()
    return data


'''
Editing .json
'''


def jsonfile_read(path, encoding='utf-8'):
    try:
        with open(path, mode='r', encoding=encoding) as file:
            data = json.load(file)
    except FileNotFoundError as error:
        return f"Soubor nebyl nalezen: {error}"
    except Exception as error:
        return f"Doslo k nejakemu problemu pri nacitani souboru: {error}"
    finally:
        file.close()
    return data


def jsonfile_write(path, data={}, encoding='utf-8'):
    try:
        with open(path, mode='w', encoding=encoding) as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError as error:
        return f"Soubor nebyl nalezen: {error}"
    except Exception as error:
        return f"Doslo k nejakemu problemu pri nacitani souboru: {error}"
    finally:
        file.close()
    return data


'''
Editing .csv
'''


def csvfile_read(path, encoding='utf-8'):
    try:
        with open(path, mode='r', encoding=encoding) as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            dict_list = []
            for row in data:
                dict_list.append(row)
    except FileNotFoundError as error:
        return f"Soubor nebyl nalezen: {error}"
    except Exception as error:
        return f"Doslo k nejakemu problemu pri nacitani souboru: {error}"
    finally:
        file.close()
    return dict_list


def csvfile_write(path, data={}, encoding='utf-8'):
    try:
        with open(path, mode='w', encoding=encoding) as file:
            writer = csv.DictWriter(file, fieldnames=list(data[0].keys()))
            writer.writeheader()
            for x in data:
                writer.writerow(x)
    except FileNotFoundError as error:
        return f"Soubor nebyl nalezen: {error}"
    except Exception as error:
        return f"Doslo k nejakemu problemu pri nacitani souboru: {error}"
    finally:
        file.close()
    return data


'''
Printing data
'''

print(f".txt soubor obsahuje: {textfile_read('python_read.txt')}")
print(f"Do .txt souboru jsme napsali: {textfile_write('python_write.txt', 'world')}\n")
print(f".json soubor obsahuje: {jsonfile_read('python_read.json')}")
skolni_zaznam = {
    "hodiny": [
      "MAT",
      "CJ",
      "ANJ"
    ],
    "zaku_pritomno": 15,
    "sluzba": "Marcel Novak",
    "sluzba_pritomna": True
}
print(f"Do .json souboru jsme napsali: {jsonfile_write('python_write.json', skolni_zaznam)}\n")
print(f".csv soubor obsahuje: {csvfile_read('python_read.csv', encoding='windows-1250')}")
csvdata = [{'id': '0', 'firstname': 'Teriann', 'lastname': 'Velick', 'email': 'Teriann.Velick@yopmail.com', 'email2': 'Teriann.Velick@gmail.com', 'profession': 'police officer'}, {'id': '1', 'firstname': 'Lorne', 'lastname': 'Henebry', 'email': 'Lorne.Henebry@yopmail.com', 'email2': 'Lorne.Henebry@gmail.com', 'profession': 'developer'}, {'id': '2', 'firstname': 'Jackie', 'lastname': 'Bord', 'email': 'Jackie.Bord@yopmail.com', 'email2': 'Jackie.Bord@gmail.com', 'profession': 'developer'}, {'id': '3', 'firstname': 'Gavrielle', 'lastname': 'Stuart', 'email': 'Gavrielle.Stuart@yopmail.com', 'email2': 'Gavrielle.Stuart@gmail.com', 'profession': 'firefighter'}, {'id': '4', 'firstname': 'Rhoda', 'lastname': 'Denis', 'email': 'Rhoda.Denis@yopmail.com', 'email2': 'Rhoda.Denis@gmail.com', 'profession': 'firefighter'}, {'id': '5', 'firstname': 'Lory', 'lastname': 'Gillan', 'email': 'Lory.Gillan@yopmail.com', 'email2': 'Lory.Gillan@gmail.com', 'profession': 'worker'}, {'id': '6', 'firstname': 'Roslyn', 'lastname': 'Tamar', 'email': 'Roslyn.Tamar@yopmail.com', 'email2': 'Roslyn.Tamar@gmail.com', 'profession': 'doctor'}, {'id': '7', 'firstname': 'Juliane', 'lastname': 'Myrilla', 'email': 'Juliane.Myrilla@yopmail.com', 'email2': 'Juliane.Myrilla@gmail.com', 'profession': 'police officer'}, {'id': '8', 'firstname': 'Zia', 'lastname': 'Elvyn', 'email': 'Zia.Elvyn@yopmail.com', 'email2': 'Zia.Elvyn@gmail.com', 'profession': 'firefighter'}, {'id': '9', 'firstname': 'Clary', 'lastname': 'Bonilla', 'email': 'Clary.Bonilla@yopmail.com', 'email2': 'Clary.Bonilla@gmail.com', 'profession': 'developer'}]
print(f"Do .csv souboru jsme napsali: {csvfile_write('python_write.csv', csvdata)}")