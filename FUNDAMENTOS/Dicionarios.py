# 1. Dicionário de Informações Pessoais
# dict
dicionario_pessoa = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# 2. Dicionário de Contatos
# dict
dicionario_contatos = {
    'amigo1': {'nome': 'Alice', 'telefone': '123-456'},
    'amigo2': {'nome': 'Bob', 'telefone': '789-012'}
}

# 3. Adição de Novo Par Chave-Valor
dicionario_pessoa['profissao'] = 'Engenheiro'

# 4. Acesso a Valor pela Chave
idade = dicionario_pessoa['idade']

# 5. Remoção de Par Chave-Valor
del dicionario_pessoa['cidade']

# 6. Verificação de Existência de Chave
tem_profissao = 'profissao' in dicionario_pessoa

# 7. Chaves, Valores e Itens do Dicionário
chaves = dicionario_pessoa.keys()
valores = dicionario_pessoa.values()
itens = dicionario_pessoa.items()

# 8. Iteração sobre um Dicionário
for chave, valor in dicionario_pessoa.items():
    print(f"{chave}: {valor}")
