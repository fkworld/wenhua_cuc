FROM python

MAINTAINER fengyong fkworld@foxmail.com

RUN python -m pip install --upgrade pip
RUN venv\Scripts\activate.bat
RUN pip install -r requirements.txt

EXPOSE 5000

CMD gunicorn -w 4 -b 114.215.141.112:5000 start:app