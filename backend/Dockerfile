# Derivando da imagem oficial do Python 3.11
FROM python:3.11

# Definir o workdir
WORKDIR /home/code

# Mover o arquivo de dependência do projeto para o workdir
COPY ./requirements.txt .

# Instalar dependências do projeto
RUN pip install --no-cache-dir --upgrade -r /home/code/requirements.txt

# Copiar a pasta do projeto no workdir
COPY ./app /home/code/app

# Comando para subir o app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
