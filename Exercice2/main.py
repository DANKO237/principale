from validation import verifier_priorite 
from taches import ajouter_tache

taches = []

while True:
  titre = input("entrer le titre")
  priorite = input("entrer la priorite")
  try:
      verifier_priorite(priorite)
      ajouter_tache(taches, titre, priorite)
      print(taches)
      break
  except ValueError as erreur:
   print(erreur)  
    