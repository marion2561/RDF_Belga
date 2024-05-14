let beersData; // Variable pour stocker les données

// Fonction pour récupérer les données depuis l'API
function getDataFromAPI() {
    // Utilisez fetch() ou une autre méthode pour faire l'appel à l'API
    fetch('http://localhost:2711/beers')
    .then(response => response.json())
    .then(data => {
        beersData = data; // Stocke les données dans la variable
        fillCards(data);
        fillTypeSelect(data);
    })
    .catch(error => {
        console.error('Erreur lors de la récupération des données:', error);
    });
}
// Variables pour les filtres
let minAbv = 0;
let beerType = '';

// Fonction pour remplir les cartes avec les données récupérées
function fillCards(data) {
    const cardsContainer = document.querySelector('#bieres');
    cardsContainer.innerHTML = ''; // Vide le contenu actuel des cartes

    // Parcours des données et création des cartes
    data.forEach(item => {
        if (item.ABV >= minAbv && (beerType === '' || item.Type === beerType)) {
            const card = `<div class="col-12 col-md-6 col-lg-4 mb-4">
                            <div class="card h-100">
                                <img src="${item.Image_URL}" alt="${item.Name}" class="card-img-top" style="height: 200px; object-fit: contain;">
                                <div class="card-body">
                                    <h5 class="card-title">${item.Name}</h5>
                                    <h6 class="card-subtitle mb-2 text-muted">${item.Type}</h6>
                                    <h7 class="card-subtitle mb-2 text-muted">${item.Brewery}</h7><br><br>
                                    <h8 class="card-subtitle mb-2 text-muted">Alcool : ${item.ABV} %</h8>
                                    <hr>
                                    <p class="card-text">${item.Description}</p>
                                </div>
                            </div>
                          </div>`;
            cardsContainer.insertAdjacentHTML('beforeend', card);
        }
    });
}

function fillTypeSelect(data) {
    const typeSelect = document.querySelector('#typeSelect');
    const types = [...new Set(data.map(item => item.Type))]; // Crée un tableau des types uniques

    types.sort(); // Trie les types par ordre alphabétique

    types.forEach(type => {
        const option = document.createElement('option');
        option.value = type;
        option.textContent = type;
        typeSelect.appendChild(option);
    });
}

// Écouteur d'événements pour le slider
document.querySelector('#abvSlider').addEventListener('input', event => {
    minAbv = event.target.value;
    document.querySelector('#abvSliderValue').textContent = minAbv;
    fillCards(beersData); // Utilise les données stockées au lieu de faire un nouvel appel API
});

// Écouteur d'événements pour la liste déroulante
document.querySelector('#typeSelect').addEventListener('change', event => {
    beerType = event.target.value;
    fillCards(beersData); // Utilise les données stockées au lieu de faire un nouvel appel API
});

// Écouteur d'événements pour la barre de recherche
document.querySelector('#searchBar').addEventListener('input', searchBeer);

// Fonction pour rechercher une bière par nom
function searchBeer(event) {
    const searchTerm = event.target.value.toLowerCase();
    const filteredBeers = beersData.filter(beer => beer.Name.toLowerCase().includes(searchTerm));
    fillCards(filteredBeers);
}

// Récupère les données initiales
getDataFromAPI();