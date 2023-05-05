$(document).ready(function(){
    setInterval(function(){
        $.ajax({
            url: '/jeu_data/',
            type: 'GET',
            success: function(response){
                $('#population').text(response.population);
                $('#air_quality').text(response.air_quality);
                $('#water_quality').text(response.water_quality);
                $('#soil_quality').text(response.soil_quality);
                $('#waste_production').text(response.waste_production);
                $('#food_production').text(response.food_production);
                $('#energy_consumption').text(response.energy_consumption);
                $('#budget').text(response.budget);
            }
        });
    }, 1000);
});
