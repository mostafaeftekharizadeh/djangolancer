
FROM python:3.8.10

WORKDIR /code
COPY requirements.txt /code/
COPY .pipcache/ /root/.cache/pip/
RUN pip install -r requirements.txt

