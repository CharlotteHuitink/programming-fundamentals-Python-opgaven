# ==========================================
# Voorbeeld Opdracht
# Gegeven is een variabele 'leeftijd' met de waarde 25. Print de zin 'Mijn leeftijd is 25'
# ==========================================

leeftijd = 25
print('Mijn leeftijd is', leeftijd)  # Het resultaat is: Mijn leeftijd is 25
print(f"Mijn leeftijd is {leeftijd}")

# ==========================================
# Opgave 1.
# Gegeven is een variabele 'naam' met de waarde 'Jan' en de variabele 'leeftijd' met de waarde 25. Print de zin 'Mijn naam is Jan en ik ben 25 jaar oud'. Verander daarna de leeftijd naar 30 en print de zin opnieuw.
#
# Verwachte uitkomst is: 'Mijn naam is Jan en ik ben 25 jaar oud' en 'Mijn naam is Jan en ik ben 30 jaar oud'
# ==========================================
print("Opgave 1")

naam = 'Jan'
leeftijd = 30

print(f"Mijn naam is {naam} en ik ben {leeftijd} jaar oud")

# ==========================================
# Opgave 2.
# Gegeven zijn een aantal variabelen. Wat zijn de datatypes van de variabelen als je ze print met de type() method? Bedenk vooraf wat het datatype is en controleer daarna met de print functie of je het goed hebt.
# ==========================================
print("Opgave 2")
#a float
#b string
#c integer
#d string

a = 5 / 5

b = '12'

c = 5 * 5

d = 'Python' * 4

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)

# ==========================================
# Opgave 3.
# Variabele namen mag je zelf verzinnen, maar niet alle namen zijn toegestaan omdat ze al gebruikt worden door Python (keywords). Welke van de volgende variabele namen zijn toegestaan en welke niet?
# ==========================================
print("Opgave 3")

# And = 'something' mag wel met hoofdletter
# while = 'something' mag niet kleine letter
# Break = 'something' mag wel met hoofdletter
# awaiting = 'something' mag wel

And = 'something'
#while = 'something'
Break = 'something'
awaiting = 'something'

print(And)
print(Break)
print(awaiting)

# ==========================================
# Opgave 4.
# Schrijf een goede variabele naam voor onderstaande onderdelen. Denk aan de conventies voor Python variabelen.
#
# a.     Het totale aantal van het product bananen in een winkelmand: totaal_aantal_bananen
#
# b.     De minimale toegestane lengte voor een attractie in een pretpark: min_lengte_attractie
#
# c.     Het grootste getal in een rij met getallen: grootste_getal_in_rij
# ==========================================



# ==========================================
# Opgave 5.
# Gegeven is de variabele 'teller' met de waarde 10. Verhoog de waarde van de teller met 1. Gebruik de samengevoegde toekenning operator. Print de waarde van de teller. Herhaal dit proces maar verlaag de teller met 2. Print opnieuw de waarde van de teller.
#
# Verwachte uitkomst is: 11 en 9
# ==========================================
print("Opgave 5")

teller = 10
teller += 1
print(teller)

teller -=2
print(teller)
# ==========================================
# Opgave 6.
# Gegeven zijn de onderstaande statements. Welke van de print statements zullen een foutmelding geven en waarom?
#
# a. print(int(‘1490.99’) Foutmelding 1490.99 is een float, geen integer
#
# b. print(float(12)) Syntax goed
#
# c. print(int('1plus1')) Foutmelding het woord plus herkent een integer niet.
#
# d. print(str(25E10)) Syntax goed
# ==========================================
print("Opgave 6")


# ==========================================
# Opgave 7.
# Gegeven is de variabele getal_1 met waarde 3 en getal_2 met waarde 5. Schrijf de zin 'Het product van 3 en 5 is 15' door de variabelen te gebruiken in de zin. Pas een f-string toe.
# ==========================================
print("Opgave 7")

getal_1 = 3
getal_2 = 5

print(f"Het product van {getal_1} en {getal_2} is {getal_1*getal_2}")
