FROM python:3.12
LABEL version="0.0.1" maintainer="PGDev" authors="PGDev, Shad0wcs, Mo11ex"

ENV PYTHONUBUFFERED=1

RUN mkdir /home/app/
RUN mkdir /home/app/web/
RUN mkdir /home/app/web/static
WORKDIR /home/app/web

COPY poetry.lock pyproject.toml ./

RUN pip install --upgrade pip "poetry==1.8.4"

RUN poetry config virtualenvs.create false --local

RUN poetry install

RUN apt-get update \
  && apt-get -y install tesseract-ocr && apt-get -y install ffmpeg libsm6 libxext6 # required for opencv

COPY codelens_backend /home/app/web
