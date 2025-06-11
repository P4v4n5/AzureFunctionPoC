document.addEventListener('DOMContentLoaded', function () {
    const links = document.querySelectorAll('.menu a');
    links.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(link.getAttribute('href')).scrollIntoView({ behavior: 'smooth' });
        });
    });
});
