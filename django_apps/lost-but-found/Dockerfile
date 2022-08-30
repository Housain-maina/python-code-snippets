FROM python:3.9

RUN mkdir /lost-but-found

WORKDIR /lost-but-found

COPY . /lost-but-found/

RUN pip install pipenv

RUN pipenv install --system --deploy
