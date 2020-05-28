FROM docker.io/centos/python-36-centos7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
CMD ["./delete-indices.py"]