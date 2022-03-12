# Nehmen wir an, wir hätten eine Spedition. Wir bekommen einen Großauftrag und müssen 1000 Kisten ausliefern. In unseren Lkw passen pro Fahrt jedoch nur 75 Kisten. Berechnen Sie, wie oft wir fahren müssen und wie viele Kisten in der letzten Fahrt transportiert werden.


Bestell_menge = 1000
Lkw_kapazitaet = 75

anzahl_fahrten = Bestell_menge // Lkw_kapazitaet
restmenge = Bestell_menge % Lkw_kapazitaet

if restmenge != 0:
    anzahl_fahrten += 1

print(f"Die anzahl fahrten werden: {anzahl_fahrten}")
print(f"Die restmenge Kisten sind: {restmenge}")
        
    
    



