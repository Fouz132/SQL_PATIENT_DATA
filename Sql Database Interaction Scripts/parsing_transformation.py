import csv
import json
import xml.etree.ElementTree as ET

def read_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def read_json(file_path):
    with open(file_path, 'r') as jsonfile:
        return json.load(jsonfile)

def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return [dict((child.tag.split('}')[1], child.text) for child in item) for item in root]

def transform_to_standard_format(data, source_format):
    # Implement your transformation logic here based on the actual structure of your data
    if source_format == 'CSV':
        # Example: Assume CSV has columns 'patient_id', 'name', 'age', 'phone', 'aadhar'
        return [{'patient_id': row['patient_id'], 'patient_name': row['name'], 'age': row['age'], 'phone': row['phone'], 'aadhar': row['aadhar']} for row in data]
    elif source_format == 'JSON':
        # Updated Example: Assume JSON has structure [{'patient_id': 1, 'name': 'John', 'age': 30, 'phone': '1234567890', 'aadhar': '1234-5678-9012'}, ...]
        return [{'patient_id': patient['patient_id'], 'patient_name': patient['name'], 'age': patient['age'], 'phone': patient['phone'], 'aadhar': patient['aadhar']} for patient in data]
    elif source_format == 'XML':
        # Example: Assume XML has structure <patients><patient><patient_id>1</patient_id><name>John</name><age>30</age><phone>1234567890</phone><aadhar>1234-5678-9012</aadhar></patient>...</patients>
        return [{'patient_id': item['patient_id'], 'patient_name': item['name'], 'age': item['age'], 'phone': item['phone'], 'aadhar': item['aadhar']} for item in data]

def save_to_csv(data, file_path):
    # Save data to CSV file
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def save_to_json(data, file_path):
    # Save data to JSON file
    with open(file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

def main():
    # Specify file paths for sample data and output files
    csv_file_path = 'C:/Users/palag/OneDrive/Desktop/SQL/Sql Database Interaction Scripts/Patient_Data_CSV.csv'
    json_file_path = 'C:/Users/palag/OneDrive/Desktop/SQL/Sql Database Interaction Scripts/Patient_Data_JSON.json'

    # Read data from different formats
    csv_data = read_csv(csv_file_path)
    json_data = read_json(json_file_path)

    # Transform data to a standardized format
    transformed_csv = transform_to_standard_format(csv_data, 'CSV')
    transformed_json = transform_to_standard_format(json_data, 'JSON')

    # Print or further process the transformed data
    print("Transformed CSV Data:", transformed_csv)
    print("Transformed JSON Data:", transformed_json)

    # Save transformed data to new CSV and JSON files
    save_to_csv(transformed_csv, 'C:/Users/palag/OneDrive/Desktop/SQL/Sql Database Interaction Scripts/Transformed_Data_CSV.csv')
    save_to_json(transformed_json, 'C:/Users/palag/OneDrive/Desktop/SQL/Sql Database Interaction Scripts/Transformed_Data_JSON.json')

if __name__ == "__main__":
    main()
