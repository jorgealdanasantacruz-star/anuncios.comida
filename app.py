{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww35640\viewh20780\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
from crewai import Agent, Task, Crew\
\
# Configura tu API key (se toma de secrets en Streamlit)\
import os\
os.environ["ANTHROPIC_API_KEY"] = st.secrets.get("ANTHROPIC_API_KEY", "")\
\
st.title("Creador de Anuncios Publicitarios de Comida")\
\
# Agent 1: Investigador\
investigador = Agent(\
    role='Investigador de Tendencias',\
    goal='Analizar anuncios exitosos en Instagram y TikTok',\
    backstory='Eres experto en marketing digital y redes sociales.',\
    verbose=True,\
    allow_delegation=False\
)\
\
# Agent 2: Director Creativo\
director = Agent(\
    role='Director Creativo',\
    goal='Crear conceptos creativos y copies para anuncios',\
    backstory='Eres un creativo publicitario con experiencia en comida.',\
    verbose=True\
)\
\
# Tareas\
task1 = Task(\
    description='Investiga anuncios exitosos de comida en redes para el tema: \{query\}',\
    agent=investigador\
)\
\
task2 = Task(\
    description='Crea 5 conceptos creativos y copies para anuncios',\
    agent=director\
)\
\
# Crew\
crew = Crew(\
    agents=[investigador, director],\
    tasks=[task1, task2],\
    verbose=2\
)\
\
# Interfaz de Streamlit\
query = st.text_input("Ingresa el tema o idea de comida (ej. salchipapas cargadas):")\
if st.button("Generar Anuncios"):\
    if query:\
        with st.spinner("Ejecutando CrewAI..."):\
            result = crew.kickoff(inputs=\{"query": query\})\
        st.success("\'a1Listo!")\
        st.write(result)\
    else:\
        st.warning("Escribe un tema primero.")}