# Configuração de Ambiente Virtual em Python usando venv

# 1. Abra o terminal no VSCode (Ctrl + `) e navegue até o diretório do seu projeto.

# 2. Criação do Ambiente Virtual:
# Use o comando a seguir para criar um ambiente virtual chamado "venv".
# Certifique-se de que "python" seja o comando correto para o interpretador Python no seu sistema.
# No exemplo, usamos "python3" para sistemas Unix.
# Se você estiver no Windows, use "python" ou "python.exe".
# Se já houver um ambiente virtual, você pode pular este passo.
#python3 -m venv venv

# 3. Ativação do Ambiente Virtual:
# Ative o ambiente virtual para começar a usá-lo.
# No Windows:
# .\venv\Scripts\activate
# No Unix/Linux/Mac:
# source venv/bin/activate

# 4. Desativação do Ambiente Virtual:
# Quando terminar de trabalhar, você pode desativar o ambiente virtual.
# deactivate

# 5. Instalação de Pacotes:
# Com o ambiente virtual ativado, você pode instalar pacotes Python usando o pip.
# Exemplo:
# pip install nome_do_pacote

# Lembre-se de que a sintaxe para ativar o ambiente virtual pode variar entre sistemas operacionais.

# 6. Configure o Ambiente Virtual no VSCode (Opcional):
# Se você deseja que o VSCode use automaticamente o ambiente virtual,
# adicione a seguinte configuração no arquivo .vscode/settings.json:
# {
#     "python.pythonPath": "caminho_para_seu_projeto/venv/bin/python"
# }

# Certifique-se de ajustar os caminhos de acordo com a estrutura do seu projeto.

# Agora, você está pronto para trabalhar no seu ambiente virtual no VSCode!
