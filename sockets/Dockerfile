FROM python:3.12.3-bookworm

WORKDIR /opt/app

EXPOSE 8765

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./socketio_server.py" ]