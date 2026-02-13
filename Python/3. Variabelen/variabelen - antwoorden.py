# ==========================================
# Voorbeeld Opdracht
# Gegeven is een variabele 'leeftijd' met de waarde 25. Print de zin 'Mijn leeftijd is 25'
# ==========================================

leeftijd = 25
print('Mijn leeftijd is', leeftijd)  # Het resultaat is: Mijn leeftijd is 25

# ==========================================
# Opgave 1.
# Gegeven is een variabele 'naam' met de waarde 'Jan' en de variabele 'leeftijd' met de waarde 25. Print de zin 'Mijn naam is Jan en ik ben 25 jaar oud'. Verander daarna de leeftijd naar 30 en print de zin opnieuw.
#
# Verwachte uitkomst is: 'Mijn naam is Jan en ik ben 25 jaar oud' en 'Mijn naam is Jan en ik ben 30 jaar oud'
# ==========================================

naam = 'Jan'
leeftijd = 25

print('Mijn naam is', naam, 'en ik ben', leeftijd, 'jaar oud')  # Het resultaat is: Mijn naam is Jan en ik ben 25 jaar oud

leeftijd = 30

print('Mijn naam is', naam, 'en ik ben', leeftijd, 'jaar oud')  # Het resultaat is: Mijn naam is Jan en ik ben 30 jaar oud



# ==========================================
# Opgave 2.
# Gegeven zijn een aantal variabelen. Wat zijn de datatypes van de variabelen als je ze print? Bedenk vooraf wat het datatype is en controleer daarna met de print functie of je het goed hebt.
# ==========================================

a = 5 / 5
print(type(a), a)  # Het resultaat is: <class 'float'> 1.0

b = '12'
print(type(b), b)  # Het resultaat is: <class 'str'> 12

c = 5 * 5
print(type(c), c)  # Het resultaat is: <class 'int'> 25

d = 'Python' * 4
print(type(d), d)  # Het resultaat is: <class 'str'> PythonPythonPythonPython


# ==========================================
# Opgave 3.
# Variabele namen mag je zelf verzinnen, maar niet alle namen zijn toegestaan omdat ze al gebruikt worden door Python (keywords). Welke van de volgende variabele namen zijn toegestaan en welke niet?
# ==========================================


# And = 'something'  # wel toegestaan. 'and' zonder hoofdletter is wel een keyword.
# while = 'something'  # niet toegestaan want 'while' is een keyword.
# Break = 'something'  # wel toegestaan.  'break' zonder hoofdletter is wel een keyword
# awaiting = 'something'  # wel toegestaan. Lijkt wel op keyword 'await'.

# LET OP: hoewel And bijvoorbeeld wel toegestaan is, is het niet aan te raden om die benaming te gebruiken. Het kan verwarrend zijn voor jou en andere developers omdat het wel lijkt op een keyword.



# ==========================================
# Opgave 4.
# Schrijf een goede variabele naam voor onderstaande onderdelen. Denk aan de conventies voor Python variabelen.
#
# a.     Het totale aantal van het product bananen in een winkelmand
#
# b.     De minimale toegestane lengte voor een attractie in een pretpark
#
# c.     Het grootste getal in een rij met getallen
# ==========================================

# a.
totale_aantal_bananen = 0
sum_bananas = 0
# b.
min_lengte_voor_achtbaan = 120
min_length_for_rollercoaster = 120
# c.
max_getal_uit_rij = 1000
highest_number_of_row = 1000

# Natuurlijk zijn er meerdere goede antwoorden mogelijk. Zorg wel dat je in ieder geval snake_case gebruikt. Liefst heb je zo kort mogelijke variabele namen, maar ze mogen zeker wat langer zijn als het daardoor duidelijker wordt waar de variabele voor staat. De lesstof en oefeningen zijn in het Nederlands geschreven, maar in de praktijk wordt meestal Engels gebruikt. Het is goed om daar alvast aan te wennen.



# ==========================================
# Opgave 5.
# Gegeven is de variabele 'teller' met de waarde 10. Verhoog de waarde van de teller met 1. Gebruik de samengevoegde toekenning operator. Print de waarde van de teller. Herhaal dit proces maar verlaag de teller met 2. Print opnieuw de waarde van de teller.
#
# Verwachte uitkomst is: 11 en 9
# ==========================================

teller = 10
teller += 1
print(teller)  # Het resultaat is: 11
teller -= 2
print(teller)  # Het resultaat is: 9




# ==========================================
# Opgave 6.
# Gegeven zijn de onderstaande statements. Welke van de print statements zullen een foutmelding geven en waarom?
#
# a. print(int(‘1490.99’)
#
# b. print(float(12))
#
# c. print(int('1plus1'))
#
# d. print(str(25E10))
# ==========================================


# a.
# print(int(‘1490.99’)  # Geeft een foutmelding omdat de string '1490.99' niet omgezet kan worden naar een integer. De string bevat een punt en dat is niet toegestaan in een integer.

# b.
# print(float(12))  # Geeft geen foutmelding. Het getal 12 wordt omgezet naar een float.

# c.
# print(int('1plus1'))  # Geeft een foutmelding omdat de string '1plus1' niet omgezet kan worden naar een integer. De string bevat letters en dat is niet toegestaan in een integer.

# d.
# print(str(25E10))  # Geeft geen foutmelding. Het getal 25E10 wordt omgezet naar een string. Het getal 25E10 is een float getal in wetenschappelijke notatie. Het wordt omgezet naar een string '250000000000.0'.



# ==========================================
# Opgave 7.
# Gegeven is de variabele getal_1 met waarde 3 en getal_2 met waarde 5. Schrijf de zin 'Het product van 3 en 5 is 15' door de variabelen te gebruiken in de zin. Pas een f-string toe.
#
# ==========================================

getal_1 = 3
getal_2 = 5

print(f"Het product van {getal_1} en {getal_2} is {getal_1 * getal_2}")  # Het resultaat is: Het product van 3 en 5 is 15

