var btnVerifica = document.querySelector('input#btnVer');
btnVerifica.addEventListener('click', adiconar_txt_from_back_end);

function adiconar_txt_from_back_end() {
    var res = document.querySelector('div#res');

    response = fetch('http://127.0.0.1:8000/hello')
        .then(response => response.json())
        .then(data => {
            jsonConvertido = JSON.stringify(data)
            res.innerHTML = `<p>${jsonConvertido}</p>`;
        })
        .catch(error => {
            console.error("Erro:", error);
        });
}; 