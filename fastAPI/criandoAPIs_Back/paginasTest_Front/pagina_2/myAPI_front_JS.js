document.addEventListener("DOMContentLoaded", () => {
    fetch("/hello")
        .then(response => response.json())
        .then(data => {
            document.getElementById("message").textContent = data.message;
        });
});
