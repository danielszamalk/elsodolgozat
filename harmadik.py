def harmadik():
#3.feladat:	Írd ki a -200 és 150 közötti minden ötödik számot egy sorba kukac jelel elválasztva. (ne egyesével gépeld be őket, az nem jó megoldás!) A megoldásodat for-al és while-al is valósítsad meg!

    for szam in range(-201,151,5):
        print(str(szam)+" @ ", end="")
             if szam == 150:
                 print(str(szam), end="")


def harmadikWhile():

    szam=-200
    while (szam <= 150) and (szam/5==0):
        print(szam)