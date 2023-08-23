var btn = document.getElementById("test")
var form = document.getElementById("form_id")
var btn_sub = document.getElementById("btn_sub")

btn.document.addEventListener("click", () => {
    fetch("/hello")
        .then(response => response.json())
        .then(data => {
            document.getElementById("message").textContent = data.message;
        });
});


btn_sub.document.addEventListener("click", async (event) => {
    event.preventDefaul();

    const formData = new FormData(form);
    const resposta = fetch("/cadastro", {
        method: "POST",
        body: formData
    });
})