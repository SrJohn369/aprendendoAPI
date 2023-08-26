from fastapi import FastAPI
from AnimalClass import *

#-----------------------------------------------
#CRIANDO OBJETOS -------------------------------
lista_corujas = [
     Coruja(id=1, nome='Einstein', raca='Coruja da neve', altura=0.56),
     Coruja(id=1, nome="Oliver", raca="Bubo", altura=0.5),
     Coruja(id=2, nome="Luna", raca="Tyto", altura=0.4),
     Coruja(id=3, nome="Hedwig", raca="Strix", altura=0.3),
     Coruja(id=4, nome="Hoot", raca="Asio", altura=0.6),
     Coruja(id=5, nome="Nocturne", raca="Athene", altura=0.35)
]
#-----------------------------------------------
#CRIANDO API -----------------------------------
app = FastAPI()

#CRIANDO GET PATH ------------------------------
#CRIANDO PARÂMETRO DE ROTA ---------------------
@app.get('/boas_vindas/{nome}') #/{nome} será usado como parâmetro da função
def boas_vindas(nome: str):
    return {"mensagem": f"Bem vindo(a) {nome} ao meu primeiro APP! :)"}

#CRIANDO PARÂMETRO DE QUERY STRING -------------
@app.get('/p_queryString') # esses parâmetros ficam no final da rota após ? ..?parametro=valor
def hello(text: str):
    texto = 'temos /p_queryString ... adiciona o valor assim -> /p_queryString?text=algumacoisa'
    # na URL os espaços são substituído por %20 /p_queryString?text=alguma%20coisa
    return {"mensagem": texto + '| você adicionou esse valor: ' + text}

# para mais de um parâmetro será usado o & ex:
@app.get('/calcular_soma') # /calcular_soma?numero_1=4.67&numero_2=7.89
def soma(numero_1: float, numero_2: float):
    somando = numero_1 + numero_2
    return {"mensagem": f"Resultado da soma entre {numero_1} e {numero_2} é igaul a: {somando}"}

