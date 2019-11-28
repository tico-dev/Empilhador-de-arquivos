import os
import openpyxl

files = []

empilhado = open('empilhado.txt', 'a+', errors='ignore')
for path, diretorio, arquivos in os.walk('C:/Users/gustavo.gomes/Desktop/empilhador'):
    for file in arquivos:
        if ('.txt' in file or '.csv' in file) and 'empilhado' not in file:
            files.append(file)

        elif '.xlsx' in file:
            file = file.replace('.xlsx', '')

            filename = f'{file}.xlsx'

            # Abre o arquivo xlsx
            xlsx = openpyxl.load_workbook(filename)

            # Ativa a planilha atual
            sheet = xlsx.active

            # Pega o conteudo da planilha
            data = sheet.rows

            # Cria o arquivo CSV
            csv = open(f"{file}.csv", "w+", errors='ignore')

            for row in data:
                l = list(row)
                for i in range(len(l)):
                    if i == len(l) - 1:
                        csv.write(str(l[i].value))
                    else:
                        csv.write(str(l[i].value) + ';')
                csv.write('\n')

            csv.close()
            files.append(f'{file}.csv')




for file in files:
    with open('C:/Users/gustavo.gomes/Desktop/empilhador/' + file, 'r', encoding='latin-1', errors='ignore') as arquivo:
        lines = arquivo.readlines()
        for line in lines:
            empilhado.write(line)

print('arquivos lidos:', files)
