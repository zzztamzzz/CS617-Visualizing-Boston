const contentData = [
    {
        text: `
            <h2>Introduction to Boston Traffic</h2>
            <p>Boston is known for its historic significance and vibrant culture. However, it is also infamous for its traffic congestion.</p>
            <p>With narrow streets and a high population density, traffic in Boston can be a nightmare for commuters.</p>
            <p>Let's explore the factors contributing to this traffic congestion.</p>
        `,
        images: [
            {
                url: "a_boston_picture.jpg",
                title: "Boston from Longfellow Bridge"
            },
            {
                url: "boston_on_road.jpg",
                title: "Boston again, on I-90 W at 6:00pm"
            }
        ],
        visualization: ""
    },
    {
        text: `
            <h2>Population Increase (Bar Chart)</h2>
            <p>Over the years, Boston has seen a significant increase in its population. This influx of people has naturally led to more vehicles on the road, contributing to the traffic problems. Let's look at a bar chart to understand the population growth better.</p>
        `,
        visualization: `
            <div class="iframe-container">
                <iframe src="population_bar_chart.html"></iframe>
            </div>
        `
    },
    {
        text: `
            <h2>Population Increase (Line Chart)</h2>
            <p>In addition to the bar chart, a line chart also helps visualize the population growth over time. Let's look at a line chart to get a different perspective on the population increase.</p>
        `,
        visualization: `
            <div class="iframe-container">
                <iframe src="population_line_chart.html"></iframe>
            </div>
        `
    },
    {
        text: `
            <h2>City Projects</h2>
            <p>Boston has undertaken several projects aimed at improving traffic conditions. These projects include building new roads, improving public transportation, and implementing traffic management systems. Here are some visualizations to show the impact of these projects.</p>
        `,
        visualization: `
            <div class="iframe-container">
                <iframe src="projects_bar_chart.html"></iframe>
            </div>
        `
    },
    {
        text: `
            <h2>Walkability Index</h2>
            <p>The Walkability Index measures how friendly an area is to walking. It considers factors such as the presence of footpaths, safety, and accessibility to amenities. This index helps understand how pedestrian-friendly Boston is, which can influence traffic patterns. Explore the interactive visualizations below to see how different factors affect the walkability index.</p>
        `,
        visualization: `
            <div class="iframe-container">
                <iframe src="correlation_matrix.html"></iframe>
            </div>
        `
    },
    {
        text: `
            <h2>Walkability vs Employment</h2>
            <p>This visualization shows the relationship between walkability and employment rates in different areas of Boston. Understanding this relationship helps in planning infrastructure improvements.</p>
        `,
        visualization: `
            <div class="iframe-container">
                <iframe src="walkability_vs_employment.html"></iframe>
            </div>
        `
    },
    {
        text: `
            <h2>Walkability vs Population</h2>
            <p>This visualization shows the relationship between walkability and population in different areas of Boston. Understanding this relationship helps in planning infrastructure improvements.</p>
        `,
        visualization: `
            <div class="iframe-container">
                <iframe src="walkability_vs_population.html"></iframe>
            </div>
        `
    },
    {
        text: `
            <h2>Walkability vs Shape Area</h2>
            <p>This visualization examines the correlation between walkability and the shape area of different regions. It provides insights into how the physical layout impacts walkability.</p>
        `,
        visualization: `
            <div class="iframe-container">
                <iframe src="walkability_vs_shape_area.html"></iframe>
            </div>
        `
    },
    {
        text: `
            <h2>Walkability vs Auto Ownership</h2>
            <p>This visualization explores how auto ownership affects walkability. Understanding this dynamic is crucial for urban planning and reducing traffic congestion.</p>
        `,
        visualization: `
            <div class="iframe-container">
                <iframe src="walkability_vs_auto0.html"></iframe>
                <iframe src="walkability_vs_auto1.html"></iframe>
                <iframe src="walkability_vs_auto2p.html"></iframe>
            </div>
        `
    },
    {
        text: `
            <h2>Wage Distribution</h2>
            <p>This visualization shows the wage distribution across different sectors and how it relates to walkability. It helps understand economic factors influencing traffic patterns.</p>
        `,
        visualization: `
            <div class="iframe-container">
                <iframe src="wage_distribution.html"></iframe>
            </div>
        `
    },
    {
        text: `
            <h2>Conclusion</h2>
            <p>Boston's traffic congestion is a multifaceted issue influenced by population growth, city infrastructure projects, and walkability. While various measures are being taken to improve the situation, it remains a challenge for the city. Understanding these factors through data visualizations can help in planning better solutions for the future.</p>
        `,
        visualization: ""
    }
];

let currentIndex = 0;

function updateContent() {
    const content = contentData[currentIndex];
    const textContentDiv = document.getElementById('text-content');
    const visualizationContentDiv = document.getElementById('visualization-content');

    textContentDiv.style.opacity = 0;
    visualizationContentDiv.style.opacity = 0;

    setTimeout(() => {
        textContentDiv.innerHTML = content.text;
        if (content.images) {
            const imageContainer = document.createElement('div');
            imageContainer.className = 'image-container';
            content.images.forEach(image => {
                const imageWrapper = document.createElement('div');
                imageWrapper.className = 'image-wrapper';
                const imgTitle = document.createElement('div');
                imgTitle.className = 'image-title';
                imgTitle.innerText = image.title;
                const img = document.createElement('img');
                img.src = image.url;
                img.alt = image.title;
                img.className = 'fade-in';
                imageWrapper.appendChild(imgTitle);
                imageWrapper.appendChild(img);
                imageContainer.appendChild(imageWrapper);
            });
            textContentDiv.appendChild(imageContainer);
        }
        if (content.visualization) {
            visualizationContentDiv.innerHTML = `
                <h2>Diagrams</h2>
                ${content.visualization}
            `;
            document.getElementById('content-container').style.gridTemplateColumns = '1fr 1fr';
        } else {
            visualizationContentDiv.innerHTML = '';
            document.getElementById('content-container').style.gridTemplateColumns = '1fr';
        }

        textContentDiv.style.opacity = 1;
        visualizationContentDiv.style.opacity = 1;

        updateButtons();
    }, 500);

    document.getElementById('progress').innerText = `${currentIndex + 1} / ${contentData.length}`;
}

function updateButtons() {
    document.getElementById('prevBtn').disabled = currentIndex === 0;
    document.getElementById('nextBtn').disabled = currentIndex === contentData.length - 1;
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
