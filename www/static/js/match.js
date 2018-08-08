$(document).ready(function(){    
    
    $.get("/team/" + id_team_west, function( data ) {        
        $('#logo-'+id_team_west).attr('src', "data:image/png;base64,"+ data.logo);
        $("#name-"+id_team_west).html(data.name);
    });

    $.get("/team/" + id_team_east, function( data ) {        
        $('#logo-'+id_team_east).attr('src', "data:image/png;base64,"+ data.logo);
        $("#name-"+id_team_east).html(data.name);
    });

    start_get_score();
});

var control_score;

function start_get_score(){
    control_score = setInterval(score, 1000);
}

function stop_get_score(){
    clearInterval(control_score);
    stop_chrono();    
}

function score(){
    $.get("/result/match/" + id_match, function( data ) {        
        $("#score-"+data[0].id_team).html(data[0].score);
        $("#score-"+data[1].id_team).html(data[1].score);
    });
}

$("#stop-match").click(function(){
    stop_get_score();
    $('#stop-match').css('display','none');
    $('#new-match').css('display','block');

    $.get("/match/stop/" + id_match, function(data){
        console.log(data);
    }).done(function() {
        score();
    });
});