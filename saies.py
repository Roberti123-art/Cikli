SpeletajaVards=input("Ievadi savu vārdu: ")

print(SpeletajaVards)

SpeletajaVards=SpeletajaVards.lower()
# "mainīgais.lower()" - konvertē visu burtu simbolus par mazajiem burtiem.

SpeletajaVards=SpeletajaVards.capitalize
# "mainīgais.capitalize()" - Simbolu virkē pirmo burtu konvertē par lielo burtu.
print(SpeletajaVards)

vards1="čība"

burtuSK=len(vards1)
# len - saskaita virknē simbolu skaitu.
minejums=input(f"Uzraksti vārdu pareizi- {vards1[3]}{vards1[0]}{vards1[2]}{vards1[1]}: ")
# mainīgais[burtu pozīcija]- simbolu virkne sākās ar indeksu -0.

minejums=minejums.lower()

if minejums==vards1:
    print("Uzminēji vārdu!")
else:
    print("Neuzminēji vārdu. ")    
