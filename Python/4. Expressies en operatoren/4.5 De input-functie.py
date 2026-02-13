# Opgave 1:
# Schrijf een programma dat de gebruiker vraagt 2 getallen in te voeren
# en als resultaat de som en het product van die getallen toont.
# Schrijf ook een passende prompt voor de input() functie
# en een passende tekst voor de print() functie.
print("Opgave 1")

getal_1 = int(input("Voer een getal in : "))
getal_2 = int(input("Voer nog een getal in : "))

print(f"De som van {getal_1} en {getal_2} is {getal_1+getal_2} en het product van deze getallen is {getal_1*getal_2}")


# Opgave 2:
# Schrijf een programma dat de gebruiker vraagt 2 getallen in te voeren
# en als resultaat de grootste van die twee getallen toont.
# Schrijf ook een passende prompt voor de input() functie
# en een passende tekst voor de print() functie.
print("Opgave 2")

getal_1 = int(input("Voer een getal in : "))
getal_2 = int(input("Voer nog een getal in : "))
grootste_getal = getal_1 if getal_1>getal_2 else getal_2

print(f"Het grootste getal wat je hebt opgegeven is {grootste_getal}")