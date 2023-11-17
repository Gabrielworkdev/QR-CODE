import pyqrcode

#Solicitando para criar uma qrcode referente ao link
url = pyqrcode.create (' https://gabrielworkdev.github.io/MY-PAGE/')
#Solicitando a criação de um svg com o qrcode
#criacao /// nome do arquivo// tamanho 
url.svg ('Nossa-página.svg', scale=6)
#codigo para executar o script no terminal "python app.py""
#Gerando png
url.png('Nossa-pagina.png', scale=5)

