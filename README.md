# Empilhador-de-arquivos
"Empilha" arquivos de texto ('txt' e 'csv') e, caso haja algum xlsx: cria um CSV com o conteúdo do XLSX e empilha o conteúdo dele também.


# Motivo
Como eu precisei (por 2 dias seguidos) juntar arquivos de texto (concatenar) manualmente, criei um script python que otimiza meu tempo, fazendo meu trabalho em "automático".

Inicialmente ele só empilhava, mas ainda tinha que converter os arquivos de formato ".xlsx" (excel) para ".csv"(arquivo de texto) manualmente, e isso era o que mais demorava. Para resolver o problema sem danificar/alterar o arquivo fonte, pensei em: ler o arquivo '.xlsx' e transcrever o conteúdo dele para um arquivo de texto (.csv) separado por ";" (para separar os campos [colunas] caso o arquivo seja aberto no Excel). Após gerar o arquivo filho '.csv', ele seria adicionado no array de "arquivos para ler", e seria empilhado junto com os outros.
