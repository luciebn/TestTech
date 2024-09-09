# Test Technique Ecolab

Ce script est une pipeline d'intégration de l'indicateur : Voyages covoiturés via plateformes

## Setup

0. **Télécharger les fichiers csv**

    Télécharger les fichiers csv dans un dossier nommé "csv_files" à partir de l'URL : "https://www.data.gouv.fr/fr/datasets/trajets-realises-en-covoiturage-registre-de-preuve-de-covoiturage/".

    [L'objectif de la PISTE D'AMELIORATION, ci-dessous, est d'éviter cette étape.]

1. **Installer Python**

2. **Installer les dépendances**:

    Ouvrir un terminal dans le dossier du projet et run :
    ```
    pip install -r requirements.txt

3. **Lancer le streamlit**:

    Run :
    ```
    streamlit run streamlit.py
    ```
4. **Ouverture du streamlit**:

    Streamlit est un application web interective qui permet ici d'afficher les premiers traitement de la base de données.
   
## Description

Trois fichiers pythons composent le dossier partagé. 

Le premier nommé "TestLB.py" contient les fonctions créées pour :

1. [PISTE D'AMELIORATION] save_csv : télécharger les bases de données à partir de l'URL du site indiqué en argument et les stocker dans un dossier portant le nom indiqué en argument. Cette foncton ne retourne rien.

2. open_csv : Ouvrir les bases de données téléchargées dans le dossier indiqué et les mettre dans une liste. Cette fonction retourne la liste contenant les bases de données. 

Le second fichier nommé "main.py"  contient toutes les commandes qui permettent de :
- importer les fichier csv dans une liste à l'aide de la fonction "open_csv",
- concaténer l'ensemble des bases de données,
- calculer le pourcentage de données manquantes,
- afficher l'histogramme des données manquantes par variables,
- créer une base de données nettoyée dans laquelle les variables contenant plus de 30% de données manquantes ont été supprimées,
- définir une fonction qui permettra de générer la base de données nettoyées dans le streamlit.

Le troisième fichier nommé "streamlit.py" contient toutes les commandes qui permettent de :
- télécharger la base de données nettoyée,
- calculer et afficher les données manquantes dans chaque colonnes,
- calculer et afficher les statistiques descriptives des variables jugées utiles par types (catégorielles, dates, quantitatives).