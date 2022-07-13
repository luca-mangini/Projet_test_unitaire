import streamlit as st 
import joblib

def load_model():
    return joblib.load('regression.joblib')

model = load_model()

def verif_taille(taille_ok):
    if taille_ok <= 0:
        result='pb'
    else:
        result='ok'
    return result

def verif_chambre(nb_rooms_ok):    
    if nb_rooms_ok <= 0:
        result='pb'
    else:
        result='ok'
    return result

def verif_jardin(garden_ok):    
    if garden_ok < 0:
        result='pb'
    else:
        result='ok'
    return result

def prediction(taille_ok,nb_room_ok,nb_garden_ok):
    if taille_ok > 0 and nb_room_ok > 0:
        
        X = [[taille_ok, nb_room_ok, nb_garden_ok]]
        prediction = model.predict(X)

def test_valeur_taille():
    assert verif_taille(-1) == "pb"
    assert verif_taille(10) == "ok"

def test_valeur_room():
    assert verif_chambre(-1) == "pb"
    assert verif_chambre(10) == "ok"

def test_valeur_jardin():
    assert verif_jardin(-1) == "pb"
    assert verif_jardin(10) == "ok"
