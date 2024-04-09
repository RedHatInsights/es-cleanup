FROM registry.redhat.io/ubi8/python-311
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt 
CMD ["./delete-indices.py"]
