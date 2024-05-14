// Fonction pour récupérer les données depuis l'API
    function getDataFromAPI() {
        // Utilisez fetch() ou une autre méthode pour faire l'appel à l'API
        fetch('http://localhost:81/getOrders')
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
        tableBody.innerHTML = '';
    
        data.forEach((item, index) => {
            let row = `<tr class="command-row" id="command-row-${index}">
                            <td>${item.orderNo}</td>
                            <td>${item.ClientName}</td>
                            <td>${item.Date}</td>
                            <td>${item.price}</td>
                        </tr>`;
            row += `<tr class="details-row d-none" id="details-row-${index}">
                        <td colspan="4">
                            <table class="table mb-0">
                                <thead>
                                    <tr>
                                        <th scope="col">Item Name</th>
                                        <th scope="col">Quantity</th>
                                        <th scope="col">Unit price</th>
                                        <th scope="col">Total line</th>
                                    </tr>
                                </thead>
                                <tbody>`;
            item.lines.forEach(line => {
                row += `<tr>
                            <td scope="row">${line.ProductName}</td>
                            <td>${line.Quantity}</td>
                            <td>${line.UnitPrice}</td>
                            <td>${line.TotalLinePrice}</td>
                        </tr>`;
            });
            row += `        </tbody>
                            </table>
                        </td>
                    </tr>`;
            tableBody.insertAdjacentHTML('beforeend', row);
        });
    
        data.forEach((item, index) => {
            document.getElementById(`command-row-${index}`).addEventListener('click', function() {
                const details = document.getElementById(`details-row-${index}`);
                // Utilise classList.toggle pour basculer la classe 'd-none'
                details.classList.toggle('d-none');
            });
        });
        
    }
    

    // Appel de la fonction pour récupérer les données dès que la page est chargée
    document.addEventListener('DOMContentLoaded', getDataFromAPI);
    
    
    
    
