# 1. Leitura de um Arquivo de Texto
# open, read
with open("exemplo.txt", "r") as arquivo_leitura:
    conteudo = arquivo_leitura.read()
    print("Conteúdo do arquivo:")
    print(conteudo)

# 2. Escrita em um Arquivo de Texto
# open, write
with open("novo_arquivo.txt", "w") as arquivo_escrita:
    arquivo_escrita.write("Olá, este é um novo arquivo!\n")
    arquivo_escrita.write("Segunda linha do arquivo.\n")

# 3. Leitura e Escrita em um Arquivo de Texto
# open, read, write
with open("arquivo_existente.txt", "a+") as arquivo_leitura_escrita:
    arquivo_leitura_escrita.write("Adicionando nova linha.\n")
    arquivo_leitura_escrita.seek(0)  # Reposiciona o cursor no início do arquivo
    novo_conteudo = arquivo_leitura_escrita.read()
    print("Novo conteúdo do arquivo:")
    print(novo_conteudo)

# 4. Leitura de Linhas de um Arquivo
# open, readline
with open("exemplo_linhas.txt", "r") as arquivo_linhas:
    linhas = arquivo_linhas.readlines()
    print("Linhas do arquivo:")
    for linha in linhas:
        print(linha.strip())  # Remove espaços em branco e quebras de linha

# 5. Manipulação de Arquivos Binários
# open, read, write, rb, wb
with open("arquivo_binario.jpg", "rb") as arquivo_binario_leitura:
    dados_binarios = arquivo_binario_leitura.read()

with open("copia_arquivo_binario.jpg", "wb") as arquivo_binario_escrita:
    arquivo_binario_escrita.write(dados_binarios)

print("Arquivo binário copiado com sucesso.")
