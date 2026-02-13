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
try :
    getal = int(input("voer een getal in: "))
    while getal != 0 :
        totaal += getal
        aantal_invoer += 1
        getal = int(input("Voer een getal in : "))
    if getal == 0 :
        print(f"totaal: {totaal}")
        print(f"gemiddelde : {totaal/aantal_invoer}")
    else :
        print("er zijn geen getallen ingevoerd")
except :
    print("Dit is geen nummer")

#TODO