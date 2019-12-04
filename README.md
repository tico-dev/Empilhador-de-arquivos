# Empilhador-de-arquivos
"Empilha" o conteúdo de arquivos de texto e arquivos excel (.xlsx), ignorando os títulos de coluna com intuito de concatenar apenas o conteúdo dos arquivos, não o cabeçalho.


# Motivo
Como eu precisei (por 2 dias seguidos) juntar arquivos de texto (concatenar) manualmente, criei um script python que otimiza meu tempo, fazendo meu trabalho de forma automática.

Inicialmente ele só empilhava, mas ainda tinha que converter os arquivos de formato ".xlsx" (excel) para ".csv"(arquivo de texto) manualmente, e isso era o que mais demorava. Para resolver o problema sem danificar/alterar o arquivo fonte, pensei em: abrir o arquivo Excel, transcrever o conteúdo dele para o arquivo "concatenado.txt", e depois fazer isso com todos os outros arquivos (ou repetir o processo, caso haja algum outro arquivo excel).

# Resultado
Empilhar arquivos é realmente algo muito fácil de ser feito manualmente, mas toma muito tempo do nosso dia e, dependendo do tamanho arquivo, ele pode não ser "readable" pelo notepad++ e outros editores de texto.
Como resposta do script python, algo que antes eu fazia em 1h e 30m, as vezes até 2h -> agora faço em questão de SEGUNDOS.
