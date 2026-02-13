# ==========================================
# Voorbeeld Opdracht
# Gegeven zijn de variabelen a = 3 en b = 10. Evalueer met een if statement of a groter is dan b. Als dat zo is, print dan a. Als dat niet zo is, print dan b.
# ==========================================

a = 3
b = 10

if a > b:
    print(a)
else:
    print(b)

# ==========================================
# Opgave 1:
# Gegeven is een int input getal_1 en getal_2 en drie print methodes.
# Schrijf een if statement dat controleert of getal1 een veelvoud is van getal2,
# andersom of dat beide getallen geen veelvoud zijn van de ander.
# Zet de juiste print methode op de goede plek in je if statement.
# Voorbeeld goede output: 10 is een veelvoud van 5
# ==========================================
print("Opgave 1")

getal_1 = int(input("voer een getal in: "))
getal_2 = int(input("voer een getal in: "))

if getal_1 % getal_2 == 0 :
    print(f"{getal_1} is een veelvoud van {getal_2}")
elif getal_2 % getal_1 == 0 :
    print(f"{getal_2} is een veelvoud van {getal_1}")
else :
    print(f"{getal_1} en {getal_2} zijn geen veelvouden van elkaar")

# ==========================================
# Opgave 2:
# De basisprijs van een bioscoopkaartje is 12 euro.

# - Kinderen tot 5 jaar zijn gratis
# - kinderen van 5 tot 12 jaar betalen de halve prijs.
# - Personen tussen 13 en 54 jaar moeten de volle prijs betalen
# - vanaf 55 jaar is de toegang weer gratis.

# Maak een programma dat de te betalen prijs afdrukt nadat je de leeftijd hebt ingevoerd als input.
# Voorbeeld output: Voor de leeftijd 10 jaar is de prijs: 6.0
# ==========================================
print("Opgave 2")

leeftijd = int(input("voer je leeftijd in: "))
prijs = 12

if leeftijd < 5 or leeftijd >=55:
    prijs = 0
elif leeftijd >= 5 and leeftijd <= 12 :
    prijs = prijs/2
elif leeftijd >=13 and leeftijd <= 54 :
    prijs = prijs

print(f"Voor de leeftijd {leeftijd} jaar is de prijs: {prijs}")


# ==========================================
# Opgave 3:
# Schrijf een programma dat 3 gehele getallen (integers) sorteert.
# De willekeurige inputs worden opgeslagen in de variabelen num1, num2 en num3
# (maak deze variabelen met inputs zelf aan).
# Schrijf een if statement die het laagste getal in num1 stopt,
# het middelste getal in num2 en het hoogste getal in num3.

# Print de variabelen in de volgorde num1, num2, num3.
# Voorbeeld input: 3 1 2
# Voorbeeld output: 1 2 3
# ==========================================
print("Opgave 3")

#Mijn antwoord
num1 = int(input("Geef een getal : "))
num2 = int(input("Geef een ander getal : "))
num3 = int(input("Geef nog een ander getal : "))

if num1 > num2 and num1 > num3 and num2 > num3 :
    print(num3, num2, num1)
elif num1 > num2 and num1 > num3 and num3 > num2 :
    print(num2, num3, num1)
elif num2 > num1 and num2 > num3 and num1 > num3 :
    print(num3, num1, num2)
elif num2 > num1 and num2 > num3 and num3 > num1 :
    print(num1, num3, num2)
elif num3 > num1 and num3 > num2 and num1 > num2 :
    print(num2, num1, num3)
elif num3 > num1 and num3 > num2 and num2 > num1 :
    print(num1, num2, num3)

# Antwoord van Novi
num1 = int(input("voer een getal in: "))
num2 = int(input("voer een getal in: "))
num3 = int(input("voer een getal in: "))
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1
print(num1, num2, num3)

#Inclusief betere uitleg
num1 = 30
num2 = 20
num3 = 10

print(f"Origineel: {num1} - {num2} - {num3}")

if num1 > num2:
    num1, num2 = num2, num1
    print(f"Switch 1: {num1} - {num2} - {num3}")
if num2 > num3:
    num2, num3 = num3, num2
    print(f"Switch 2: {num1} - {num2} - {num3}")
if num1 > num2:
    num1, num2 = num2, num1
    print(f"Switch 3: {num1} - {num2} - {num3}")

print(f"Eindresultaat: {num1} - {num2} - {num3}")

# ==========================================
# Opgave 4:
# Gegeven is de variabele 'totaal' met een waarde van 0.
# Schrijf een programma dat herhaaldelijk een getal als input vraagt.
# Elk getal dat je invoert moet moet worden opgeteld bij het totaal.
# Als je 0 invoert moet het programma stoppen en met een print statement het totaal
# en het gemiddelde van de getallen afdrukken (dus totaal / aantal inputs).
# Als er geen getallen zijn ingevoerd moet de volgende string worden geprint: "er zijn geen getallen ingevoerd".
#
# Voorbeeld input: 2, 4, 6, 0
# Voorbeeld output: totaal: 12, gemiddelde: 4.0
# ==========================================
print("Opgave 4")

totaal = 0
getal = int(input("Voer een getal in : "))
aantal_invoer = 0

while getal != 0 :
    totaal += getal
    aantal_invoer += 1
    getal = int(input("Voer een getal in : "))
if getal == 0 :
    print(f"totaal: {totaal}")
    print(f"geiddelde : {totaal/aantal_invoer}")
else :
    print("er zijn geen getallen ingevoerd")


# ==========================================
# Opgave 5:
# Schrijf een input die een integer verwacht en stop deze in de variabele “factor”.
# Schrijf daarna een programma dat de tafel van “factor” afdrukt.
# Print de tafel van 'factor' van 1 tot en met 10.

# Voorbeeld input: 5
# Voorbeeld output:
#   1 x 5 = 5
#   2 x 5 = 10
#   3 x 5 = 15    # enz. tot en met 10
# ==========================================
print("Opgave 5")

factor = int(input("geef een getal : "))

for i in range(1,11) :
    print (f"{i} x {factor} = {i * factor}")






