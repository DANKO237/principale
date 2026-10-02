# Exercice 1

taches = ["Reviser python", "Faire les exercices", "lire le cours"]
print(taches[0])
print(taches[1])
print(taches[2])
while True:
  try:
    numero = int(input("entrer un numero"))
    print(numero)
  except ValueError:
    print("entrer un nombre entier")
  else:
    if 1<= numero <=len(taches):
        print(taches[numero - 1])
        break
    else:
        print("choisissez un numero entre 1 et 3")
  finally:
    print("Fin de tentative")
