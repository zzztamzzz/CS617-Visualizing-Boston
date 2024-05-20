// Simple script for the website behavior.
// Script ensures when shortcut is clicked we go to the specific section by scrolling/
// We also have a scroll to top button
document.addEventListener('DOMContentLoaded', function () {
    setupNavigation();
    setupBackToTopButton();
});

function setupNavigation() {
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const sectionId = this.getAttribute('href').substring(1);
            const section = document.getElementById(sectionId);
            const headerOffset = document.querySelector('nav').offsetHeight;
            const additionalOffset = 20; // Adjust this value as needed
            const elementPosition = section.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset - additionalOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
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
