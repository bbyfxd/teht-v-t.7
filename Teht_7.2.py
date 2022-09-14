nimet = set()
nimi = input("Anna nimi: ")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
        nimi = input("Anna uusi nimi: ")
    else:
        nimet.add(nimi)
        print("Uusi nimi.")
        nimi = input("Anna uusi nimi: ")

for i in nimet:
    print(i)