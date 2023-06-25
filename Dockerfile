# syntax=docker/dockerfile:1
FROM python:3.8.10
# ENV SECRET_KEY 71)0c2pluviivk1!p93qouc_w017(#%x#g+2(*eo(0sf6h)vq3
# ENV DEBUG 1
# ENV ALLOWED_HOSTS 127.0.0.1 midlancer.ir
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY .pipcache/ /root/.cache/pip/
RUN pip install -r requirements.txt

