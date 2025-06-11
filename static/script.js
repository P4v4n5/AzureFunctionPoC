function showSection(hash) {
    const id = (hash || '#about').replace('#', '');
    document.querySelectorAll('.section').forEach(sec => sec.classList.remove('active'));
    const section = document.getElementById(id);
    if (section) {
        section.classList.add('active');
        section.scrollIntoView({ behavior: 'smooth' });
    }
    document.querySelectorAll('.nav-links a').forEach(link => {
        if (link.getAttribute('href') === '#' + id) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

// Smooth scroll function
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add scroll animations
function animateOnScroll() {
    const elements = document.querySelectorAll('.container section');
    
    elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 150;
        
        if (elementTop < window.innerHeight - elementVisible) {
            element.classList.add('active');
        }
    });
}

window.addEventListener('scroll', animateOnScroll);
window.addEventListener('load', animateOnScroll);

// Add active state to nav items
function updateActiveNavItem() {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-bar a');
    
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (window.scrollY >= sectionTop - 60) {
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
window.addEventListener('load', updateActiveNavItem);

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
