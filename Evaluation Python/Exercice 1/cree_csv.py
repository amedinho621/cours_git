import csv

# Données à écrire dans le fichier CSV
donnees = [
    {"Prefecture": "Conakry", "Date": "2014-08-01", "Cases": 10, "Deces": 5},
    {"Prefecture": "Conakry", "Date": "2014-08-15", "Cases": 15, "Deces": 8},
    {"Prefecture": "Conakry", "Date": "2014-08-01", "Cases": 22, "Deces": 12},
    {"Prefecture": "Boke", "Date": "2014-08-01", "Cases": 3, "Deces": 1},
    {"Prefecture": "Boke", "Date": "2014-08-15", "Cases": 5, "Deces": 2},
    {"Prefecture": "Boke", "Date": "2014-09-01", "Cases": 8, "Deces": 4},
    {"Prefecture": "Kindia", "Date": "2024-08-01", "Cases": 5, "Deces": 2},
    {"Prefecture": "Kindia", "Date": "2024-08-15", "Cases": 8, "Deces": 3},
    {"Prefecture": "Kindia", "Date": "2024-09-01", "Cases": 12, "Deces": 6},
]

# Nom du fichier CSV
nom_fichier = "ebola_guinea.csv"

# Écrire les données dans le fichier CSV
with open(nom_fichier, mode='w', newline='', encoding='utf-8') as fichier:
    # Définir les en-têtes des colonnes
    champs = ["Prefecture", "Date", "Cases", "Deces"]
    
    # Créer un objet DictWriter
    writer = csv.DictWriter(fichier, fieldnames=champs)
    
    # Écrire l'en-tête
    writer.writeheader()
    
    # Écrire les lignes de données
    for ligne in donnees:
        writer.writerow(ligne)

print(f"Le fichier {nom_fichier} a été créé avec succès.")