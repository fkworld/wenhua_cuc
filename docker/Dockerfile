FROM python

MAINTAINER fengyong fkworld@foxmail.com

VOLUME ["/app"]
ADD /root/wenhua_cuc /app
WORKDIR app
RUN python -m pip install --upgrade pip
RUN pip install -r /root/wenhua_cuc/requirements.txt

EXPOSE 5000

CMD gunicorn -w 4 -b 114.215.141.112:5000 start:app