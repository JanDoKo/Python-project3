#Pro instalalaci balíčků potřebných pro spuštění pythonu je zapotřebí spustit příkaz
pip install -r requirements.txt

--------------------------------------------------

#Spuštění souboru probíhá pomocí příkazu se zadáním dvou argumentů, například:
python projekt3.py "https://volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4204" "file.csv"

--------------------------------------------------

#Při správném zadání všech argumentů se postupně uživateli vypíše, adresu, jakou uživatel zadal, informaci jakého okresu se týká a poté bude uživatel informován jaká data právě program zpracovává a nakonec jaký soubor byl vytvořen

ZPRACOVÁVÁM DATA PRO ADRESU https://volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4204
Vybrán Okres: Louny


Zpracovávám pomocné tabulky
   - hotovo

Zpracovávám výsledky stran
   - hotovo 

Zpracovávám počty platných hlasů
   - hotovo 

Zpracovávám počty odevzadných obálek
   - hotovo 

Zpracovávám počty registrovaných voličů
   - hotovo 

Zpracovávám seznam obvodů v daném okrese
   - hotovo

Zpracovávám kódy měst
   - hotovo 

Zpracovávám seznam stran v daném okrese
   - hotovo 

Výsledný csv soubor file.csv byl vytvořen

--------------------------------------------------

#Při zadání nesprávného počtu argumentů vypíše program chybové hlášení:
Je zapotřebí zadat 2 argumenty za názvem python souboru - název, url adresa a název výstupního souboru 
 -> například python "projekt3.py" "https://volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4204" "file.csv"

--------------------------------------------------

#Při zadání chybné adresy program vypíše chybové hlášení:
ZPRACOVÁVÁM DATA PRO ADRESU https://volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4211
Zadána chybná adresa

--------------------------------------------------

#NEDOSTATKY K DALŠÍMU MOŽNÉMU ZPRACOVÁNÍ
data je možné stahovat pouze pro rok 2021, pro jiná léta není příkaz ošetřen
u zadané adresy je zkontrolován pouze správný stav (zda existuje), může být zadána adresa, která kontrolou projde, ale bude chybně zpracována


