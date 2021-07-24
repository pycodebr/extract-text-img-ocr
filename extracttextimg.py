from os import read
import easyocr

# Define o idioma a ser usado
reader = easyocr.Reader(['pt'])

# Carrega e faz a leitura da imagem
results = reader.readtext('exemplo.png', paragraph=False)

print('\n\n')
# Mostra resultados
for result in results:
    print(f'Texto: {result[1]}\n'
        f'Posição: {result[0]}\n')
