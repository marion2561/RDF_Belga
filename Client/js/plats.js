// Fonction pour récupérer les données depuis l'API
function getDataFromAPI() {
    // Utilisez fetch() ou une autre méthode pour faire l'appel à l'API
    fetch('http://localhost:81/plats')
        .then(response => response.json())
        .then(data => {
            // Convertir l'objet en tableau d'objets
            let dataArray = Object.values(data);
            // Une fois les données récupérées, appelez une fonction pour remplir le tableau
            fillCards(dataArray);
        })
        .catch(error => {
            console.error('Erreur lors de la récupération des données:', error);
        });
}

 // Fonction pour ouvrir la modal
function openModal(dishName) {
var myModal = new bootstrap.Modal(document.getElementById('exampleModal'));
var modalBodyContent = document.getElementById('modalBodyContent');

// Vider le contenu précédent et afficher le GIF de chargement
modalBodyContent.innerHTML = `
    <div class="loading-spinner">
    <img src="https://i.gifer.com/ZZ5H.gif" alt="Loading...">
    </div>
`;

// Ouvrir la modal
myModal.show();

// Faire l'appel API
fetch('http://localhost:81/bestBeers/' + dishName)
    .then(response => response.json())
    .then(data => {
    // Vider le contenu précédent
    modalBodyContent.innerHTML = '';

    // Créer une rangée pour les bières
    var row = document.createElement('div');
    row.className = 'row';

    // Parcourir les données et remplir la modal
    data.forEach(beer => {
        var col = document.createElement('div');
        col.className = 'col-md-4 mb-3'; // Utilisation des colonnes pour la grille Bootstrap

        col.innerHTML = `
        <div class="card h-100">
            <div class="beer-img-container">
            <img src="${beer.Image_URL}" class="beer-img" alt="${beer.Name}">
            </div>
            <div class="card-body">
            <h5 class="card-title">${beer.Name}</h5>
            <h6 class="card-subtitle mb-2 text-muted"><strong>Brasserie:</strong> ${beer.Type}</h6>
            <h7 class="card-subtitle mb-2 text-muted">${beer.Brewery}</h7><br><br>
            <h8 class="card-subtitle mb-2 text-muted">Alcool : ${beer.ABV} %</h8>
            <hr>
            <p class="card-text"><strong>Description:</strong> ${beer.Description}</p>
            <p class="card-text"><strong>Explication du choix:</strong> ${beer.Explanation}</p>
            </div>
        </div>
        `;
        row.appendChild(col);
    });

    modalBodyContent.appendChild(row);
    })
    .catch(error => {
    console.error('Erreur lors de la récupération des données:', error);
    modalBodyContent.innerHTML = '<p class="text-danger">Erreur lors de la récupération des données.</p>';
    });
}



function fillCards(dataArray) {
    const cardsContainer = document.querySelector('#plats');
    cardsContainer.innerHTML = ''; // Vide le contenu actuel des cartes

    // Parcours des données et création des cartes
    dataArray.forEach(item => {
            const card = `<div class="col-12 col-md-6 col-lg-4 mb-4" onclick="openModal('${item.nom_de_plat}')">
                            <div class="card h-100">
                                <img src="${item.image_url}" alt="${item.nom_de_plat}" class="card-img-top" style="height: 200px; object-fit: contain;">
                                </a>
                                <div class="card-body">
                                    <h5 class="card-title">${item.nom_de_plat}</h5>
                                    <h6 class="card-subtitle mb-2 text-muted">${item.prix} CHF</h6>
                                    <h7 class="card-subtitle mb-2 text-muted">Ingrédients : <br>${item.ingredients} </h7><br><br>
                                    <h8 class="card-subtitle mb-2 text-muted">Popularité : ${item.popularite} </h8>
                                    <hr>
                                    <p class="card-text">${item.description}</p>
                                </div>
                            </div>
                          </div>`;
            cardsContainer.insertAdjacentHTML('beforeend', card);
}
)}  ;
document.getElementById
// Appel de la fonction pour récupérer les données
getDataFromAPI();
