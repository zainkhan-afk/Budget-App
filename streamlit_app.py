import streamlit as st
from helper_functions import tap_populator
import data

st.set_page_config(
    page_title="App",
    layout="wide",
    initial_sidebar_state="expanded")

st.markdown("### App")

with st.sidebar:
    st.markdown("### Sidebar")


tabs = st.tabs(list(data.data.keys()))

i = 0
for tab in tabs:
    tap_populator(tab, list(data.data.keys())[i])
    i += 1