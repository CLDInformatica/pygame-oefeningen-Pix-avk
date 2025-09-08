# Maak een functie genaamd rekenmachine met 3 argumenten:

#   - getal1
#   - getal2
#   - operatie

# De operatie kan plus, min, keer of delen zijn. 

# Doe iets met getal1 en getal2 afhankelijk van de operatie en return het resultaat.
# Dus als operatie plus is tel je de 2 getallen bij elkaar op, enz.
# Voer hierna de functie uit met verschillende inputs en bekijk de resultaten.
# Let op: Het is verplicht om een functie te gebruiken!

def rekenmachine(getal1, getal2, operatie):
    if operatie == "plus":
        resultaat = getal1 + getal2
        print(resultaat)
        return resultaat
    elif operatie == "min":
        resultaat = getal1 - getal2
        print(resultaat)
        return resultaat
    elif operatie == "keer":
        resultaat = getal1 * getal2
        print (resultaat)
        return resultaat
    elif operatie == "delen":
        resultaat = getal1 / getal2
        print (resultaat)
        return resultaat
    else:
        print("Operatie niet gevonden")


rekenmachine(2, 5, "keer")
rekenmachine(8, 4, "min")
rekenmachine(15, 3, "delen")
rekenmachine(2, 2, "plus")
