$(document).ready(function () {
    var socket = io.connect('http://localhost:' + location.port + '/test');
    socket.on('my connection', function (msg) {
        $('#log').append('<p>Status: ' + msg.data + '</p>');
    });
    socket.on('new message', function (msg) {
        $('#log').append('<p>Received: ' + msg.data + '</p>');
    });
    $('form#message').submit(function (event) {
        socket.emit('my new message', { data: $('#message_data').val() });
        document.getElementById("message").reset();
        return false;
    });
});