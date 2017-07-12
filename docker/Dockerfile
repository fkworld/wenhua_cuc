FROM python

MAINTAINER fengyong fkworld@foxmail.com

WORKDIR app
VOLUME ["/app"]
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt

EXPOSE 80

CMD ["gunicorn","-w","4","-b","0.0.0.0:80","start:app"]