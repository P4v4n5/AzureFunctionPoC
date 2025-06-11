function navigateTo(sectionId) {
    // Hide all sections
    document.querySelectorAll('.section').forEach(sec => sec.classList.remove('active'));
    // Show the selected section
    document.getElementById(sectionId).classList.add('active');
    // Update nav button active state
    document.querySelectorAll('.nav-links button').forEach(btn => btn.classList.remove('active'));
    const navBtns = document.querySelectorAll('.nav-links button');
    const ids = ['about','certifications','skills','education','experience','projects'];
    ids.forEach((id, idx) => {
        if (id === sectionId) navBtns[idx].classList.add('active');
    });
}
// Set default section on load
window.onload = function() {
    navigateTo('about');
};
