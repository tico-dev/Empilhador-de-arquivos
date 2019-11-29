import os
import openpyxl

files = []
juntar = []

cabecalho = "userid;nome;cpf;endereco"  # Defina um cabeçalho
diretorio = os.getcwd()

empilhado = open('empilhado.txt', 'a+', encoding='latin-1', errors='ignore')
for _, _, arquivos in os.walk(diretorio):
    for file in arquivos:
        file = file.lower()
        if ('.txt' in file or '.csv' in file) and 'empilhado' not in file:
            files.append(file)

        if '.xlsx' in file:
            file = file.replace('.xlsx', '')

            filename = f'{file}.xlsx'

            # Abre o arquivo xlsx
            xlsx = openpyxl.load_workbook(filename)

            # Ativa a planilha atual
            sheet = xlsx.active

            # Pega o conteudo da planilha
            data = sheet.rows

            # Cria o arquivo CSV
            csv = open(f"{file}.csv", "w+", encoding='latin-1', errors='ignore')

            for row in data:
                l = list(row)
                for i in range(len(l)):
                    if i == len(l) - 1:
                        csv.write(str(l[i].value))
                    else:
                        csv.write(str(l[i].value) + ';')
                csv.write('\n')
            files.append(f'{file}.csv')
            csv.close()

empilhado.write(cabecalho.replace(';', '|'))
for file in files:
    with open(os.path.dirname(os.path.realpath(__file__)).replace("\\", '/') + '/' + file, 'r', encoding='latin-1', errors='ignore') as arquivo:
        lines = arquivo.readlines()
        empilhado.write('\n')
        for line in lines:
            if cabecalho not in line.lower():
                empilhado.write(line.replace(' ', '').replace(';', '|'))


print('arquivos empilhados:', files)

for _, _, arquivos in os.walk(diretorio):
    print('Procurando arquivos gerados pelo programa...')
    for arquivo in arquivos:
        if '.xlsx' in arquivo:
            arquivo = arquivo.replace('xlsx', 'csv')
            print('Removido arquivo CSV gerado pelo programa:', arquivo)
            os.remove(arquivo)
