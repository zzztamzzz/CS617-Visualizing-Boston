# Data points from spreadsheet
data = [
    (2010, 7.45), (2011, 477.78), (2012, 316.47), (2013, 315.48),
    (2014, 349.87), (2015, 188.96), (2016, 242.4), (2017, 317.81),
    (2018, 521.02), (2019, 417.92), (2020, 346.89), (2021, 352.64),
    (2022, 239.5), (2023, 534.89), (2024, 123.45)
]

# SVG dimensions
svg_width = 700
svg_height = svg_width

# Determine min and max for scaling
years = [year for year, value in data]
values = [value for year, value in data]
min_year, max_year = min(years), max(years)
min_value, max_value = min(values), max(values)

# Calculate scaling factors
x_scale = svg_width / (max_year - min_year)
y_scale = svg_height / (max_value - min_value)

# Scale data points
scaled_points = [
    ((year - min_year) * x_scale, svg_height - (value - min_value) * y_scale)
    for year, value in data
]

# print(scaled_points);

# print("Here are the scaled values:")
# for point in scaled_points:
#     print(f"{point[0]:.2f}, {point[1]:.2f}")
# print("\n")

print("Adjusted by 20px")
for point in scaled_points:
    print(f"{point[0]+20:.2f}, {point[1]+20:.2f}")
print("\n")

print("\nsatisfy the lazy")
for x, y in scaled_points:
    print(f'<circle cx="{x+20:.2f}" cy="{y+20:.2f}" r="4" fill="red" />')
    # print(f'<circle cx="{x+20:.2f}" cy="{y+20:.2f}" r="4" fill="red">\n<title>2010: 620 inches</title>\n</circle>')

