FROM python:3.6 

RUN pip3 install grpcio 
RUN pip3 install google-api-python-client

ADD app /app/

EXPOSE 50051  
