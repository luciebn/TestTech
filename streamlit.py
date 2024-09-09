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

from main import df_cleaned_loading  # Importer le fichier `main.py`

# Appeler la fonction `load_data` depuis le fichier `main.py`
df = df_cleaned_loading()

# Titre de l'application streamlit
st.title("Indicateur : Voyages covoiturés via plateformes")

# Détection des données manquantes de la base nettoyée
missing_percentage = df.isnull().mean() * 100

# Création de l'histogramme des données manquantes par colonne
fig = px.bar(
    missing_percentage,
    x=missing_percentage.index,
    y=missing_percentage.values,
    title='Pourcentage des données manquantes par colonne après nettoyage',
    labels={'x': 'Colonnes', 'y': 'Pourcentage des données manquantes (%)'},
    color_discrete_sequence=['skyblue']
)

# Affichage du graphique des données manquantes de la base de données nettoyée dans Streamlit
st.subheader("Pourcentage de données manquantes par variable de la base de données nettoyée")
st.plotly_chart(fig, use_container_width=True)

# Calcul des statistiques descriptives pour les données catégorielles
start_town_stats = {
    'Nombre total de catégories': df['journey_start_town'].nunique(),
    'Distribution des catégories': df['journey_start_town'].value_counts(),
    'Fréquence relative (%)': df['journey_start_town'].value_counts(normalize=True) * 100,
    'Mode': df['journey_start_town'].mode()[0]
}

end_town_stats = {
    'Nombre total de catégories': df['journey_end_town'].nunique(),
    'Distribution des catégories': df['journey_end_town'].value_counts(),
    'Fréquence relative (%)': df['journey_end_town'].value_counts(normalize=True) * 100,
    'Mode': df['journey_end_town'].mode()[0]
}

start_depart_stats = {
    'Nombre total de catégories': df['journey_start_department'].nunique(),
    'Distribution des catégories': df['journey_start_department'].value_counts(),
    'Fréquence relative (%)': df['journey_start_department'].value_counts(normalize=True) * 100,
    'Mode': df['journey_start_department'].mode()[0]
}

end_depart_stats = {
    'Nombre total de catégories': df['journey_end_department'].nunique(),
    'Distribution des catégories': df['journey_end_department'].value_counts(),
    'Fréquence relative (%)': df['journey_end_department'].value_counts(normalize=True) * 100,
    'Mode': df['journey_end_department'].mode()[0]
}

operator_stats = {
    'Nombre total de catégories': df['operator_class'].nunique(),
    'Distribution des catégories': df['operator_class'].value_counts(),
    'Fréquence relative (%)': df['operator_class'].value_counts(normalize=True) * 100,
    'Mode': df['operator_class'].mode()[0]
}

passenger_seats_stats = {
    'Nombre total de catégories': df['passenger_seats'].nunique(),
    'Distribution des catégories': df['passenger_seats'].value_counts(),
    'Fréquence relative (%)': df['passenger_seats'].value_counts(normalize=True) * 100,
    'Mode': df['passenger_seats'].mode()[0]
}


# Affichage des statistiques des variables catégorielles sélectionnées dans Streamlit
st.write("Statistiques descriptives des catégories :")
st.write(start_town_stats)
st.write(end_town_stats)
st.write(start_depart_stats)
st.write(end_depart_stats)
st.write(operator_stats)
st.write(passenger_seats_stats)

# Conversion des dates en format python dates
df['journey_start_date'] = pd.to_datetime(df['journey_start_date'])
df['journey_end_date'] = pd.to_datetime(df['journey_end_date'])
df['journey_start_time'] = pd.to_datetime(df['journey_end_date'])
df['journey_end_time'] = pd.to_datetime(df['journey_end_date'])
df['journey_start_datetime'] = pd.to_datetime(df['journey_end_date'])
df['journey_end_datetime'] = pd.to_datetime(df['journey_end_date'])

# Calcul les statistiques descriptives pour les dates
date_stats = {
    'Premier jour': df['journey_start_date'].min(),
    'Dernier jour': df['journey_start_date'].max(),
    'Nombre de jours': (df['journey_start_date'].max() - df['journey_start_date'].min()).days,
    'Nombre de valeurs uniques': df['journey_start_date'].nunique(),
    'Fréquence des dates': df['journey_start_date'].value_counts().sort_index()
}

# Affichage des statistiques descriptives dans Streamlit
st.write("Statistiques descriptives des dates :")
st.write(date_stats)

# Calculer et afficher les statistiques descriptives pour les données quantitatives
st.subheader("Statistiques descriptives des variables quantitatives")
st.write(df['journey_duration'].describe())
st.write(df['journey_distance'].describe())

# Tracés des boxplot des variables quantitatives
fig_duration = px.box(df, y="journey_duration", title="Boxplot avec valeurs extrêmes de la durée des trajets")
st.plotly_chart(fig_duration)
fig_distance = px.box(df, y="journey_distance", title="Boxplot avec valeurs extrêmes de la distance des trajets")
st.plotly_chart(fig_distance)







