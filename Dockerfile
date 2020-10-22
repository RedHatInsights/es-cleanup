FROM registry.redhat.io/ubi8/python-36
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt 
CMD ["./delete-indices.py"]

