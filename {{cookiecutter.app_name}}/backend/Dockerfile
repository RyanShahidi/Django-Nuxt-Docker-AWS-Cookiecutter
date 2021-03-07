FROM public.ecr.aws/bitnami/python:3.8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app
COPY . /usr/src/app/
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./entrypoint-prod.sh /usr/src/app/entrypoint-prod.sh
RUN chmod +x /usr/src/app/entrypoint-prod.sh

ENTRYPOINT ["/usr/src/app/entrypoint-prod.sh"]