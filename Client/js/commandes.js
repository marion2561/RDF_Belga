// Fonction pour récupérer les données depuis l'API
    function getDataFromAPI() {
        console.log("ok");
        // Utilisez fetch() ou une autre méthode pour faire l'appel à l'API
        fetch('http://http://localhost:85/getOrders')
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
        const tableBody = document.querySelector('#commandes tbody');
        tableBody.innerHTML = ''; // Vide le contenu actuel du tableau
        // Parcours des données et création des lignes du tableau
        data.forEach(item => {
            const row = `<tr>
                        <td>${item.orderNo}</td>
                        <td>${item.ClientName}</td>
                        <td>${item.Date}</td>
                        <td>${item.price}</td>
                    </tr>`;
            tableBody.insertAdjacentHTML('beforeend', row)
        });
    }

    // Appel de la fonction pour récupérer les données dès que la page est chargée
    document.addEventListener('DOMContentLoaded', getDataFromAPI);
