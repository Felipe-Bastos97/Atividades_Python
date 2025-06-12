from pathlib import Path

# tenta encontrar a pasta Desktop ou Área de Trabalho
home = Path.home()
possiveis_nomes = ['Desktop', 'Área de Trabalho']

for nome in possiveis_nomes:
    desktop = home / nome
    if desktop.exists():
        break
else:
    raise FileNotFoundError("Não foi possível localizar a área de trabalho.")

# cria o caminho do arquivo
arquivo = desktop / 'meu_arquivo.txt'

# escreve no arquivo
with open(arquivo, 'w', encoding='utf-8') as f:
    f.write('Arquivo criado na sua área de trabalho com sucesso!')

print(f'Arquivo criado em: {arquivo}')
