import math

print("--- Witaj w Kalkulatorek v2.0! ---")

while True:
    print("\n--- Nowe obliczenie ---")
    print("Wybierz działanie: +, -, *, /, **, p (pierwiastek), % (obliczanie %), k (pole kola) lub wpisz 'x' (wyjdź):")
    dzialanie = input("Twój wybór: ")

    # Sprawdzamy, czy użytkownik chce wyjść
    if dzialanie.lower() == 'x':
        print("Dzięki za korzystanie z kalkulatora! Do widzenia.")
        break
    
 
    #Sprawdzam jakie działanie wpisane    
    if dzialanie == "p":
        try:
            a = float(input("Podaj liczbę do pierwiastkowania: "))
            if a >= 0:
                wynik = math.sqrt(a)
            else:
                wynik = "Błąd! Liczba ujemna."
        except ValueError:
            print("To nie jest liczba! Kolejna próba")
        continue

    elif dzialanie == "k":
        try:
            a = float(input("Podaj promień koła (r): "))
            wynik = math.pi * (a ** 2)
            print(f"Użyta wartość Pi:  {math.pi:.2f}")
            print(f"Wynik: {wynik: .2f} ")
        except ValueError:
            print("To nie jest liczba! Kolejna próba")
        continue

    elif dzialanie == "%":
        try:
            a = float(input("Ile procent (np. 15): "))
            b = float(input("Z jakiej liczby: "))
                # Wzór: (procent / 100) * liczba
            wynik = (a / 100) * b
            print(f"Wynik: {wynik: .2f}")
        except ValueError:
                print("Błąd! Podaj poprawne liczby.")
        continue
    elif dzialanie == "**":
        try:
            a = float(input("Podaj podstawę potęgi: "))
            b = float(input("Podaj wykładnik (do której potęgi): "))
            wynik = a ** b
        except ValueError:
            print("Błąd! Podaj poprawne liczby.")
            continue    
    else:
        # Dla pozostałych działań (+, -, *, /)
        try:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
        except ValueError:
            print("To nie jest liczba! Kolejna próba")
            continue

        if dzialanie == "+":
            wynik = a + b
        elif dzialanie == "-":
            wynik = a - b
        elif dzialanie == "*":
            wynik = a * b
        elif dzialanie == "/":
            wynik = a / b if b != 0 else "Nie dziel przez zero!"
        elif dzialanie == "**":
            wynik = a ** b        
        else:
            wynik = "Nieznane działanie"

    print(f"Wynik: {wynik: .2f}")