import streamlit as st
import pandas as pd
import plotly_express as px

# Título de la aplicación
st.header('Análisis de Datos: Mercado de Videojuegos')

# Leer los datos
# Asegúrate de que el nombre del CSV coincida exactamente
df_games = pd.read_csv('games.csv') 

# Botón para el Histograma
if st.button('Construir histograma de ventas'):
    st.write('Distribución de las ventas globales')
    fig = px.histogram(df_games, x="total_sales")
    st.plotly_chart(fig, use_container_width=True)

# Botón para Gráfico de Dispersión
if st.button('Gráfico de Dispersión: Críticos vs Ventas'):
    st.write('Relación entre la puntuación de la crítica y las ventas')
    fig = px.scatter(df_games, x="critic_score", y="total_sales")
    st.plotly_chart(fig, use_container_width=True)