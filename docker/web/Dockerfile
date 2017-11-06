FROM python:3.6.2

RUN mkdir /code
WORKDIR /code

RUN mkdir /tmp/requirements
COPY ./requirements /tmp/requirements
RUN pip install --no-cache-dir -r /tmp/requirements/dev.txt

COPY . /code/
