from fastapi import FastAPI
from AnimalClass import *
#-----------------------------------------------
#CRIANDO OBJETOS -------------------------------
corujinha = Coruja(id=1, nome='Einstein', raca='Coruja da neve', altura=57.6)
#-----------------------------------------------
#CRIANDO API -----------------------------------
app = FastAPI()

