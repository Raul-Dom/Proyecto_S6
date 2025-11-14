import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer el archivo CSV del conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal de la aplicación
st.header("Vehicle Sales Dashboard")

# Botón para mostrar un histograma del odómetro
hist_button = st.button("Show odometer histogram")

# Lógica que se ejecuta cuando el usuario hace clic en el botón
if hist_button:
    st.write("Creating a histogram for the vehicle dataset...")

    # Crear una figura de Plotly para el histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Título del gráfico
    fig.update_layout(title_text="Odometer Distribution")

    # Mostrar el gráfico en la app Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Botón para mostrar un scatter plot (odómetro vs precio)
scatter_button = st.button("Show scatter plot (odometer vs price)")

# Lógica cuando el usuario hace clic
if scatter_button:
    st.write("Creating a scatter plot for odometer vs price...")

    # Crear una figura de Plotly para scatter plot
    fig = go.Figure(
        data=[go.Scatter(
            x=car_data['odometer'],
            y=car_data['price'],
            mode='markers'
        )]
    )

    # Título del gráfico
    fig.update_layout(title_text="Odometer vs Price")

    # Mostrar el gráfico en la app Streamlit
    st.plotly_chart(fig, use_container_width=True)
