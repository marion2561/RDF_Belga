// Fonction pour récupérer les données depuis l'API
function getDataFromAPI() {
    // Utilisez fetch() ou une autre méthode pour faire l'appel à l'API
    fetch('http://localhost:8000/api/plats')
        .then(response => response.json())
        .then(data => {
            // Convertir l'objet en tableau d'objets
            let dataArray = Object.values(data);
            // Une fois les données récupérées, appelez une fonction pour remplir le tableau
            fillTable(dataArray);
        })
        .catch(error => {
            console.error('Erreur lors de la récupération des données:', error);
        });
}
function fillTable(dataArray) {
    const tableBody = document.querySelector('#plats tbody');
    tableBody.innerHTML = ''; // Vide le contenu actuel du tableau
    // Parcours des données et création des lignes du tableau
    dataArray.forEach(item => {
        const row = `<tr>
                        <td>${item.nom_de_plat}</td>
                        <td>${item.description}</td>
                        <td>${item.categorie}</td>
                        <td>${item.prix}</td>
                        <td>${item.ingredients}</td>
                        <td>${item.allergenes}</td>
                        <td>${item.temps_de_preparation}</td>
                        <td>${item.temps_de_cuisson}</td>
                        <td>${item.disponibilite}</td>
                        <td>${item.popularite}</td>
                    </tr>`;
        tableBody.insertAdjacentHTML('beforeend', row);
    });
}
// Appel de la fonction pour récupérer les données dès que la page est chargée
document.addEventListener('DOMContentLoaded', getDataFromAPI);