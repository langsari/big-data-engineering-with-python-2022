import json
import csv

# Open the JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Open the CSV file and write the header row
with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'age', 'email'])

    # Loop through each item in the JSON data and write a row to the CSV file
    for item in data:
        name = item['name']
        age = item['age']
        email = item['email']
        writer.writerow([name, age, email])
