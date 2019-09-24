// Show confirm password field when user clicks email box

$('#new_email').on('input', function () {

    var id = document.getElementById("password");
    var id2 = document.getElementById("email-password-label");
    var id3 = document.getElementById("passwordRequired");

    id.classList.remove("d-none");
    id2.classList.remove("d-none");
    id3.classList.remove("d-none");

});