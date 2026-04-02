import math

print("--- Witaj w Kalkulatorek v2.0! ---")

while True:
    print("\n--- Nowe obliczenie ---")
    print("Wybierz działanie: +, -, *, /, **, p (pierwiastek), k (pole kola) lub wpisz 'x' (wyjdź):")
    dzialanie = input("Twój wybór: ")

    # Sprawdzamy, czy użytkownik chce wyjść
    if dzialanie.lower() == 'x':
        print("Dzięki za korzystanie z kalkulatora! Do widzenia.")
        break

    a = float(input("Podaj pierwszą liczbę: "))

    if dzialanie == "p":
        if a >= 0:
            wynik = math.sqrt(a)    
        else:
            wynik = "Błąd! Liczba ujemna."
    elif dzialanie == "k":
        # Wzór na pole koła: Pi * r^2
        wynik = math.pi * (a ** 2)
        print(f"Użyta wartość Pi: {math.pi}")
    else:
        b = float(input("Podaj drugą liczbę: "))
        
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

    print(f"Wynik: {wynik}")