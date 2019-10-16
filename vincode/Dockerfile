FROM python:3.6
ADD . /vincode/
WORKDIR /vincode
RUN pip install --upgrade pip
RUN pip install -r /vincode/requirements.txt
RUN python /vincode/manage.py collectstatic 
RUN python /vincode/manage.py makemigrations && python /vincode/manage.py migrate 
CMD gunicorn --bind 0.0.0.0:$PORT config.wsgi