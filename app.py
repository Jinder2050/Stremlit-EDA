import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components
import streamlit as st

st.set_page_config(
    page_title="Dashboard interactivo",
    layout="wide"
)

st.title("EDA en Streamlit")

file = st.file_uploader(label='Cargar un archivo CSV', accept_multiple_files=False, type=["csv"])
if file is not None:
    try:
        df = pd.read_csv(file)
        st.success('Archivo csv cargado correctamente...', icon="✅")
    except Exception as e:
        st.error(f"Error al cargar el archivo: {str(e)}")
else:
    st.info('Carga un archivo csv para empezar.')


if 'df' in locals():
    with st.spinner("Abriendo pygwalker..."):
        try:
            pyg_html = pyg.walk(df, return_html=True)
            components.html(pyg_html, height=1000, scrolling=True)
        except Exception as e:
            st.error(f"Error al realizar el análisis exploratorio de datos: {str(e)}")


