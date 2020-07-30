$(document).ready(function () {
    $('#assemble').click(function () {
        $.ajax({
            url: "{{ url_for('assemble') }}",
            type: 'POST',
            data: { input: 'assemble' },
            success: function (data) {
                location.reload();
            }
        });
    });

});
$('tr').click(function () {
    //Check to see if background color is set or if it's set to white.
    if (this.style.background == "" || this.style.background == "white") {
        $(this).css('background', 'red');
    }
    else {
        $(this).css('background', 'white');
    }
});
$("#run").click(function () {
    var type = 'run'
    $.ajax({
        url: "{{ url_for('simulate') }}",
        type: 'POST',
        data: { input: type },
        success: function (data) {
            location.reload();
        }
    });
});
$("#step").click(function () {
    var type = 'step'
    $.ajax({
        url: "{{ url_for('simulate') }}",
        type: 'POST',
        data: { input: type },
        success: function (data) {
            location.reload();
            // refresh_register();
        }
    });

});
$("#prev").click(function () {
    var type = 'prev'
    $.ajax({
        url: "{{ url_for('simulate') }}",
        type: 'POST',
        data: { input: type }
    });
});
$("#reset").click(function () {
    var type = 'reset'
    $.ajax({
        url: "{{ url_for('simulate') }}",
        type: 'POST',
        data: { input: type },
        success: function (data) {
            location.reload();
            // refresh_register();
        }
    });
});
$("#dump").click(function () {
    var type = 'dump'
    $.ajax({
        url: "{{ url_for('simulate') }}",
        type: 'POST',
        data: { input: type }
    });
});
$("#trace").click(function () {
    var type = 'trace'
    $.ajax({
        url: "{{ url_for('simulate') }}",
        type: 'POST',
        data: { input: type }
    });
});
$("#hex").click(function () {
    var Display = 'hex'
    $.ajax({
        url: "{{ url_for('display') }}",
        type: 'POST',
        data: { input: Display },
        success: function (data) {
            location.reload();
        }
    });
});
$("#decimal").click(function () {
    var Display = 'decimal'
    $.ajax({
        url: "{{ url_for('display') }}",
        type: 'POST',
        data: { input: Display },
        success: function (data) {
            // alert(data);
            console.log('data'+data);
            // location.reload();
        }
    });
});
$("#ascii").click(function () {
    var Display = 'ascii'
    $.ajax({
        url: "{{ url_for('display') }}",
        type: 'POST',
        data: { input: Display },
        success: function (data) {
            location.reload();
        }
    });
});
$("#jump").click(function () {
    var Address = $('#jumpAddress').val()
    $.ajax({
        url: "{{ url_for('jump') }}",
        type: 'POST',
        data: { input: Address },
        success: function (data) {
            location.reload();
        }
    });
});
// function refresh_register() {
//     $.ajax({
//         url: "{{ url_for('refresh_register') }}",
//         type: 'POST',
//         data: { input: Address },
//         success: function (data) {
//             alert(data);
//         }
//     });
//     $('#register').html();

// }
