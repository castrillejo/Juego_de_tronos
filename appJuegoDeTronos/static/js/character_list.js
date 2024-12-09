document.addEventListener("DOMContentLoaded", function ()
 {
    const searchBar = document.getElementById("search-bar");
    const characterItems = document.querySelectorAll(".character-item");
    const favoriteList = document.getElementById("favorite-list");

    //Cargar favoritos desde localStorage
    const loadFavorites = () =>
        {
        const favorites = JSON.parse(localStorage.getItem("favorites")) || [];
        favoriteList.innerHTML = "";

        favorites.forEach(fav => 
        {
            const listItem = document.createElement("li");
            const link = document.createElement("a");
            link.textContent = fav.name;
            link.href = `/characters/${fav.id}/`;
            link.classList.add("favorite-link");
            listItem.appendChild(link);
            favoriteList.appendChild(listItem);
        });

        //Estrellas en la lista de personajes
        characterItems.forEach(item => 
            {
            const characterId = item.dataset.characterId;
            const star = item.querySelector(".favorite-star");
            const isFavorite = favorites.some(fav => fav.id === characterId);

            if (isFavorite) 
            {
                star.textContent = "★";
                star.classList.add("favorite");
            } else 
            {
                star.textContent = "☆";
                star.classList.remove("favorite");
            }
        });
    };

    //Guardar o eliminar favoritos en localStorage
    const toggleFavorite = (id, name) => 
        {
        let favorites = JSON.parse(localStorage.getItem("favorites")) || [];
        const favoriteIndex = favorites.findIndex(fav => fav.id === id);

        if (favoriteIndex > -1) 
        {
            favorites.splice(favoriteIndex, 1);
        } else {
            favorites.push({ id, name });
        }

        localStorage.setItem("favorites", JSON.stringify(favorites));
        loadFavorites(); 
    };

    //Eventos de búsqueda
    searchBar.addEventListener("input", function () 
    {
        const query = searchBar.value.toLowerCase();
        characterItems.forEach(item => 
        {
            const characterName = item.dataset.characterName.toLowerCase();
            if (characterName.includes(query)) 
            {
                item.style.display = "flex";
            } else 
            {
                item.style.display = "none";
            }
        });
    });

    //Marcar/Desmarcar como Favorito
    characterItems.forEach(item => 
        {
        const favoriteStar = item.querySelector(".favorite-star");
        const characterId = item.dataset.characterId;
        const characterName = item.querySelector(".character-name").textContent.trim();

        favoriteStar.addEventListener("click", function () 
        {
            toggleFavorite(characterId, characterName);
        });
    });

    //Cargar los favoritos al iniciar
    loadFavorites();
});
