def masodik():
#2.feladat:	Egy pizzázó téged kért fel belső rendszerének modernizálására. Vendégcsábító akciókba kezdtek. A te dolgod az akciók kezelésének kidolgozása. A felhasználó vásárol a felületen ezt egy vegOsszeg változóban tárolják, a felhasználó kedvezmény kategóriáját pedig egy kategoria nevű változóba

    vegOsszeg=int(input("Mekkora összegért vásárolt?"))
    kategoria=input("Milyen kedvezményre jogosult?")
    return(vegOsszeg)

    if kategoria=="arany":
        print(vegOsszeg*0.9)
        print("10% kedvezményt kap!")
    if kategoria=="ezüst":
        print(vegOsszeg*0.95)
        print("5% kedvezményt kap!")
    if kategoria=="bronz":
        print(vegOsszeg*0.98)
        print("2% kedvezményt kap!")
    if kategoria=="vip":
        print(vegOsszeg*0.8)
        print("20% kedvezményt kap")

    elif kategoria=="":
        print(vegOsszeg*0.99)
        print("Haloween akció 1% kedvezményt kap")

    if vegOsszeg>=10000:
        print("Nagy összegű vásárlás!")
