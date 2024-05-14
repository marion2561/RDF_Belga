document.addEventListener('DOMContentLoaded', function() {
    const spinner = document.getElementById('spinner');
    const beerInfo = document.getElementById('beer-info');
    const maxRetries = 5; // Nombre maximum de tentatives
    const retryDelay = 2000; // Délai entre les tentatives en millisecondes

    function fetchData(retries) {
        fetch('http://localhost:81/menu')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                document.getElementById('beer-image').src = data.Image_URL;
                document.getElementById('beer-description').textContent = data.Description;
                document.getElementById('menu-name').textContent = data.Name + " - " + data.MealName;
                document.getElementById('beer-explanation').textContent = data.Explanation;
                
                // Cacher le spinner et afficher les informations
                spinner.classList.add('hidden');
                beerInfo.classList.remove('hidden');
            })
            .catch(error => {
                console.error('Erreur:', error);
                if (retries > 0) {
                    setTimeout(() => fetchData(retries - 1), retryDelay);
                } else {
                    spinner.textContent = 'Erreur de chargement des données. Veuillez réessayer plus tard.';
                }
            });
    }

    // Initial fetch with retries
    fetchData(maxRetries);
});

