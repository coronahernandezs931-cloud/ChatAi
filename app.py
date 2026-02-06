# Estas son las carpetas que utilize para este proyecto 
from langchain_google_genai import ChatGoogleGenerativeAI
# Es el framework de langchain para falicitar el uso de la IA en proyectos
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
# Estas clases son para separar los mensajes de los usuarios,IA y del sistema osea parte de los
# que se le dan a la IA pero en este caso no fue usado
import streamlit as st
# La libreria de Streamlit es un Framework de desarrollo web muy facil de usar por su facilidad 
# la seleccione para el proyecto


st.set_page_config(page_title="App Ethan" , page_icon="X")
st.title("ChatBot IA")
st.markdown("Agente para tus necesidades: ")
# Botton para reiniciar el chat
value = st.button("Delete")

# Si aun no esta creada la lista msj la creo
if "msj" not in st.session_state:
    # session_state es para guardar datos por que todo se elimina al hacer un cambio en la app
    # se vuelve a ejecutar todo el codigo cada que hay un cambio y solo lo que esta en session_state prebalese
    st.session_state.msj = []

if value:
    # Si el boton de delete se presiona session_state es reiniciado y baciado
    st.session_state.msj.clear()
    # Rerun permite que se vuelva a cargar la pagina
    st.rerun()


for mesage in st.session_state.msj:

    if isinstance(mesage,SystemMessage):
        continue
    # Aqui en una variable guardo de quien es cada mensaje
    rol = "assistant" if isinstance(mesage,AIMessage) else "user"
    # Muestro en pantalla cada uno de los mensajes en pantalla sacados desde la "base de datos" de session_state
    with st.chat_message(rol):
        st.markdown(mesage.content)
# Sidebar sirve para la ventana que esta orientada del lado derecho que es nuestra configuracion
with st.sidebar:
    st.header("Configuracion")
    temp = st.slider("Temperatura",0.0,1.0)
    model = st.selectbox("Modelo",["gemini-2.5-flash","gemini-3-flash-preview","gemini-3-pro-preview"])

# Aqui solo pido que ingrese el promt
prom = st.chat_input("Promt here:")
# La app no hace nada si un promt no exite
if prom:
    # Instancio la clase de coneccion con la IA
    MCP = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=temp)
    # Guando el promt que mando el usuario
    st.session_state.msj.append(HumanMessage(content=prom))
    # Muestro en pantalla el promt del usuario
    with st.chat_message("user"):
        st.markdown(prom)
    # Le mando el historial de conversasiones para que tenga contexto de lo que se esta ablando
    response = MCP.invoke(st.session_state.msj)
    # Si existe una respuesta guardo en session_state la respuesta de la IA y la mando a pantalla
    if response:
        st.session_state.msj.append(AIMessage(content=response.content))
        with st.chat_message("assistant"):
            st.markdown(response.content)


# Gracias por ver este proyecto!
