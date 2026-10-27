# 🏦 Système de Gestion de Comptes Bancaires

Une application console en Python simulant un système bancaire automatisé avec gestion de comptes courants et de comptes épargne. Ce projet met en pratique les concepts fondamentaux de la **Programmation Orientée Objet (POO)**.

## 🚀 Fonctionnalités

### 💳 Compte Courant
* **Consultation de solde** : Affichage du solde actuel via un accès sécurisé.
* **Dépôt d'argent** : Créditer le compte d'un montant positif.
* **Retrait d'argent** : Débiter le compte avec vérification automatique du solde disponible (sécurité anti-découvert).

### 📈 Compte Épargne
* **Héritage complet** : Dispose de toutes les fonctionnalités de base du compte courant (Dépôt, Retrait, Affichage).
* **Calcul des intérêts** : Calcule et applique automatiquement les intérêts au solde en fonction d'un taux défini (ex: 3%).

### 🖥️ Interface Utilisateur (Menu Interactif)
* Interface en ligne de commande (CLI) intuitive et robuste.
* Gestion rigoureuse des erreurs de saisie utilisateur grâce à des blocs `try/except`.

## 🛠️ Concepts POO Mis en Œuvre

* **Encapsulation (Sécurité)** : Le solde des comptes est rendu strictement privé (`self.__solde`) pour empêcher toute modification directe ou frauduleuse depuis l'extérieur des classes. La lecture du solde est contrôlée de manière sécurisée par la méthode `get_solde()`.
* **Héritage** : La classe `compte_epargne` hérite de la classe parente `compte_bancaire`, évitant la duplication de code pour les opérations communes.
* **Extension de Méthode** : Utilisation de `super()` dans le calcul des intérêts pour réutiliser proprement la logique de dépôt de la classe parente.

## 📦 Installation et Exécution

1. **Cloner le projet** :
   ```bash
   git clone https://github.com
   ```

2. **Accéder au dossier du projet** :
   ```bash
   cd Gestion-Compte-Bancaire-Python
   ```

3. **Lancer l'application** :
   ```bash
   python main.py
   ```

---
💡 *Projet d'apprentissage développé pour consolider les bases de la POO et de la manipulation des classes en Python.*
