tab = [1, 2, 3]
imie = "Aleskander"
imiona = ["Aleksander", "Mateusz"]

tablica = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

#print(tablica[1][0])
#print(tablica[2][2])
#print(tablica[2][1])

matryca = []  #deklarowanie tablicy
wiersz = 0
with open("zplik1.txt", "r") as file:
    for line in file:
        line = line.strip()
        matryca.append([])  #dodawanie pustej tablicy do tablicy 3D
        matryca[wiersz] = line.split(' ')  #dzielimy naszą linijke w odniesieniu do spacji
        wiersz += 1

najwieksza = 0
najmniejsza = 255

print(matryca[0])

for wiersz in matryca:  #rozpatrywanie wszystkich wierszy w matrycy
    for wartosc in wiersz:  #rozpatrywanie wszystkich wartosci w wierszu
        wartosc = int(wartosc)  #zamiana wartosci ze stringa na int
        if wartosc > najwieksza:  #szukanie wartosci najwiekszej
            najwieksza = wartosc
        elif wartosc < najmniejsza:
            najmniejsza = wartosc

print(najmniejsza)
print(najwieksza)
