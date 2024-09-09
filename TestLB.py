# Importation des packages utiles
import pandas as pd
import os
from os.path import join
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def save_csv(url,dossier="csv_files") :
    
    # 1 : Récupération du contenu de la page web
    # url = 'https://www.data.gouv.fr/fr/datasets/trajets-realises-en-covoiturage-registre-de- preuve-de-covoiturage/'  

    response = requests.get(url)

    # Test : Vérification de la réussite de la requête (code 200)
    if response.status_code == 200:
        print("Page récupérée avec succès")
    else:
        print(f"Erreur lors de la récupération de la page :{response.status_code}")

    # 2 : Analyse du contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # 3 : Création un dossier pour sauvegarder les fichiers CSV
    os.makedirs(dossier, exist_ok=True)

    # 4 : Recherche de tous les liens vers les fichiers CSV (en supposant que l'extension .csv est présente dans les URLs)
    csv_links = soup.find_all('a', href=lambda href: href and ".csv" in href)

    # 5 : Téléchargement de chaque fichier CSV
    for link in csv_links:
        # Obtention de l'URL complète du fichier CSV
        csv_url = link['href']
        
        # Si le lien est relatif, nous le rendons absolu
        if not csv_url.startswith('http'):
            csv_url = requests.compat.urljoin(url, csv_url)
        
        # Téléchargement du fichier CSV
        csv_response = requests.get(csv_url)
        
        # Extraction du nom du fichier à partir de l'URL
        csv_filename = os.path.join(dossier, os.path.basename(csv_url))
        
        # Sauvegarde du fichier CSV
        with open(csv_filename, 'wb') as file:
            file.write(csv_response.content)
            print(f"Fichier CSV téléchargé : {csv_filename}")

def open_csv(dossier="csv_files") :

    # Import des fichiers
    dir_data = os.path.abspath(os.path.normpath(dossier))

    # Spécification du répertoire où se trouvent les fichiers CSV
    repertoire = dir_data

    # Liste de tous les fichiers CSV dans le répertoire
    fichiers_csv = [fichier for fichier in os.listdir(repertoire) if fichier.endswith('.csv')]

    # Ajout des noms des fichiers CSV dans une liste
    list_name= []
    for fichier in fichiers_csv:
        list_name.append(fichier)

    # Import des fichiers dans une liste
    list_file =[]
    for i in list_name:
        list_file.append(pd.read_csv(join(dir_data,i), sep=";"))
    
    # Return de la liste avec les fichiers csv
    return list_file