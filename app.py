from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
import streamlit as st

st.set_page_config(page_title="App Ethan" , page_icon="X")
st.title("ChatBot IA")
st.markdown("Agente para tus necesidades: ")
value = st.button("Delete")

if "msj" not in st.session_state:
    st.session_state.msj = []

if value:
    st.session_state.msj.clear()
    st.rerun()

for mesage in st.session_state.msj:

    if isinstance(mesage,SystemMessage):
        continue
    rol = "assistant" if isinstance(mesage,AIMessage) else "user"
    with st.chat_message(rol):
        st.markdown(mesage.content)

with st.sidebar:
    st.header("Configuracion")
    temp = st.slider("Temperatura",0.0,1.0)
    model = st.selectbox("Modelo",["gemini-2.5-flash","gemini-3-flash-preview","gemini-3-pro-preview"])


prom = st.chat_input("Promt here:")

if prom:
    MCP = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=temp)
    st.session_state.msj.append(HumanMessage(content=prom))

    with st.chat_message("user"):
        st.markdown(prom)
    response = MCP.invoke(st.session_state.msj)

    if response:
        st.session_state.msj.append(AIMessage(content=response.content))
        with st.chat_message("assistant"):
            st.markdown(response.content)



