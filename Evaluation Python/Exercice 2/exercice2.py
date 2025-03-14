import random

class Personne:
    def __init__(self, nom, sante='saine', proba_infection=0.1):
        """
        Initialise une personne.

        :param nom: Le nom de la personne.
        :param sante: L'état de santé initial ('saine', 'infectée', 'immunisée').
        :param proba_infection: La probabilité d'être infecté par contact avec une personne infectée.
        """
        self.nom = nom
        self.sante = sante
        self.proba_infection = proba_infection

    def est_infectee(self):
        """
        Vérifie si la personne est infectée.
        """
        return self.sante == 'infectée'

    def contaminer(self):
        """
        Infecte la personne avec une certaine probabilité.
        """
        if self.sante == 'saine' and random.random() < self.proba_infection:
            self.sante = 'infectée'

    def guerir(self, proba_guerison=0.05):
        """
        Immunise la personne si elle était infectée, avec une certaine probabilité.

        :param proba_guerison: La probabilité que la personne guérisse.
        """
        if self.sante == 'infectée' and random.random() < proba_guerison:
            self.sante = 'immunisée'

    def __str__(self):
        """
        Représentation textuelle de la personne.
        """
        return f"{self.nom} ({self.sante})"


class Population:
    def __init__(self):
        """
        Initialise une population vide.
        """
        self.individus = []

    def ajouter_personne(self, personne):
        """
        Ajoute une personne à la population.

        :param personne: Un objet de type Personne.
        """
        self.individus.append(personne)

    def propager_maladie(self):
        """
        Simule la propagation de la maladie dans la population.
        """
        # Liste des personnes infectées
        infectes = [p for p in self.individus if p.est_infectee()]

        # Pour chaque personne saine, vérifier si elle est contaminée par un contact
        for personne in self.individus:
            if personne.sante == 'saine' and infectes:
                personne.contaminer()

    def afficher_statistiques(self):
        """
        Affiche les statistiques de la population.
        """
        sains = sum(1 for p in self.individus if p.sante == 'saine')
        infectes = sum(1 for p in self.individus if p.est_infectee())
        immunises = sum(1 for p in self.individus if p.sante == 'immunisée')

        print(f"Statistiques de la population :")
        print(f"- Sains : {sains}")
        print(f"- Infectés : {infectes}")
        print(f"- Immunisés : {immunises}")
        print()

    def __str__(self):
        """
        Représentation textuelle de la population.
        """
        return "\n".join(str(p) for p in self.individus)


# Simulation
if __name__ == "__main__":
    # 1. Créer une population de 1000 personnes
    population = Population()
    for i in range(1, 1001):
        population.ajouter_personne(Personne(f"Personne {i}", sante='saine', proba_infection=0.1))

    # 2. Introduire 10 personnes infectées au hasard
    infectes_initiaux = random.sample(population.individus, 10)
    for personne in infectes_initiaux:
        personne.sante = 'infectée'

    # 3. Simuler 30 jours de propagation
    for jour in range(1, 31):
        print(f"=== Jour {jour} ===")
        population.propager_maladie()

        # Guérir certaines personnes infectées
        for personne in population.individus:
            personne.guerir(proba_guerison=0.05)

        # Afficher les statistiques de la population
        population.afficher_statistiques()