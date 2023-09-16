function app(){
    console.log("app iniciado!")
    carregandoAnimais()
    addAnimal()
}

async function carregandoAnimais() {
    const response = await axios.get("http://localhost:8000/animais")
    const animais = response.data
    const lista_animais = document.getElementById("lista_animais")

    lista_animais.innerHTML = '' //limpa a lista anterior

    // carrega a lista de animais
    animais.forEach(animal => {
        const item = document.createElement("li")
        item.innerText = animal.nome

        lista_animais.appendChild(item)
    }); 
}

function addAnimal() {
    const form_submit = document.getElementById("formulario_1")
    const animal_nome = document.getElementById("input_txt")

    form_submit.onsubmit = async (event) => {
        event.preventDefault() //Evita reload após submit
        const nome = animal_nome.value
        
        await axios.post("http://localhost:8000/animais", {
            nome: nome,
            idade: 2,
            sexo: "macho",
            cor: "verde"
        })
        carregandoAnimais()
    }
}

app()