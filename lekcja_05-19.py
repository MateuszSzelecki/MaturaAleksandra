
# for - pętla - wykonywana wielokrotnie

#for i in range(8):
#    print(i)

#w programowaniu liczymy sobie od 0

#print() - wyswietlanie

# typy danych:
# string - ciąg znaków np.: "Hello world"
# int - liczba
# char - pojedynczy znak np.: 'A'

# biorąc dane z pliku tekstowego wszystko jest w stringach

#imie = "Aleksander"
#print(imie[0]) - wyswietli A
#print(imie[2]) - wyswietli sie e

# == przy porównywaniu
# = przy przypisywaniu wartosci

#rstrip - usuwa spacje, tabulacje itp

result4_1 = 0
result_4_1_2 = ""
with open("liczby.txt", "r") as file:  #odczytywanie pliku tekstowego jako file
    for line in file:  #odczytywanie linijki z file
        line = line.rstrip()  #wyciecie spacji z linijek
        dlugosc = len(line)  #sprawdzenie dlugosci linijki i przypisanie do zmiennej
        pierwsza = line[0]  #zapisanie pierwszej litery do zmiennej
        ostatnia = line[dlugosc-1]  #zapisanie ostatniej litery do zmiennej
        if pierwsza == ostatnia:  #jesli identyczne - porównanie z ==
            if result4_1 == 0:
                result_4_1_2 = line
            result4_1 += 1

print(result4_1)
print(result_4_1_2)
