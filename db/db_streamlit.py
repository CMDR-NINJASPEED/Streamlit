import streamlit as st
import sqlite3

#Creamos el menú lateral
st.sidebar.title("Gestor de usuarios")
opcion = st.sidebar.selectbox("Selecciona una opción", ["Ver usuarios","Agregar","Actualizar","Eliminar"])
# Creamos lista de usuario
match opcion:
    case "Ver usuarios":
        st.text("test")
    case "Agregar":
        st.text("Por favor, inserte los datos a crear")
        usuario=st.text_input("Nombre:")
        email=st.text_input("email")
        st.button("Agregar")
        if st.button("Agregar"):
            try:
                # Conectar a la base de datos (crea el archivo si no existe)
                conn = sqlite3.connect('usuarios.db')
                cursor = conn.cursor()

                # Crear tabla si no existe, uso únique en TEXT como restricción para que no se repita el email
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    email TEXT UNIQUE 
                )
                ''')

                # Confirmar los cambios
                conn.commit()
                print("Base de datos y tabla creadas correctamente.")
            
            cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (usuario, email))

            except Exception as e:
                print(f" Error al crear la base de datos o la tabla: {e}")

            finally:
            # Si conn es true entonces cierra
                if conn:
                    conn.close()

    case "Actualizar":
        st.text("test")
    case "Eliminar":
        st.text("test")