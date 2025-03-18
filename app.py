import streamlit as st
import random

# Diccionario de elementos químicos
ELEMENTOS = {
    "H": "Hidrógeno",
    "He": "Helio",
    "Li": "Litio",
    "Be": "Berilio",
    "B": "Boro",
    "C": "Carbono",
    "N": "Nitrógeno",
    "O": "Oxígeno",
    "F": "Flúor",
    "Ne": "Neón",
}

# Función para seleccionar un elemento aleatorio
def obtener_elemento():
    return random.choice(list(ELEMENTOS.items()))

st.title("Juego de Elementos Químicos")

if "elemento_actual" not in st.session_state:
    st.session_state.elemento_actual = obtener_elemento()

simbolo, nombre_correcto = st.session_state.elemento_actual
st.write(f"**Símbolo químico:** {simbolo}")

respuesta_usuario = st.text_input("Ingresa el nombre del elemento:")

if st.button("Verificar"):
    if respuesta_usuario.strip().lower() == nombre_correcto.lower():
        st.success("¡Correcto!")
        st.session_state.elemento_actual = obtener_elemento()
    else:
        st.error(f"Incorrecto. La respuesta correcta es {nombre_correcto}.")
        
if st.button("Siguiente Elemento"):
    st.session_state.elemento_actual = obtener_elemento()
    st.experimental_rerun()
