# coding=utf-8
import os
import openpyxl
from datetime import datetime

print(f'Início junção: {datetime.now()}')
empilhados = []
files = []
# diretorio = 'C:/Users/Guto/Desktop/empilhador_folder'
diretorio = os.path.dirname(os.path.realpath(__file__))

empilhado = open('ARQUIVOS CONCATENADOS.txt', 'a+', encoding="utf-8", errors='ignore')


for _, _, arquivos in os.walk(diretorio):
    for file in arquivos:
        if ('.txt' in file.lower() or '.csv' in file.lower()) and 'ARQUIVOS CONCATENADOS' not in file.upper():
            files.append(file)
            empilhados.append(file)

        if '.xlsx' in file:
            global index
            print('ACHOU ARQUIVO EXCEL')
            file = file.replace('.xlsx', '')

            filename = f'{file}.xlsx'

            # Abre o arquivo xlsx
            xlsx = openpyxl.load_workbook(filename)

            # Ativa a planilha atual
            sheet = xlsx.active

            # Pega o conteudo da planilha
            data = sheet.rows

            for index, row in enumerate(data):
                if index == 0:
                    continue
                l = list(row)
                for i in range(len(l)):
                    if i == len(l) - 1:
                        empilhado.write(str(l[i].value))
                    else:
                        empilhado.write(str(l[i].value) + '|')
                empilhado.write('\n')
            empilhados.append(file)

for file in files:
    with open(os.path.dirname(os.path.realpath(__file__)).replace("\\", '/') + '/' + file, 'r', encoding="utf-8", errors='ignore') as arquivo:
        lines = arquivo.readlines()[1:]
        tamanho = len(lines)
        print(f'Linhas em {file}: {tamanho}')
        empilhado.write(''.join(lines).replace(';', '|'))


print('arquivos empilhados:', empilhados)
print(f'final junção: {datetime.now()}')

empilhado.close()

print('Contando linhas no arquivo gerado:')
novo_arquivo = open('ARQUIVOS CONCATENADOS.txt', 'r', encoding="utf-8", errors='ignore')
novo_arquivo_linhas = novo_arquivo.readlines()
novo_arquivo_tamanho = len(novo_arquivo_linhas)


print(f'Linhas em ARQUIVOS CONCATENADOS.txt: {novo_arquivo_tamanho}')
