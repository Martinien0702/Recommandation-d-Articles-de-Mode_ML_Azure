# Projet de Classification pour la Recommandation d'Articles de Mode

## Présentation du projet

Ce projet a été réalisé dans le cadre du cours **Outils infonuagiques (IFM30497-0040-H2025)** à l'Université. L'objectif est de développer un pipeline complet de machine learning pour prédire si un article de mode (robe) sera recommandé ou non, en utilisant **Azure Machine Learning Studio Designer**.

### Equipe
- Gansoaba Mohamed Tareq Ouedraogo
- Kevin Tchinda Ndiffo
- Martinien Mehoun

### Encadré par
Mouhcine Zakri

## Table des matières
1. [Objectifs](#objectifs)
2. [Données](#données)
3. [Architecture du Pipeline](#architecture-du-pipeline)
4. [Résultats et Performances](#résultats-et-performances)
5. [Technologies utilisées](#technologies-utilisées)
6. [Leçons apprises](#leçons-apprisées)
7. [Améliorations futures](#améliorations-futures)
8. [Références](#références)

## Objectifs

- Démontrer l'utilisation d'Azure ML Studio Designer pour automatiser le processus de modélisation prédictive
- Implémenter un pipeline complet de classification binaire
- Optimiser les performances du modèle à travers plusieurs itérations
- Comparer différents algorithmes de machine learning

## Données

Le projet utilise deux jeux de données :
1. **Données sur les ventes** : Informations sur la vente de robes
2. **Données sur les caractéristiques et recommandations** : Caractéristiques des robes avec étiquettes de recommandation (0 = non recommandé, 1 = recommandé)

## Architecture du Pipeline

### Etape 1 : Prétraitement des données

#### Partie I - Création de l'expérience et importation
- Création d'une nouvelle expérience dans Azure ML Studio
- Importation des datasets depuis des sources externes
- Analyse exploratoire initiale

#### Partie II - Nettoyage via script Python
- Script personnalisé pour automatiser le nettoyage
- Fusion des deux jeux de données
- Gestion des valeurs manquantes (remplacement de 'null', 'NULL' par 'nc')
- Normalisation du format des données

#### Partie III - Filtrage des lignes
- Suppression des lignes avec valeurs manquantes
- Alternative : imputation par le mode pour conserver plus de données

### Etape 2 : Séparation des données
- Répartition 70% entraînement / 30% test
- Stratification pour maintenir la distribution des classes
- Utilisation du module Column Selector pour sélectionner la variable cible

### Etape 3 : Modélisation initiale

#### Algorithmes testés :
- Two-Class Logistic Regression (modèle de base)
- Two-Class Decision Forest
- Two-Class Boosted Decision Tree
- Two-Class Support Vector Machine (SVM)
- Two-Class Neural Network

#### Processus :
- Configuration du module Train Model
- Évaluation avec Score Model et Evaluate Model
- Métriques analysées : F1 Score, Accuracy, AUC, matrice de confusion

### Etape 4 : Optimisation du modèle

#### Partie I - Changement d'algorithmes
- Comparaison systématique des performances
- Meilleur résultat initial : Boosted Decision Tree (F1 Score = 0.508)

#### Partie II - Révision du prétraitement
- Suppression des colonnes avec >50% de valeurs manquantes
- Remplacement des valeurs manquantes par le mode
- Normalisation des données avec méthode Z-Score

#### Partie III - Sélection des caractéristiques
- Analyse de pertinence des colonnes
- Suppression des variables non informatives (ex: Dress_ID)
- Sélection manuelle avec Select Columns in Dataset
- Utilisation de SelectKBest pour identifier les caractéristiques importantes

#### Partie IV - Prétraitement avancé avec script
- Standardisation du texte (mise en minuscule)
- Correction des erreurs de saisie
- Encodage ordinal pour Price et Size
- Encodage par fréquence pour les autres variables catégorielles

#### Partie V - Normalisation des données
- Application de la normalisation Z-Score
- Impact limité sur les performances (+0.05 F1 Score)

#### Partie VI - Analyse de corrélation
- Identification de coefficients de corrélation faibles entre caractéristiques et cible
- Conclusion : besoin d'ingénierie des caractéristiques pour améliorer les performances

#### Partie VII - Utilisation d'AutoML
- Lancement d'expérimentation avec Automated Machine Learning
- Configuration : classification, 70/30 split, métrique F1 Score
- Non aboutie en raison des limitations du compte utilisateur

## Résultats et Performances

### Performances initiales
- Logistic Regression : F1 Score = 0.50 (baseline)
- Boosted Decision Tree : F1 Score = 0.508 (meilleur modèle initial)

### Challenges rencontrés
- Données déséquilibrées et corrélations faibles
- Limitations des performances malgré l'optimisation
- Score F1 maximal atteint : < 0.6

### Insights clés
- L'approche sans code permet un prototypage rapide
- La qualité des données est cruciale pour les performances
- L'ingénierie des caractéristiques est nécessaire pour améliorer les résultats

## Technologies utilisées

- Azure Machine Learning Studio Designer
- Python (pandas pour les scripts personnalisés)
- Modules Azure ML : Clean Missing Data, Normalize Data, Select Columns, etc.
- Algorithmes : Logistic Regression, Decision Forest, Boosted Decision Tree, SVM, Neural Networks

## Leçons apprises

1. L'importance d'un prétraitement rigoureux des données
2. La nécessité d'analyser les corrélations avant la modélisation
3. La valeur de l'expérimentation itérative avec différents algorithmes
4. Les limitations de l'approche sans code pour des problèmes complexes

## Améliorations futures

1. Ingénierie des caractéristiques avancée
2. Techniques de rééchantillonnage pour gérer le déséquilibre des classes
3. Essais avec AutoML avec des ressources adéquates
4. Déploiement du modèle en production
5. Collecte de données supplémentaires pour améliorer la qualité des features

## Références

1. Microsoft Azure Machine Learning Documentation
2. Scikit-learn User Guide
3. Pandas Documentation
4. Machine Learning Yearning - Andrew Ng
5. OpenClassrooms - Initiation au Machine Learning

---
