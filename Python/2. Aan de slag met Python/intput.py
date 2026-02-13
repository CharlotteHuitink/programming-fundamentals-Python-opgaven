# ==========================================
# Voorbeeld Opdracht
# Voer je naam in met de input() methode en print daarna je naam in de console.
# ==========================================

naam = input('Voer je naam in: ')  # voorbeeld invoer: Bart
print('Je naam is: ', naam)  # Het resultaat is: Je naam is: Bart


# ==========================================
# Opgave 1:
# Gegeven is het woord 'Python'. Schrijf een programma dat de gebruiker vraagt om input. Als de gebruiker het woord 'Python' invoert, print dan de boolean True, anders print False.
# ==========================================
invoer = input("Schrijf een woord op: ")
output = True if invoer == "Python" else False
print(output)


# ==========================================
# Opgave 2:
# Schrijf een programma dat de gebruiker vraagt om een getal. Voer daarna nog een getal in en print de som van de twee getallen.

# Verwachte uitkomst bij invoer van getallen 2 en 3:  De som van 2 en 3 is : 5
# ==========================================
getal_1 = int(input ("Vul een getal in : "))
getal_2 = int(input ("Vul nog een getal in : "))
som_1_2 = getal_1 + getal_2

print("De som van ", getal_1, "en ", getal_2, "is : ", som_1_2)
