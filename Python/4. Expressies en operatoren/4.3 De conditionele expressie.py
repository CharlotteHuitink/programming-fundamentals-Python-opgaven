# Opgave 1: Even of oneven nummer
# Neem een nummer, bijvoorbeeld 42, en je wilt weten of het even of oneven is.
# Je gebruikt een eenvoudige check: als het nummer gedeeld door 2 geen rest heeft, dan is het even.
# Anders is het oneven.
# Dus, voor het nummer 42, zou je zeggen dat het "Even" is, omdat het zonder rest door 2 gedeeld kan worden.
# Schrijf de vergelijking nu in Python code.

# Conditionele expressie: expressie1 if conditie else expressie2
print("Opgave 1")

nummer = 42
print("Even" if nummer%2==0 else "Oneven")

# Opgave 2: Begroeting op Basis van het Uur van de Dag
# Stel je hebt een klok die aangeeft dat het 9 uur 's ochtends is (uur = 9).
# Afhankelijk van het tijdstip wil je een passende begroeting gebruiken: "Goedemorgen", "Goedemiddag", of "Goedenavond".
# Met een conditionele expressie kun je besluiten: als het uur minder dan 12 is, zeg "Goedemorgen";
# als het minder dan 18 is, zeg "Goedemiddag";
# en anders, zeg "Goedenavond".
# Voor 9 uur 's ochtends zou de gekozen begroeting "Goedemorgen" zijn.
# Tip: je kunt meerdere keren ‘else’ achterelkaar zetten.

# Conditionele expressie: expressie1 if conditie else expressie2
print("Opgave 2")

tijdstip = 22
print("Goedemorgen" if tijdstip<12 else "Goedemiddag" if tijdstip <18 else "Goedenavond")