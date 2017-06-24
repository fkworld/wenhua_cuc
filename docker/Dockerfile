FROM python

MAINTAINER fengyong fkworld@foxmail.com

WORKDIR /root/wenhua_cuc

RUN python -m pip install --upgrade pip
RUN venv/scripts/active.bat
RUN pip install -r /root/wenhua_cuc/requirements.txt

EXPOSE 5000

CMD gunicorn -w 4 -b 114.215.141.112:5000 start:app