FROM registry.access.redhat.com/ubi8/python-312
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt 
CMD ["./delete-indices.py"]
