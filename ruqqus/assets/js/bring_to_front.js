// Enlarge thumbnail on post-img click

$(".post-actions a").click(function (event) {
    event.preventDefault();

    var id = $(this).parent().attr("id");

    document.getElementById(id).style.zIndex = "4";

});