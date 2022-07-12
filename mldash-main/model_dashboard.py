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

def verif_taille(taille_ok):
    if taille_ok <= 0:
        st.write('mettre taille correcte')
        result='pb'
    else:
        result='ok'
    return result

def verif_chambre(nb_rooms_ok):    
    if nb_rooms_ok <= 0:
        st.write("mettre nombre de chambre correct")
        result='pb'
    else:
        result='ok'
    return result

def verif_jardin(garden_ok):    
    if garden_ok < 0:
        st.write("mettre nombre de jardin correct")
        result='pb'
    else:
        result='ok'
    return result

def prediction(taille_ok,nb_room_ok,nb_garden_ok):
    if taille_ok > 0 and nb_room_ok > 0:
        
        X = [[taille_ok, nb_room_ok, nb_garden_ok]]
        prediction = model.predict(X)
        ## afficher la prediction
        st.write("le prix de la maison est : {}". format(prediction[0]))

verif_taille(taille)
verif_chambre(nb_rooms)
verif_jardin(garden)

prediction(taille,nb_rooms,garden)

def test_valeur_taille():
    assert verif_taille(-1) == "pb"
    assert verif_taille(10) == "ok"

def test_valeur_room():
    assert verif_chambre(-1) == "pb"
    assert verif_chambre(10) == "ok"

def test_valeur_jardin():
    assert verif_jardin(-1) == "pb"
    assert verif_jardin(10) == "ok"
