# Exercice 2

def verifier_priorite(valeur):
   if valeur == "basse" or valeur == "haute":
      return valeur
   else:
      raise ValueError("la priorité doit etre basse ou haute")
   