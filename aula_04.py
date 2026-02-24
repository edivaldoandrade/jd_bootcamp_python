# Arquivos
import csv

file_path = "files/report_20260222111308.csv"

csv_file : list = []

# open csv delimiter is ;
with open(file_path, mode="r") as file:
    csv_reader = csv.DictReader(file, delimiter=";")
    
    for row in csv_reader:
        csv_file.append(row)

print(csv_file)