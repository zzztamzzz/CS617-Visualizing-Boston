document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('introduction').classList.add('active');
    setupNavigation();
    setupBackToTopButton();
});

function nextSection(sectionId) {
    changeSection(sectionId);
}

function prevSection(sectionId) {
    changeSection(sectionId);
}

function changeSection(sectionId) {
    const currentSection = document.querySelector('.content.active');
    currentSection.classList.remove('active');
    setTimeout(() => {
        currentSection.style.display = 'none';
        const targetSection = document.getElementById(sectionId);
        targetSection.style.display = 'block';
        setTimeout(() => {
            targetSection.classList.add('active');
        }, 10);
    }, 500);
}

function setupNavigation() {
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const sectionId = this.getAttribute('href').substring(1);
            changeSection(sectionId);
        });
    });
}

function setupBackToTopButton() {
    const backToTopButton = document.getElementById('back-to-top');
    window.addEventListener('scroll', function () {
        if (window.scrollY > 200) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    backToTopButton.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}
