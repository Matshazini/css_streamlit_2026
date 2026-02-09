# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 22:52:54 2026

@author: Zukisa Matshazini
"""

import streamlit as st


st.title("Jungle of Big Five ")

menu = st.radio("Welcome to us", ["About Us","Contact Us","Write Feedback to Us"])
if menu == "About Us":
    st.title("About Us:")
    st.header("This app assist the tourists to be able to do online bokking. It also allows them to be able to check the available wild animals")
    
    Forest = "Kruga National Park"
    City = "Pretoria"
    Provice ="Gauteng"
    Country = "South Africa"
    
    st.write(f"**Forest:** {Forest}")
    st.write(f"**City:** {City}")
    st.write(f"**Provice:** {Provice}")
    st.write(f"**Country:** {Country}")
    menu = st.page_link("https://www.google.com/search?client=firefox-b-d&hs=DIz9&sca_esv=896419ed210a4547&udm=2&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3vWUtYx0DZdicpfE1faGYenqWn-q4MFiFFtvJjTKeAVxS4PPKl3W41Y-d9O9355Lz3Xya85A9mlj2M1wlia6-Mw1PlcqfTox6-pDMMGayYtTmoITIwmHBkKIZ-77eesjMk-WyUn6NdMpbielekCqEbKuIKAv02SvLe9qvugXyfsLqTRwwA&q=jungle&sa=X&ved=2ahUKEwjcusaO48ySAxVNWkEAHRBeJe0QtKgLegQIExAB&biw=1274&bih=635&dpr=1#sv=CAMSWBoyKhBlLTZWQVE5U0xtOEJNcVVNMg42VkFROVNMbThCTXFVTToOQWdzZTdERzFmQlZRUk0gBCocCgZtb3NhaWMSEGUtNlZBUTlTTG04Qk1xVU0YADABOAAYByCCrqPDBjACSggQAhgCIAIoAg", label="Click to View animals and our environment", icon="🏠") 
    

elif menu == "Contact Us":
    st.title("Contact Us:")
    st.header("Zukisa Matshazini")
    menu = st.page_link("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&dsh=S-1824673242%3A1770659224702825&ifkv=AXbMIuCArNr9ydFwdt4jFmV-cZLmJqR6dL48IaCvtAhwMm3uhTjOmOXrc4r0c5MQ1FgHNekYEnN3&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin", label="Email address", icon="📧")
    email = "Zukisa.Matshazini@gmail.com"
    st.write(f"  Or email me at: {email}")
    menu = st.page_link("https://www.linkedin.com/in/zukisa-matshazini-9896797a/", label="LinkedIn", icon="🔗")
    menu = st.page_link("https://www.google.com/maps/place/Union+Buildings/@-25.7402069,28.2094159,17z/data=!3m1!4b1!4m6!3m5!1s0x1e9561f7541b3737:0x15bc1a7319252305!8m2!3d-25.7402069!4d28.2119908!16zL20vMDJkNWJk?entry=ttu&g_ep=EgoyMDI2MDIwNC4wIKXMDSoASAFQAw%3D%3D", label="Location", icon="📍")
    st.write("**About him:** Zukisa Matshazini, currently is working for an IT Company at App Development and Maintenance. He previous worked form the Department of Health. He obtained Advanced Diploma and ND: IT.")

elif menu == "Write Feedback to Us":
    st.title("Write Feedback to Us")
    name = st.text_input("**Full Name:** ")
    number = st.text_input("**Contact Number:** ")
    email = st.text_input("**Email Address:** ")
    response = st.text_area("**Specify purpose of communication:** ")    
    submit = st.button("Submit")
    st.write(f"Thank you very much for contacting us, you will get a response soon : {name}!")

    
