// Bouton permettant d'appeler la fonction pour récupérer les données depuis l'API
var button = document.getElementById("BtnData");
button.addEventListener("click", getDataFromAPI);
// Fonction pour récupérer les données depuis l'API
function getDataFromAPI() {
    // Utilisez fetch() ou une autre méthode pour faire l'appel à l'API
    fetch('http://localhost:5000/beer_services/beers?min_abv=8')
    .then(response => response.json())
    .then(data => {
        // Une fois les données récupérées, appelez une fonction pour remplir le tableau
        fillTable(data);
    })
    .catch(error => {
        console.error('Erreur lors de la récupération des données:', error);
    });
}
// Fonction pour remplir le tableau avec les données récupérées
function fillTable(data) {
    const tableBody = document.querySelector('#bieres tbody');
    tableBody.innerHTML = ''; // Vide le contenu actuel du tableau
    // Parcours des données et création des lignes du tableau
    data.forEach(item => {
        const row = `<tr>
                        <td>${item.Name}</td>
                        <td>${item.Type}</td>
                        <td>${item.ABV}</td>
                        <td>${item.IBU}</td>
                        <td>${item.Brewery}</td>
                        <td>${item.Description}</td>
                    </tr>`;
        tableBody.insertAdjacentHTML('beforeend', row);
    });
}

// Appel de la fonction pour récupérer les données dès que la page est chargée
document.addEventListener('DOMContentLoaded', getDataFromAPI);