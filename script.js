document.getElementById("search").addEventListener("keyup", function() {
    let value = this.value.toLowerCase();
    let cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        let name = card.innerText.toLowerCase();
        card.style.display = name.includes(value) ? "block" : "none";
    });
});

function showPreview(name, image) {
    document.getElementById("previewTitle").innerText = name;
    document.getElementById("previewImage").src = "/static/emotes/" + image;
    document.getElementById("previewModal").style.display = "block";
}

function closePreview() {
    document.getElementById("previewModal").style.display = "none";
}