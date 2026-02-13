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
#num1 = int(input("Geef een getal : "))
#num2 = int(input("Geef een ander getal : "))
#num3 = int(input("Geef nog een ander getal : "))

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