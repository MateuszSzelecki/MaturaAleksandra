maksymalna = -1
result = []

with open("identyfikator.txt", "r") as file:
    for line in file:
        line = line.rstrip()
        suma_cyfr = 0
        for i in range(3, len(line)):
            suma_cyfr += int(line[i])  #zamiana znaku na liczbe (int)
        if suma_cyfr > maksymalna:
            maksymalna = suma_cyfr
            result.clear()
            result.append(line)
        elif suma_cyfr == maksymalna:  #elif wykonuje się tylko wtedy gdy if nieprawdziwy
            result.append(line)

print(result)

#*** PALINDROMY ***
# KAJAK - palindrom, dlaczego?
# czytasz od lewej: KAJAK
# czytasz od prawej: KAJAK
# 12121 - dodatkowy przykład

slowo = "KAJAKI"
polowa_dlugosci = int(len(slowo)/2)
czy_palindrom = True
for i in range(polowa_dlugosci):
    if slowo[i] != slowo[len(slowo)-1-i]:  #ponieważ ostatni indeks stringa to dlugosc tego stringa - 1
        czy_palindrom = False


#DZIELENIE STRINGA na kilka mniejszych
imie = "Mateusz"

czesc1 = imie[0:3] #od indeksu 0 do indeksu 3 (bez 3)
czesc2 = imie[3:] #od indeksu 3 do konca stringa


with open("identyfikator.txt", "r") as file:
    for line in file:
        line = line.rstrip()
        seria = line[0:3]
        numer = line[3:]
