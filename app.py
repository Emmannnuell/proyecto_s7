import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Dashboard de Análisis de Vehículos")
st.subheader("Proyecto Sprint 7")


car_data = pd.read_csv('datasets/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
disp_button = st.button('Construir un gráfica de dispersión') # crear un botón
     
if hist_button: # al hacer clic en el botón
     # mensaje
     st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
     # crear un histograma
     fig = px.histogram(car_data, x="odometer")
     # mostrar un gráfico Plotly interactivo
     st.plotly_chart(fig, use_container_width=True)


if disp_button:
    # mensaje
    st.write('Creacion de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')
    #Creación de gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
     