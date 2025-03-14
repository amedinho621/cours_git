import csv
import matplotlib.pyplot as plt

# 1. Fonction pour lire le fichier CSV et stocker les données dans une liste de dictionnaires
def lire_fichier_csv(nom_fichier):
    """
    Lit un fichier CSV et retourne les données sous forme d'une liste de dictionnaires.

    :param nom_fichier: Le chemin du fichier CSV.
    :return: Une liste de dictionnaires représentant les données du fichier.
    """
    donnees = []
    try:
        with open(nom_fichier, mode='r', encoding='utf-8') as fichier:
            lecteur_csv = csv.DictReader(fichier)
            for ligne in lecteur_csv:
                donnees.append(ligne)
        print(f"Le fichier {nom_fichier} a été lu avec succès.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier {nom_fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")
    return donnees


# 2. Fonction pour calculer le nombre total de cas et de décès par préfecture
def calculer_statistiques(donnees):
    """
    Calcule le nombre total de cas et de décès pour chaque préfecture.

    :param donnees: Une liste de dictionnaires contenant les données du fichier CSV.
    :return: Un dictionnaire où les clés sont les noms des préfectures et les valeurs sont des dictionnaires
             contenant le nombre total de cas et de décès.
    """
    statistiques = {}

    for ligne in donnees:
        prefecture = ligne['Prefecture']
        cas = int(ligne['Cases'])
        deces = int(ligne['Deces'])

        if prefecture not in statistiques:
            statistiques[prefecture] = {'cas': 0, 'deces': 0}

        statistiques[prefecture]['cas'] += cas
        statistiques[prefecture]['deces'] += deces

    return statistiques


# 3. Fonction pour créer un diagramme à barres montrant le nombre total de cas par préfecture
def afficher_diagramme_cas(statistiques):
    """
    Affiche un diagramme à barres montrant le nombre total de cas par préfecture.

    :param statistiques: Un dictionnaire contenant les statistiques par préfecture.
    """
    prefectures = list(statistiques.keys())
    cas = [statistiques[p]['cas'] for p in prefectures]

    plt.figure(figsize=(10, 6))
    plt.bar(prefectures, cas, color='blue')
    plt.title('Nombre total de cas par préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Nombre de cas')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


# 4. Fonction pour créer un diagramme à barres montrant le taux de mortalité par préfecture
def afficher_diagramme_taux_mortalite(statistiques):
    """
    Affiche un diagramme à barres montrant le taux de mortalité par préfecture.

    :param statistiques: Un dictionnaire contenant les statistiques par préfecture.
    """
    prefectures = list(statistiques.keys())
    taux_mortalite = [(statistiques[p]['deces'] / statistiques[p]['cas']) * 100 for p in prefectures]

    plt.figure(figsize=(10, 6))
    plt.bar(prefectures, taux_mortalite, color='red')
    plt.title('Taux de mortalité par préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Taux de mortalité (%)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


# Programme principal
if __name__ == "__main__":
    # 1. Lire le fichier CSV
    fichier_csv = '/home/iniesta/Bureau/Evaluation Python/Exercice 1/ebola_guinea.csv'  # Remplacez par le chemin de votre fichier
    donnees = lire_fichier_csv(fichier_csv)

    if donnees:
        # 2. Calculer les statistiques
        statistiques = calculer_statistiques(donnees)

        # Afficher les statistiques
        print("\nStatistiques par préfecture :")
        for prefecture, stats in statistiques.items():
            print(f"{prefecture}: {stats['cas']} cas, {stats['deces']} décès")

        # 3. Afficher les diagrammes
        afficher_diagramme_cas(statistiques)
        afficher_diagramme_taux_mortalite(statistiques)