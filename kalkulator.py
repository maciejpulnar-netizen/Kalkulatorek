# Prosty kalkulator
print("--- Witaj w Kalkulatorku! ---")

# Pobieranie danych od użytkownika (input zawsze zwraca tekst, więc zmieniamy go na liczbę float)
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print("Wybierz działanie: +, -, *, /")
dzialanie = input("Twój wybór: ")

# Logika kalkulatora
if dzialanie == "+":
    wynik = a + b
elif dzialanie == "-":
    wynik = a - b
elif dzialanie == "*":
    wynik = a * b
elif dzialanie == "/":
    if b != 0:
        wynik = a / b
    else:
        wynik = "Błąd! Nie dziel przez zero."
else:
    wynik = "Nieznane działanie"

print(f"Wynik: {wynik}")