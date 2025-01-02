import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header("Análisis de Vehículos Usados en Estados Unidos")

hist_button = st.button('Construir un histograma', key='unique_hist_button')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir un gráfico de dispersión', key='unique_scatter_button')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para "odometer" vs "price"')
    fig = px.scatter(car_data, x="odometer", y="price", title="Odómetro vs Precio")
    st.plotly_chart(fig, use_container_width=True)