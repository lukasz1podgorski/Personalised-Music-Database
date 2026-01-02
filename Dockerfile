FROM python:3.13

WORKDIR /spotifyAPItoDBproject

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]