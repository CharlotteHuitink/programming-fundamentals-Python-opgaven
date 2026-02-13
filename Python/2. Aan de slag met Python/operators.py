# ==========================================
# Voorbeeld Opdracht
# Schrijf de notatie van een 10 miljoen. Gebruik de ‘leesbaarheid methode’ van Python.
# print het getal.
# ==========================================

print(10_000_000)  # Het resultaat is: 10000000


# ==========================================
# Opgave 1:
# Welk getal is goed geschreven volgens de ‘leesbaarheid methode’
# print het getal.

#     100_00.000_001
#     1_000.00_001
#     1_000_000.000_1
# ==========================================
print(1_000_000.000_1)


# ==========================================
# Opgave 2:
# Hoe schrijf je de volgende getallen uit in de wetenschappelijke notatie van Python?
# print de getallen.

#     -12.000.000
#     0.13 met drie extra nullen (0.00013)
#     64.000.000.000
# ==========================================
print(-12E6)
print(0.13E-3)
print(64E9)


# ==========================================
# Opgave 3:
# Schrijf 5 miljoen uit. Hoe maak je daar met behulp van de wetenschappelijke notatie 0.05 van?
# ==========================================
print(0.05E8)

# Het goede antwoord
print(5_000_000)
print(5_000_000E-8)


# ==========================================
# Opgave 4:
# Wat is het antwoord? Probeer vooraf te bedenken of het antwoord een integer of een float is. Check je antwoord door een print uit te voeren.

# a. 11 * 3 (integer)
# b. 7.5 – 1.5 (float)
# c. 3 + 4.0 (float)
# d. 15 / 5 (float)
# ==========================================
print(11*3)
print(7.5-1.5)
print(3+4.0)
print(15/5)


# ==========================================
# Opgave 5:
# Wat is het antwoord? Probeer vooraf te bedenken of het antwoord een integer of een float is. Check je antwoord door een print uit te voeren.
# a. 18 // 4 (integer)
# b. 15.5 // 4 (integer) = float
# c. 10 % 4 (integer)
# d. 9 % 4.5 (float)
# ==========================================
print(18//4)
print(15.5//4)
print(10%4)
print(9%4.5)


# ==========================================
# Opgave 6:
# Hieronder staan een aantal expressies. Schrijf voor jezelf in een comment wat de volgorde is en reken het antwoord uit. Check dan met een print statement of je hetzelfde antwoord krijgt

#  A   8 + 2 * 3 = 8 + 6 = 14
#  B   (8 + 2) * 3 = 10 * 3 = 30
#  C   2 ** 3 ** 2 = 2^9 = 512
#  D   (2 ** 3) ** 2 = 8^2 = 64
#  E   100 - 5 ** 2 / 5 * 2 = 100 - 25 / 5 * 2 = 100 - 5 * 2 = 100 - 10  = 90
# ==========================================
print(8+2*3)
print((8+2)*3)
print(2**3**2)
print((2**3)**2)
print(100-5**2/5*2)

# ==========================================
# Opgave 7:
# Zet de volgende tekst om naar een Python string. Let op speciale tekens en spaties.
# Tip: Herhalende woorden kun je met een operator vaker printen
# Check het resultaat met een print statement

# A: Dit is de vorm van een dak / \
# B: ‘quotes’ ‘quotes’ ‘quotes’ ‘quotes’ spamspamspam
# C: Python’s syntax is “eenvoudig”
# ==========================================
print(str("Dit is de vorm van een / \\"))
print(str("'quotes' "*4+"spam"*3))
print("Pythons\'s syntax is \"eenvoudig\"")
