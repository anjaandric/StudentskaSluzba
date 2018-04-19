import datetime

from tabulate import tabulate


def stampaj_tabelu(podaci, zaglavlje):
    print(tabulate(podaci, headers=zaglavlje, tablefmt='orgtbl'))


def stamapaj_spisak():
    fakultet = str(input("Za koji fakultet zelite da dobijete spisak: "))

    # Otvaramo bazu podataka
    baza_fajl = open("baza.db", "r")
    svi_studenti = baza_fajl.readlines()
    baza_fajl.close()

    lista_lista_svih_studenata = []

    for line in svi_studenti:
        linije_bez_praznina = line.strip()
        student_lista=linije_bez_praznina.split(",")
        student_lista_stampa = [student_lista[0] + '/' + student_lista[1],
                                student_lista[2],
                                student_lista[3],
                                student_lista[4]]

        # FIX THIS!
        if fakultet:
            if student_lista[4].lower() == fakultet.lower():
                lista_lista_svih_studenata.append(student_lista_stampa)
        else:
            lista_lista_svih_studenata.append(student_lista_stampa)

    stampaj_tabelu(lista_lista_svih_studenata, ["Br. Indexa",
                                                "Ime",
                                                "Prezime",
                                                "Fakultet"])


def dodaj_studenta():
    print("----------------------")
    print("+ DODAVANJE STUDENTA +")
    print("----------------------")
    print("\n")

    ime = input("Unesite ime studenta: ")
    prezime = input("Unesite prezime studenta: ")

    postojeci_fakulteti = ["Matematika", "Elektrotehnika"]
    fakultet = input("Unesite fakultet sutdenta: ")

    if fakultet not in postojeci_fakulteti:
        print("Fakultet ne postoji!")
        return

    baza_fajl_citanje = open("baza.db", "r")
    svi_studenti = baza_fajl_citanje.readlines()
    baza_fajl_citanje.close()

    baza_fajl_pisanje = open("baza.db", "a+")

    zadnji_upisani = svi_studenti[-1]
    student = zadnji_upisani.split(",")

    trenutno_vrijeme = datetime.datetime.now()
    godina = trenutno_vrijeme.year
    indeks = student[1]

    godina_novog_studenta = str(godina)
    indeks_novog_studenta = str(int(indeks) + 1)

    baza_fajl_pisanje.write(godina_novog_studenta[2:] + ","
                            + indeks_novog_studenta + ","
                            + ime + ","
                            + prezime + ","
                            + fakultet + "\n")
    baza_fajl_pisanje.close()

    print("Uspjesno studenta " + ime + " " + prezime + ".", end="\n")


print("========================")
print("+  STUDENTSKA SLUZBA   +")
print("========================")

while True:

    print(" 1 - Stampaj listu studenata")
    print(" 2 - Dodaj novog studenta")
    print(" 3 - Obrisi studenta")
    print(" 4 - Suspenduj studenta")
    print("========================")
    komanda = input("Unesite zeljenu komandu: ")
    print("\n\n")

    if komanda == "1":
        stamapaj_spisak()
    elif komanda == "2":
        dodaj_studenta()

    print("\n\n\n\n\n")