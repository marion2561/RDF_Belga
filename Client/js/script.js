$(document).ready(function() {
  $.ajax({
      url: 'http://127.0.0.1:5000/beer_services/beers?min_abv=8',
      dataType: 'json',
      useragent: 'Mozilla/5.0',
      method: 'GET',
      success: function(data) {
          var rows = '';
          data.forEach(function(item) {
              rows += '<tr>' +
                      '<td>' + item.Name + '</td>' +
                      '<td>' + item.Type + '</td>' +
                      '<td>' + item.ABV + '</td>' +
                      '<td>' + item.IBU + '</td>' +
                      '<td>' + item.Brewery + '</td>' +
                      '<td>' + item.Description + '</td>' +
                      '</tr>';
          });
          $('#bieres tbody').html(rows);
      },
      error: function(error) {
          console.error('Erreur lors du chargement des données:', error);
      }
  });
});