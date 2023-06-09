document.addEventListener("DOMContentLoaded", function() {
    function toggleSidebar() {
        document.querySelector("body").classList.toggle("hide-sidebar");
    }
    // Add event listener to the hamburger icon
    document.querySelector(".hamburger").addEventListener("click", toggleSidebar); 
});