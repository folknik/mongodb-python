FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/app
RUN mkdir -p /usr/app/logs

COPY /src/app.py /usr/app
COPy requirements.txt /usr/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "-u", "app.py"]