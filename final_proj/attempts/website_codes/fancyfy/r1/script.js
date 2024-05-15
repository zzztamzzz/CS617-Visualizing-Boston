const contentData = [
    {
        text: "Introduction to Boston Traffic",
        visualization: "<p>Visualization of traffic introduction goes here.</p>"
    },
    {
        text: "Population Impact on Traffic",
        visualization: "<canvas id='populationChart'></canvas>"
    },
    {
        text: "Projects Dedicated to Traffic Improvement",
        visualization: "<canvas id='projectsChart'></canvas>"
    },
    {
        text: "Walkability Index",
        visualization: "<p>Visualization of walkability index goes here.</p>"
    }
];

let currentIndex = 0;

function updateContent() {
    const content = contentData[currentIndex];
    const contentDiv = document.getElementById('content');
    contentDiv.style.opacity = 0;
    setTimeout(() => {
        contentDiv.innerHTML = `
            <h2>${content.text}</h2>
            ${content.visualization}
        `;
        contentDiv.style.opacity = 1;
        renderCharts();
        updateButtons();
    }, 300);
}

function updateButtons() {
    document.getElementById('prevBtn').disabled = currentIndex === 0;
    document.getElementById('nextBtn').disabled = currentIndex === contentData.length - 1;
}

function renderCharts() {
    if (currentIndex === 1) {
        const ctx = document.getElementById('populationChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['2010', '2015', '2020', '2025'],
                datasets: [{
                    label: 'Population',
                    data: [600000, 650000, 700000, 750000],
                    borderColor: 'rgba(75, 192, 192, 1)',
                    fill: false
                }]
            }
        });
    } else if (currentIndex === 2) {
        const ctx = document.getElementById('projectsChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Project 1', 'Project 2', 'Project 3'],
                datasets: [{
                    label: 'Number of Projects',
                    data: [5, 10, 3],
                    backgroundColor: 'rgba(153, 102, 255, 0.2)',
                    borderColor: 'rgba(153, 102, 255, 1)',
                    borderWidth: 1
                }]
            }
        });
    }
}

function init() {
    document.getElementById('prevBtn').addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateContent();
        }
    });

    document.getElementById('nextBtn').addEventListener('click', () => {
        if (currentIndex < contentData.length - 1) {
            currentIndex++;
            updateContent();
        }
    });

    updateContent();
}

window.onload = init;
