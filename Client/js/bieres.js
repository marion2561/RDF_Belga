// Bouton permettant d'appeler la fonction pour récupérer les données depuis l'API

// Fonction pour récupérer les données depuis l'API
function getDataFromAPI() {
    // Utilisez fetch() ou une autre méthode pour faire l'appel à l'API
    fetch('http://localhost:2711/beers')
    .then(response => response.json())
    .then(data => {
        // Une fois les données récupérées, appelez une fonction pour remplir le tableau
        fillCards(data);
    })
    .catch(error => {
        console.error('Erreur lors de la récupération des données:', error);
    });
}
// Fonction pour remplir les cartes avec les données récupérées
function fillCards(data) {
    const cardsContainer = document.querySelector('#bieres');
    cardsContainer.innerHTML = ''; // Vide le contenu actuel des cartes

    // Parcours des données et création des cartes
    data.forEach(item => {
        const card = `<div class="col-12 col-md-6 col-lg-4 mb-4">
                        <div class="card h-100">
                            <img src="${item.Image_URL}" alt="${item.Name}" class="card-img-top" style="height: 200px; object-fit: cover;">
                            <div class="card-body">
                                <h5 class="card-title">${item.Name}</h5>
                                <h6 class="card-subtitle mb-2 text-muted">${item.Type}</h6>
                                <p class="card-text">${item.Description}</p>
                                <p class="card-text">ABV: ${item.ABV}</p>
                                <p class="card-text">IBU: ${item.IBU}</p>
                                <p class="card-text">Brewery: ${item.Brewery}</p>
                            </div>
                        </div>
                      </div>`;
        cardsContainer.insertAdjacentHTML('beforeend', card);
    });
}

// Appellez la fonction generateCardsFromCSV lorsque la page est chargée
//window.onload = getDataFromAPI;
// Appel de la fonction pour récupérer les données dès que la page est chargée
document.addEventListener('DOMContentLoaded', getDataFromAPI);