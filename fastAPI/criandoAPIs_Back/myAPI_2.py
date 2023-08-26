from fastapi import FastAPI, HTTPException
from AnimalClass import *

#-----------------------------------------------
#CRIANDO OBJETOS -------------------------------
todas_corujas = {"Corujas": [
     Coruja(id_classe=0, altura=0.5, id_animal=0, raca='Coruja-das-neves', nome='Oliver'),
     Coruja(id_classe=0, altura=0.4, id_animal=1, raca='Coruja-buraqueira', nome='Luna'),
     Coruja(id_classe=0, altura=0.6, id_animal=2, raca='Coruja-de-orelhas', nome='Einstein'),
     Coruja(id_classe=0, altura=0.3, id_animal=3, raca='Coruja-do-mato', nome='Aurora')
]}
todos_cachorros = {"test": []}
todos_animais = [
    todas_corujas,
    todos_cachorros
]
#-----------------------------------------------
#CRIANDO API -----------------------------------
app = FastAPI()

#-----------------------------------------------
#Algumas funções para funcionamento desta API --
#Verificando existencia de animais COM LISTAS E DICIONÁRIOS
#Em caso de um banco de dados a consulta é diferente
def busca_animais(id: int):
    try:
        if todos_animais[id]:
            return todos_animais[id]
        else:
            return None
    except:
        return None

def busca_animal(id_classe: int, id_animal):
    if busca_animais(id_classe):
        # Verificando IndexError: list index out of range | id que não existe na matriz/array
        try:
            # pegando a chave do dicionário com a lista dos animais
            chave = list(busca_animais(id_classe).keys())[0]
            if busca_animais(id_classe)[chave][id_animal]:
                return busca_animais(id_classe)[chave][id_animal]
        except:
            return None
    else:
        return None

#CRIANDO GET PATH ------------------------------
#CRIANDO PARÂMETRO DE ROTA ---------------------
@app.get('/boas_vindas/{nome}') #/{nome} será usado como parâmetro da função
async def boas_vindas(nome: str):
    return {"mensagem": f"Bem vindo(a) {nome} ao meu primeiro APP! :)"}

# retorna uma lista com todas as classes dos animais cadastrados
@app.get('/animais')
async def animais():
    return todos_animais

# retorna uma lista de animais da classe de animal cadastrado
@app.get('/animais/{id_classe}')
async def animal_classe(id_classe: int):
    busca = busca_animais(id_classe)
    if busca == None:
        raise HTTPException(
            status_code=404,
            detail="Erro 404: Classe de Animal não encointrada"
        )
    else:
        return busca

# retorna o animal cadastrado
@app.get('/animais/{id_classe}/{id_animal}')
async def animal(id_classe: int, id_animal: int):
    busca = busca_animal(id_classe, id_animal)
    if busca == None:
        raise HTTPException(
            status_code=404,
            detail="Error 404: Animal não encontrado!"
        )
    else:
        return busca

#CRIANDO PARÂMETRO DE QUERY STRING -------------
@app.get('/p_queryString') # esses parâmetros ficam no final da rota após ? ..?parametro=valor
async def hello(text: str):
    texto = 'temos /p_queryString ... adiciona o valor assim -> /p_queryString?text=algumacoisa'
    # na URL os espaços são substituído por %20 /p_queryString?text=alguma%20coisa
    return {"mensagem": texto + '| você adicionou esse valor: ' + text}

# para mais de um parâmetro será usado o & ex:
@app.get('/calcular_soma') # /calcular_soma?numero_1=4.67&numero_2=7.89
async def soma(numero_1: float, numero_2: float):
    somando = numero_1 + numero_2
    return {"mensagem": f"Resultado da soma entre {numero_1} e {numero_2} é igaul a: {somando}"}

# ISSO TAMBÉM É POSSÍVEL 
@app.get('/calcular_soma/{numero_1}/{numero_2}') # /calcular_soma/3/6
async def soma(numero_1: float, numero_2: float):
    somando = numero_1 + numero_2
    return {"mensagem": f"Resultado da soma entre {numero_1} e {numero_2} é igaul a: {somando}"}

#CRIANDO POST PATH ------------------------------
@app.post("/") # cadastro uma nova coruja
async def nova_coruja(id_classe: Coruja):
    pass