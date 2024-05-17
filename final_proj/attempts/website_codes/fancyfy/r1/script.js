document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('introduction').classList.add('active');
    setupNavigation();
});

function nextSection(sectionId) {
    const currentSection = document.querySelector('.content.active');
    currentSection.classList.remove('active');
    setTimeout(() => {
        currentSection.style.display = 'none';
        const nextSection = document.getElementById(sectionId);
        nextSection.style.display = 'block';
        setTimeout(() => {
            nextSection.classList.add('active');
        }, 10);
    }, 500);
}

function prevSection(sectionId) {
    const currentSection = document.querySelector('.content.active');
    currentSection.classList.remove('active');
    setTimeout(() => {
        currentSection.style.display = 'none';
        const prevSection = document.getElementById(sectionId);
        prevSection.style.display = 'block';
        setTimeout(() => {
            prevSection.classList.add('active');
        }, 10);
    }, 500);
}

function setupNavigation() {
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const sectionId = this.getAttribute('href').substring(1);
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
        });
    });
}
