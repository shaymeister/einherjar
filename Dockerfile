# defines the runtime environment for einherjar.py
FROM python:3.7.4-stretch
ADD requirements.txt /
ADD einherjar.py /
ADD mypkg /
ADD data /
RUN pip install --upgrade pip && pip install -r requirements.txt
ENTRYPOINT ["python3", "./einherjar.py"]
LABEL maintainer="Shay Snyder shaymeister@hotmail.com"
