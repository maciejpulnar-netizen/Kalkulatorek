# Prosty kalkulator
print("--- Witaj w Kalkulatorku! ---")

# Pobieranie danych od użytkownika (input zawsze zwraca tekst, więc zmieniamy go na liczbę float)
a = float(input("Podaj pierwszą liczbę: "))


print("Wybierz działanie: +, -, *, /, **, p")
dzialanie = input("Twój wybór: ")

# Logika kalkulatora
if dzialanie == "p":
    if a >= 0:
        wynik = a ** 0.5
    else:
        wynik = "Błąd! Nie podnosź do zera."
else:
    # Tylko jeżeli nie wybrano pierwiastka pytaj o drugą zmienną
    b = float(input("Podaj drugą liczbę: "))
    if dzialanie == "+":
        wynik = a + b
    elif dzialanie == "-":
        wynik = a - b
    elif dzialanie == "*":
        wynik = a * b
    elif dzialanie == "/":
        wynik = a / b if b != 0 else "Błąd! Nie dziel przez zero."
    
    elif dzialanie == "**":
        wynik = a ** b
    

print(f"Wynik: {wynik}")