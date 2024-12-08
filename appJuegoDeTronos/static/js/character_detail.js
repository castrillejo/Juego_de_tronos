document.addEventListener("DOMContentLoaded", function () {
    const characterImageWrapper = document.getElementById("character-image-wrapper");
    const infoText = document.getElementById("info-text");
    const loadMoreButton = document.getElementById("check-alive-button");
    const aliveStatus = document.getElementById("alive-status");

    //Girar la imagen del personaje 
    if (characterImageWrapper) {
        characterImageWrapper.addEventListener("click", function () {
            characterImageWrapper.classList.toggle("rotated");

            if (infoText) {
                if (infoText.style.display === "none" || infoText.style.display === "") {
                    infoText.style.display = "flex";
                } else {
                    infoText.style.display = "none";
                }
            }
        });
    }

    //Está vivo o muerto
    if (loadMoreButton) {
        const characterId = loadMoreButton.getAttribute("data-character-id");

        loadMoreButton.addEventListener("click", function () {
            //Realizar solicitud AJAX con fetch
            fetch(`/api/character-info/${characterId}/`)
                .then((response) => {
                    if (!response.ok) {
                        throw new Error("Error en la respuesta de la solicitud");
                    }
                    return response.json();
                })
                .then((data) => {
                    //Actualizar el contenido del div con la información recibida
                    const status = data.is_alive ? "vivo" : "muerto";
                    aliveStatus.innerHTML = `Este personaje está <strong>${status}</strong> al final de la serie.`;
                    aliveStatus.style.display = "block";
                })
                .catch((error) => {
                    //Manejar errores y mostrar mensaje al usuario
                    aliveStatus.innerHTML = `<p>Error al cargar la información.</p>`;
                    aliveStatus.style.display = "block";
                    console.error("Error en la solicitud AJAX:", error);
                });
        });
    }
});
