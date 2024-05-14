// Fonction pour récupérer les données depuis l'API
function getDataFromAPI() {
    // Utilisez fetch() ou une autre méthode pour faire l'appel à l'API
    fetch('http://localhost:8000/api/plats')
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
function fillCards(dataArray) {
    const cardsContainer = document.querySelector('#plats');
    cardsContainer.innerHTML = ''; // Vide le contenu actuel des cartes

    // Parcours des données et création des cartes
    dataArray.forEach(item => {
            const card = `<div class="col-12 col-md-6 col-lg-4 mb-4">
                            <div class="card h-100">
                                <img src="${item.image_url}" alt="${item.nom_de_plat}" class="card-img-top" style="height: 200px; object-fit: contain;">
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
    });
}
// Appel de la fonction pour récupérer les données
getDataFromAPI();