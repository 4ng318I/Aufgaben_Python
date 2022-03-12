'''
In dieser Aufgabe sollen Sie für einen Pizzalieferservice die Preisberechnung implementieren. Nehmen wir vereinfachend an, jede Pizza Kostet 11€. Dabei gelten folgende Regelung zum Rabatt: Wenn wir 5 oder mehr Pizzen bestellen, dann erhalten wir einen Rabatt von 10%. Wenn wir die Pizzen selbst abholen, dann erhalten wir pro Pizza einen Nachlass von 2€. Schreiben Sie eine Funktion, die den Rechnungbetrag ermittelt.'''

Pizzen = 0
abholen = False
preis = 0

def Pizzen_preis(Pizzen, abholen):
    if Pizzen >= 5 and abholen == False:
        preis = (Pizzen * 11.0)
        descuento = preis / 10
        total = preis - descuento
        print(f"Die Pizzen kostet {total}")
    elif Pizzen > 0 and abholen == True:
        preis = (Pizzen * 9)
        print(f"Die Pizzen kostet {preis}")
    
    

Pizzen_preis(5, False)

    