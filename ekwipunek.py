# zarządzanie ekwipunkiem
def pokaz_ekwipunek(ekwipunek, waga):
    # print(a)
    for nazwa, dane in ekwipunek.items():
        print(f"{nazwa} | Ilość: {dane['ilosc']} | Waga: {dane['waga']} | Wartość: {dane['wartosc']}")
    print()
    print(f"Całkowita waga {waga}")
    print()


def pokaz_zloto(zloto):
    print(f"Twoje saldo w złocie wynosi: {zloto}")
    print()


def pokaz_sklep(sklep):
    for nazwa, dane in sklep.items():
        print(f"{nazwa} | Cena: {dane['wartosc']}")
    print()


def dodaj_przedmiot(nazwa_przedmiotu, ekwipunek, max_waga, waga, wartosc):
    if nazwa_przedmiotu in ekwipunek:
        waga_przedmiotu = ekwipunek[nazwa_przedmiotu]["waga"]
        if czy_mozna_podniesc(ekwipunek, max_waga, waga_przedmiotu):
            ekwipunek[nazwa_przedmiotu]["ilosc"] += 1
            return True
        else:
            print("Masz za mało miejsa w ekwipunku!")
            print()
            return False
    else:
        # waga = float(input("Jaka waga wariacie: "))
        if waga <= 0:
            print("Ten przedmiot musi istnieć w naszym uniwersum")
            print()
            return False
        else:
            if czy_mozna_podniesc(ekwipunek, max_waga, waga):
                # wartosc = int(input("Jaka wartość wariacie: "))
                if wartosc < 0:
                    print("Znajdź coś co nie wprowadzi cię w długi")
                    print()
                    return False
                else:
                    ekwipunek[nazwa_przedmiotu] = {
                        "ilosc": 1,
                        "waga": waga,
                        "wartosc": wartosc
                    }
                    print()
                    return True
            else:
                print("Masz za mało miejsca w ekwipunku!")
                print()
                return False


def uzyj_przedmiot(nazwa_przedmiotu, ekwipunek):
    if nazwa_przedmiotu in ekwipunek:
        ekwipunek[nazwa_przedmiotu]["ilosc"] -= 1
        print("Użyto itemu:", nazwa_przedmiotu)
        print()
        if ekwipunek[nazwa_przedmiotu]["ilosc"] <= 0:
            del ekwipunek[nazwa_przedmiotu]
    else:
        print("nie masz tego itemu")
        print()
    print()


def kup_przedmiot(sklep, ekwipunek, nazwa_przedmiotu, zloto, max_waga):
    if nazwa_przedmiotu in sklep:
        cena_przedmiotu = sklep[nazwa_przedmiotu]["wartosc"]
        waga = sklep[nazwa_przedmiotu]["waga"]
        wartosc = sklep[nazwa_przedmiotu]["wartosc"]
        if zloto >= cena_przedmiotu:
            if dodaj_przedmiot(nazwa_przedmiotu, ekwipunek, max_waga, waga, wartosc):
                print(f"Kupiłeś przedmiot {nazwa_przedmiotu} w cenie {cena_przedmiotu}")
                print()
                zloto -= cena_przedmiotu
                return zloto
            return zloto
        else:
            print("Nie stać cię na to")
            print()
            return zloto
    else:
        print("Taki przedmiot nie jest sprzedawany w tym sklepie")
        print()
        return zloto


def sprzedaj_przedmiot(ekwipunek, nazwa_przedmiotu, zloto):
    if nazwa_przedmiotu in ekwipunek:
        cena_przedmiotu = ekwipunek[nazwa_przedmiotu]["wartosc"]
        print(f"Chcesz sprzedać przedmiot {nazwa_przedmiotu}. Potwierdź tak/nie")
        potwierdz = input("Potwierdź sprzedaż: ")
        if potwierdz == "tak":
            print(f"Sprzedano przedmiot {nazwa_przedmiotu} za {cena_przedmiotu}")
            print()
            del ekwipunek[nazwa_przedmiotu]
            zloto += cena_przedmiotu
            return zloto
        elif potwierdz == "nie":
            print("Nie sprzedano bo nie potrafisz się zdecydować")
            print()
            return zloto
        else:
            print("Nie podano konkretnej odpowiedzi, więc odmówiono sprzedarzy")
            print()
            return zloto
    else:
        print("Nie masz takiego przedmiotu")
        print()
        return zloto

# sprawdzające


def sprawdz_przedmiot(nazwa_przedmiotu, ekwipunek):
    if nazwa_przedmiotu in ekwipunek:
        print(f"Masz ten item w ilości: {ekwipunek[nazwa_przedmiotu] ['ilosc']}")
        print(f"Waga pojedyńczego przedmiotu to: {ekwipunek[nazwa_przedmiotu] ['waga']}")
        print(f"Wartość pojedyńczego przedmiotu to: {ekwipunek[nazwa_przedmiotu] ['wartosc']}")
        print()
    else:
        print("Nie masz tego itemu")
    print()


def oblicz_waga(ekwipunek):
    waga = 0
    for nazwa, dane in ekwipunek.items():
        waga_przedmiotow = dane["waga"] * dane["ilosc"]
        waga += waga_przedmiotow
    return waga


def czy_mozna_podniesc(ekwipunek, max_waga, waga_przedmiotu):
    obecna_waga = oblicz_waga(ekwipunek)
    if obecna_waga + waga_przedmiotu >= max_waga:
        return False
    else:
        return True


# menu


def pytanie():
    print("Opcje")
    print("1 - Pokaż ekwipunek, 2 - Dodaj, 3 - Użyj, 4 - Sprawdź 5 - Wyjdź, 6 - Pokaż saldo, 7 - Pokaż asortyment, 8 - Kup, 9 - Sprzedaj")
    opcja = input("Co chcesz zrobić: ")
    return opcja

# main


def ekwipunek():
    # stan początkowy
    ekwipunek = {
        "miecz": {
            "ilosc": 1,
            "waga": 6.9,
            "wartosc": 34
        },
        "mikstura": {
            "ilosc": 1,
            "waga": 0.5,
            "wartosc": 15
        },
        "zbroja": {
            "ilosc": 1,
            "waga": 35,
            "wartosc": 69
        }

    }
    # asortyment sklepu
    sklep = {
        "miecz": {
            "waga": 6.9,
            "wartosc": 34
        },
        "tarcza": {
            "waga": 6,
            "wartosc": 40
        },
        "mikstura": {
            "waga": 0.5,
            "wartosc": 15
        },
        "szmelc": {
            "waga": 0.1,
            "wartosc": 420
        }
    }

    zloto = 50
    max_waga = 120
    waga = oblicz_waga(ekwipunek)
    pokaz_ekwipunek(ekwipunek, waga)

    while True:  # 1 > 0
        wybor = pytanie()

        # print("Opcja", wybor)
        if wybor == "1":
            pokaz_ekwipunek(ekwipunek, waga)
        elif wybor == "2":
            nazwa_przedmiotu = input("Co chcesz dodac do eq: ")
            waga = float(input("Jaka waga wariacie: "))
            wartosc = int(input("Jaka wartość wariacie: "))
            dodaj_przedmiot(nazwa_przedmiotu, ekwipunek, max_waga, waga, wartosc)
        elif wybor == "3":
            nazwa_przedmiotu = input("Co chcesz uzyc z eq: ")
            uzyj_przedmiot(nazwa_przedmiotu, ekwipunek)
        elif wybor == "4":
            nazwa_przedmiotu = input("Co chcesz sprawdzic z eq: ")
            sprawdz_przedmiot(nazwa_przedmiotu, ekwipunek)
        elif wybor == "5":
            print("Spadaj")
            break
        elif wybor == "6":
            pokaz_zloto(zloto)
        elif wybor == "7":
            pokaz_sklep(sklep)
        elif wybor == "8":
            nazwa_przedmiotu = input("Co chcesz kupić ze sklepu: ")
            zloto = kup_przedmiot(sklep, ekwipunek, nazwa_przedmiotu, zloto, max_waga)
        elif wybor == "9":
            nazwa_przedmiotu = input("Co chcesz sprzedać: ")
            zloto = sprzedaj_przedmiot(ekwipunek, nazwa_przedmiotu, zloto)
        else:
            print("Brak takiej opcji. Wybierz coś konkretnego")
            print()

        waga = oblicz_waga(ekwipunek)

        if waga >= max_waga:
            print(f"Jesteś przeciążony o {waga - max_waga}! Usuń albo użyj jakiś item")
            print()


ekwipunek()
