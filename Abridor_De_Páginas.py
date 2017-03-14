import webbrowser
import time
link = input('Informe O Link Desejado\n')
tempo = eval(input('Informe O Tempo De Abertura Das Páginas(Seg)'))
while True:
    webbrowser.open(link)
    time.sleep(tempo)
