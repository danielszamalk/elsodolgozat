import math


def negyedik():
#4.feladat:	Kérj be a felhasználótól egy valósszámot. A programod számítsa ki a bekért érték alsó egész részét(kerekítse lefele), ehhez a math csomag floor() eljárásátt használd.
    print("Kérem adjon meg egy valós számot!")
    a = float(input())
    b = math.floor(a)
    print(b)