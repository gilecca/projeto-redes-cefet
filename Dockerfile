# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do servidor e do cliente
COPY server/server.py ./server/
COPY client/client.py ./client/

# Comando padrão para rodar o servidor
CMD ["python", "server/server.py"]