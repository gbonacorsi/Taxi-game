
"""
while True: 
    try:
        prixHT = float(input("Prix HT : "))
        prixTTC = prixHT * 1.2
        print(f"Prix TTC : {prixTTC}")
        break

    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")

    finally:
        print("Fin du programme.")

"""


prixHT = float(input("Prix HT : "))
prixTTC = prixHT * 1.2
print(f"Prix TTC : {prixTTC}")