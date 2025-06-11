function showSection(hash) {
    const id = (hash || '#about').replace('#', '');
    // Hide all sections
    document.querySelectorAll('.section').forEach(sec => sec.classList.remove('active'));
    // Show the selected section
    const section = document.getElementById(id);
    if (section) {
        section.classList.add('active');
        section.scrollIntoView({ behavior: 'smooth' });
    }
    // Update nav link active state
    document.querySelectorAll('.sidebar-nav .nav-link').forEach(link => {
        if (link.getAttribute('href') === '#' + id) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

// Smooth scroll for sidebar nav links
document.querySelectorAll('.sidebar-nav .nav-link').forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault();
        const hash = this.getAttribute('href');
        window.location.hash = hash;
        showSection(hash);
    });
});

// Optional: Add scroll animations for card sections (if desired)
// function animateOnScroll() {
//     const elements = document.querySelectorAll('.card-section');
//     elements.forEach(element => {
//         const elementTop = element.getBoundingClientRect().top;
//         const elementVisible = 150;
//         if (elementTop < window.innerHeight - elementVisible) {
//             element.classList.add('active');
//         }
//     });
// }
// window.addEventListener('scroll', animateOnScroll);
// window.addEventListener('load', animateOnScroll);

// Update active nav item on scroll
function updateActiveNavItem() {
    const sections = document.querySelectorAll('.section');
    const navLinks = document.querySelectorAll('.sidebar-nav .nav-link');
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (window.scrollY >= sectionTop - 80) {
            current = section.getAttribute('id');
        }
    });
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('active');
        }
    });
}

window.addEventListener('scroll', updateActiveNavItem);
window.addEventListener('load', function() {
    showSection(window.location.hash);
    updateActiveNavItem();
});
window.addEventListener('hashchange', function() {
    showSection(window.location.hash);
    updateActiveNavItem();
});
