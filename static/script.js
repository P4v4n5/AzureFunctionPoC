
function showSection(hash) {
    const id = (hash || '#about').replace('#', '');
    document.querySelectorAll('.section').forEach(sec => sec.classList.remove('active'));
    const section = document.getElementById(id);
    if (section) section.classList.add('active');
    document.querySelectorAll('.side-nav .nav-link').forEach(link => link.classList.remove('active'));
    const nav = document.querySelector('.side-nav .nav-link[href="#' + id + '"]');
    if (nav) nav.classList.add('active');
}

window.addEventListener('DOMContentLoaded', function() {
    showSection(window.location.hash);
    document.querySelectorAll('.side-nav .nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const hash = this.getAttribute('href');
            window.location.hash = hash;
            showSection(hash);
        });
    });
    window.addEventListener('hashchange', function() {
        showSection(window.location.hash);
    });
});
