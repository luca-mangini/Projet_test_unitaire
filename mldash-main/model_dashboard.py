import streamlit as st 
import joblib

@st.cache
def load_model():
    return joblib.load('regression.joblib')


st.title('Prédiction de prix de maison')

taille = st.number_input("Taille maison")
nb_rooms = st.number_input("Nombre de chambre")
garden = st.number_input("Y a un jardin")

model = load_model()

if taille <= 0:
    st.write('mettre taille correcte')

if nb_rooms <= 0:
    st.write("mettre nombre de chambre correct")

if garden < 0:
    st.write("mettre nombre de jardin correct")

if taille > 0 and nb_rooms > 0 and garden >= 0:
        
    X = [[taille, nb_rooms, garden]]
    prediction = model.predict(X)
    ## afficher la prediction
    st.write("le prix de la maison est : {}". format(prediction[0]))
