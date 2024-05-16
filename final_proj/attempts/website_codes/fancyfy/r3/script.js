const contentData = [
    {
        text: "Introduction to Boston Traffic",
        visualization: "<p>Visualization of traffic introduction goes here.</p>"
    },
    {
        text: "Population Impact on Traffic",
        visualization: `
            <div>
                <iframe src="population_combination_chart.html" width="100%" height="600"></iframe>
            </div>
        `
    },
    {
        text: "Projects Dedicated to Traffic Improvement",
        visualization: `
            <div>
                <iframe src="projects_bar_chart.html" width="100%" height="400"></iframe>
            </div>
        `
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
    }, 500);
}

function updateButtons() {
    document.getElementById('prevBtn').disabled = currentIndex === 0;
    document.getElementById('nextBtn').disabled = currentIndex === contentData.length - 1;
}

function renderCharts() {
    if (currentIndex === 2) {
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
