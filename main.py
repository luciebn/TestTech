# Importation des packages utiles
import streamlit as st
import plotly.express as px
import pandas as pd
import os
import requests
from os.path import join
from bs4 import BeautifulSoup
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Importation des fonctions utiles créées dans "TestLB.py"
from TestLB import save_csv, open_csv

# Téléchargement des fichiers csv du site
# save_csv('https://www.data.gouv.fr/fr/datasets/trajets-realises-en-covoiturage-registre-de-preuve-de-covoiturage/')

# Création de la liste contenant les fichiers csv du site
list_file = open_csv()

df_concat = pd.concat(list_file, axis=0, ignore_index=True)
print("Le base de données concaténée est de taille (lignes, colonnes) : ",df_concat.shape)

# Détection des données manquantes
missing_percentage_init = df_concat.isnull().mean() * 100

# Création de l'histogramme des données manquantes par colonne
fig_init = px.bar(
    missing_percentage_init,
    x=missing_percentage_init.index,
    y=missing_percentage_init.values,
    title='Pourcentage des données manquantes par colonne',
    labels={'x': 'Colonnes', 'y': 'Pourcentage des données manquantes (%)'},
    color_discrete_sequence=['skyblue']
)

# Supprimer les colonnes qui ont plus de 30% de valeurs manquantes
df_cleaned = df_concat.loc[:, missing_percentage_init <= 30]

# Permettre la génération du dataframe dans le streamlit
def df_cleaned_loading (dossier="csv_files"):
    list_file = open_csv(dossier)
    df_concat = pd.concat(list_file, axis=0, ignore_index=True)
    missing_percentage_init = df_concat.isnull().mean() * 100
    df_cleaned = df_concat.loc[:, missing_percentage_init <= 30]
    return df_cleaned
     