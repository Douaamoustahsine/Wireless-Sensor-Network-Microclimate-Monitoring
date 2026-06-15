import re
import csv

input_file = "data_raw.txt"
output_file = "data_clean.csv"

with open(input_file, "r") as f:
    data = f.read()

pattern = r"Temp:\s*([\d.]+),\s*Hum:\s*([\d.]+),\s*Pres:\s*([\d.]+)_#BAT:(\d+)"

matches = re.findall(pattern, data)

with open(output_file, "w") as f:
    f.write("Temperature,Humidity,Pressure,Battery\n")
    for m in matches:
        f.write(",".join(m) + "\n")

print("Done! File created:", output_file)


html_file = "index.html"

with open("data_clean.csv", "r") as csvfile:
    reader = csv.reader(csvfile)

    with open(html_file, "w", encoding="utf-8") as html:
        html.write("""
<html>
<head>
<title>IoT Sensors</title>
</head>
<body>
<h1>Sensor data</h1>
<table border="1">
""")

        for row in reader:
            html.write("<tr>")
            for cell in row:
                html.write(f"<td>{cell}</td>")
            html.write("</tr>")

        html.write("""
</table>
</body>
</html>
""")

print("HTML created : index.html")