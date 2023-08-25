import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components
import streamlit as st

st.set_page_config(
    page_title="Dashboard interactivo",
    layout="wide"
)

st.title("Usar Pygwalker en Streamlit")

df = pd.read_csv("src/bike_sharing_dc.csv")
 
pyg_html = pyg.walk(df, return_html=True)
 
components.html(pyg_html, height=1000, scrolling=True)