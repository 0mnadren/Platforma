function imeRadaPretraga(url) {
    const ime_rada_input = $('#ime_rada').val();
    const csrfToken = $( "input[name=\"csrfmiddlewaretoken\"]" ).val ( );

    $.ajax({
        url: url,
        type: 'post',
        data: {
            ime_rada: ime_rada_input,
            csrfmiddlewaretoken: csrfToken,
        },
        success: function(result, status, xhr) {
            $('#tbody_ime_rada').html(result);
        },
        error: function(xhr, status, error) {
            console.log(error);
        }
    });
}

function recenzijeDaniPretraga(url) {
    const broj_dana_input = $('#broj_dana').val();
    const csrfToken = $( "input[name=\"csrfmiddlewaretoken\"]" ).val ( );
    console.log(broj_dana_input)
    console.log(csrfToken)

    $.ajax({
        url: url,
        type: 'post',
        data: {
            broj_dana: broj_dana_input,
            csrfmiddlewaretoken: csrfToken,
        },
        success: function(result, status, xhr) {
            $('#div_broj_dana').html(result);
        },
        error: function(xhr, status, error) {
            console.log(error);
        }
    });
}

