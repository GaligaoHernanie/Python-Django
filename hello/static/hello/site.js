function toggleDropdown(event) {
    var dropdowns = document.getElementsByClassName('dropdown');
    var homeLink = document.getElementById('home-link');

    for (var i = 0; i < dropdowns.length; i++) {
        var dropdown = dropdowns[i];

        if (event.target === homeLink) {
            dropdown.classList.remove('active');
        } else {
            dropdown.classList.toggle('active');
        }
    }

    event.stopPropagation();
}
