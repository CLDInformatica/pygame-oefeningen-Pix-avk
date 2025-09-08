# Gegeven is een functie met 2 argumenten:
#   - getal1
#   - getal2

# Return de grootste van deze 2 getallen.
# Voer de functie daarna uit met verschillende waarden en print de uitkomst

def grootste(getal1, getal2):
    if getal1 > getal2:
        print(getal1)
        return getal1
    else:
        print(getal2)
        return getal2

grootste(3, 8)

grootste(9, 2)

grootste(4, -6)