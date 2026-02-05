# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 22:52:54 2026

@author: Zukisa Matshazini
"""

import streamlit as st

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")
