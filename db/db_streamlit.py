import streamlit as st
import sqlite3

#Creamos el menú lateral
st.sidebar.title("Gestor de usuarios")
opcion = st.sidebar.selectbox("Selecciona una opción", ["Ver usuarios:","Agregar","Actualizar","Eliminar"])
# Creamos lista de usuario
match opcion:
    case "Ver usuarios":

    case "Agregar":
        st.text("Por favor, inserte los datos a crear")
        st.text_input("Nombre:")
        st.text_input("email")
        st.input()
    
    case "Actualizar":

    case "Eliminar":