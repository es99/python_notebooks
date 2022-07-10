"""Script que que procura todos os arquivos .csv no diretório atual,
lê esses arquivos e grava-os em um diretório 'headerRemoved' os mesmos arquivos
sem os cabeçalhos"""

import os
import csv

os.makedirs('headerRemoved', exist_ok=True)

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    print(f'Removendo cabeçalho do arquivo {csvFilename}...')

    csvRows = []
    with open(csvFilename) as csvReader:
        csv_reader = csv.reader(csvReader)
        for row in csv_reader:
            if csv_reader.line_num == 1:
                continue
            csvRows.append(row)

    with open(os.path.join('headerRemoved', csvFilename), 'w', newline='') as csvFileObj:
        csv_writer = csv.writer(csvFileObj)
        for row in csvRows:
            csv_writer.writerow(row)

