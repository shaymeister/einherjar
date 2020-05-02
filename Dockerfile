# defines the runtime environment for einherjar.py
FROM python:3.7.7-stretch
ADD requirements.txt ./
ADD einherjar.py ./
ADD valkyrie_pkg /valkyrie_pkg
ADD data /data
ADD results /results
RUN pip install --upgrade pip && pip install -r requirements.txt
ENTRYPOINT ["python3", "./einherjar.py"]
LABEL maintainer="Shay Snyder snyderse2@etsu.edu"