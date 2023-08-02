'''
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Jan Dolejší
email: j-dolejsi@koito-czech.cz
discord: Jan D#4030
'''

'''
Jak postupovat
1. Na svém počítači si vytvoříte vlastní virtuální prostředí (speciálně pro tento úkol)
2. Do nově vytvořeného prostředí si přes IDE (nebo příkazový řádek) nainstalujete potřebné knihovny třetích stran
3. Vygenerujete soubor requirements.txt, který obsahuje soupis všech knihoven a jejich verzí (nevypisovat ručně!)
4. Výsledný soubor budete spouštět pomocí 2 argumentů (ne pomocí funkce input). První argument obsahuje odkaz, který územní celek chcete scrapovat (př. územní celek Prostějov ), druhý argument obsahuje jméno výstupního souboru (př. vysledky_prostejov.csv)
5. Pokud uživatel nezadá oba argumenty (ať už nesprávné pořadí, nebo argument, který neobsahuje správný odkaz), program jej upozorní a nepokračuje.
6. Následně dopište README.md soubor, který uživatele seznámíte se svým projektem. Jak nainstalovat potřebné knihovny ze souboru requirements.txt, jak spustit váš soubor, příp. doplnit ukázku, kde demonstrujete váš kód na konkrétním odkaze s konkrétním výpisem.
'''

import requests
from bs4 import BeautifulSoup
import os
import csv
import sys

def checkcommand():
    if len(sys.argv) != 3:
        print(f'Je zapotřebí zadat 2 argumenty za názvem python souboru - název, url adresa a název výstupního souboru \n -> například python "projekt3.py" "https://volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4204" "file.csv"')
        quit()

def checkcommandvalues(url,soup):
    os.system('cls')
    print(f'ZPRACOVÁVÁM DATA PRO ADRESU {url}')
    try: 
        country = []
        values = soup.find_all("h3")
        for v in values:
            v = v.text
            country.append(v.replace('\n', ''))
        print(f'Vybrán {country[1]}')
    except IndexError:
        print("Zadána chybná adresa")
        quit()
    except:
        print("Neznámá chyba, zkuste zkontrolovat funkčnost webové adresy")
        quit()
    else:
         print('\n') 

def supporturl() -> list:
    '''
    Vytvoření listu, který obsahuje url cesty pro dané obce
    '''
    print('Zpracovávám pomocné tabulky')    
    url_list = []
    urls = soup.find_all("td", "cislo", "href")
    for u in urls:
        u = u.a["href"]
        url_list.append(f"https://volby.cz/pls/ps2021/{u}")
    print(f'   - hotovo \n')
    return(url_list)

def webadjustment(source):
    path = requests.get(source)
    web = BeautifulSoup(path.text, "html.parser")
    return(web)

def wards(Description, tag, classvalue) -> list:
    '''
    Do funkce budou zadány hodnoty
     - description - pouze pro popis uživateli, jaká hodnota je právě zpracovávána
     - tag - návěští html kódu (v našem případě vždy hodnota td, mohla by být v tomto případě dána i natvrdo)
     - classvalue - hodnota dané třídy
    Pomocí této funkce budou zpracovány listy pro:
     - seznam obvodů v daném okrese
     - kódy měst'
    '''
    print(f'Zpracovávám {Description}')
    list = []
    values = soup.find_all(tag, classvalue)
    for v in values:
        list.append(v.text)
    print(f'   - hotovo \n')
    return(list)

def votersdata(Description, url_list, id) -> list:
    '''
    Do funkce budou zadány hodnoty
     - description - pouze pro popis uživateli, jaká hodnota je právě zpracovávána
     - url_list - list adres, které budou zpracovány v procesu
     - id - vybraná hodnota v seznamu
    Pomocí této funkce budou zpracovány listy pro:
     - počty platných hlasů
     - počty odevzadných obálek
     - počty registrovaných voličů
    '''
    print(f'Zpracovávám {Description}')
    list = []
    for u in url_list:
        web = webadjustment(u)
        lists = web.find_all("td", headers=id)
        for l in lists:
            l = l.text
            list.append(l.replace('\xa0', ' '))
    print(f'   - hotovo \n')
    return(list)

def parties(Description, url_list) -> list:
    '''
    Do funkce budou zadány hodnoty
     - description - pouze pro popis uživateli, jaká hodnota je právě zpracovávána
     - url_list - list adres, které budou zpracovány v procesu
    Pomocí této funkce bude zpracován list jednotlivých stran ze zadaného listu s adresami
    '''
    print(f'Zpracovávám {Description}')    
    list = []
    web = webadjustment(url_list[0])
    parties = web.find_all("td", "overflow_name")
    for p in parties:
        list.append(p.text)
    print(f'   - hotovo \n')
    return(list)

def partiesresults(Description, url_list) -> list:
    '''
    Do funkce budou zadány hodnoty
     - description - pouze pro popis uživateli, jaká hodnota je právě zpracovávána
     - url_list - list adres, které budou zpracovány v procesu
    Pomocí této funkce bude zpracován list podlistů pro vytažení výsledků stran    
    '''
    print(f'Zpracovávám {Description}') 
    list = []
    for u in url_list:
        web = webadjustment(u)
        results = web.find_all("td", "cislo", headers=["t1sb4", "t2sb4"])
        sublist = []
        for r in results:
            sublist.append(r.text + ' %')
        list.append(sublist)
    print(f'   - hotovo \n')
    return(list)

def makefinaltuple() -> tuple:
    '''
    Zpracování všech záznamů (listů) do jednoho tuplu
    '''
    url_list = supporturl()
    result = partiesresults('výsledky stran', url_list)
    final = (result)
    valid = votersdata('počty platných hlasů', url_list, 'sa6')
    for x in range(len(valid)):
        final[x].insert(0,valid[x])
    envelope = votersdata('počty odevzadných obálek', url_list, 'sa3')
    for x in range(len(envelope)):
        final[x].insert(0,envelope[x])
    registered = votersdata('počty registrovaných voličů', url_list, 'sa2')
    for x in range(len(registered)):
        final[x].insert(0,registered[x])
    location = wards('seznam obvodů v daném okrese', 'td', 'overflow_name')
    for x in range(len(location)):
        final[x].insert(0,location[x])
    code = wards('kódy měst', 'td', 'cislo')
    for x in range(len(code)):
        final[x].insert(0,code[x])
    party = parties('seznam stran v daném okrese', url_list)
    header = ['code', 'location', 'registered', 'envelopes', 'valid']
    header.extend(party)
    final.insert(0,header)
    return(tuple(final))

def csvmaker(file) -> None:
    new_csv = open(file, mode="w", newline='')
    writer = csv.writer(new_csv, delimiter=";")
    writer.writerows(makefinaltuple())
    print(f'Výsledný csv soubor {file} byl vytvořen')
    new_csv.close()

if __name__ == '__main__':
    checkcommand()
    url = sys.argv[1]
    file = sys.argv[2]
    odp_serveru = requests.get(url)
    type(odp_serveru.text)
    soup = BeautifulSoup(odp_serveru.text, "html.parser")
    checkcommandvalues(url,soup)
    csvmaker(file)
