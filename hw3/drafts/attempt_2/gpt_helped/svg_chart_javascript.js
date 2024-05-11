
<script>
    window.onload = function() {
        const svgNS = "http://www.w3.org/2000/svg";
        const svgContainer = document.getElementById('lineChart');
        const xOffset = 60; // Offset for the x-axis to start more to the right
        const yOffset = 450; // Adjust y-axis height to fit within the axes
        const yAxisHeight = 500;
        const xAxisLength = 940; // Adjust x-axis length to fit within the SVG

        const dataPoints = document.querySelectorAll('#chartData [data-point]');
        let points = "";

        dataPoints.forEach((elem, index) => {
            const [x, y] = elem.getAttribute('data-point').split(',').map(Number);
            const scaledX = xOffset + (x - 2010) * (xAxisLength / (2023 - 2010)); // Adjust scale for x considering the xOffset
            const scaledY = yOffset - (y / 1.5); // Adjust scale for y
            points += `${scaledX},${scaledY} `;
        });

        const polyline = document.createElementNS(svgNS, "polyline");
        polyline.setAttribute("points", points.trim());
        polyline.setAttribute("stroke", "blue");
        polyline.setAttribute("stroke-width", "2");
        polyline.setAttribute("fill", "none");
        svgContainer.appendChild(polyline);

        // Draw Y-axis, now starting from xOffset to align with the first data point
        const yAxis = document.createElementNS(svgNS, "line");
        yAxis.setAttribute("x1", xOffset);
        yAxis.setAttribute("y1", "0");
        yAxis.setAttribute("x2", xOffset);
        yAxis.setAttribute("y2", yAxisHeight);
        yAxis.setAttribute("class", "axis");
        svgContainer.appendChild(yAxis);

        // Draw X-axis, adjusting its length to fit within the SVG container
        const xAxis = document.createElementNS(svgNS, "line");
        xAxis.setAttribute("x1", xOffset);
        xAxis.setAttribute("y1", yOffset);
        xAxis.setAttribute("x2", xOffset + xAxisLength);
        xAxis.setAttribute("y2", yOffset);
        xAxis.setAttribute("class", "axis");
        svgContainer.appendChild(xAxis);

        // Axis labels
        const yAxisLabel = document.createElementNS(svgNS, "text");
        yAxisLabel.setAttribute("x", -200);
        yAxisLabel.setAttribute("y", 20);
        yAxisLabel.setAttribute("transform", "rotate(-90)");
        yAxisLabel.setAttribute("class", "axis-label");
        yAxisLabel.textContent = "Measured Rainfall (inches)";
        svgContainer.appendChild(yAxisLabel);

        const xAxisLabel = document.createElementNS(svgNS, "text");
        xAxisLabel.setAttribute("x", xOffset + (xAxisLength / 2) - 20);
        xAxisLabel.setAttribute("y", "520");
        xAxisLabel.setAttribute("class", "axis-label");
        xAxisLabel.textContent = "Years";
        svgContainer.appendChild(xAxisLabel);
    };
</script>
