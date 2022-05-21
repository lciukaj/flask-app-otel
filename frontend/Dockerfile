# set base image (host OS)
FROM python:3.8-slim

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
ADD . /app

# install dependencies
RUN pip install -r requirements.txt
RUN opentelemetry-bootstrap --action=install

# Make port 5000 available for links and/or publish
EXPOSE 5000

# command to run on container start
# ENTRYPOINT [ "python" ]
# CMD [ "app.py" ]

CMD [ "opentelemetry-instrument", "--resource_attributes", "service.namespace=flask-otel-test,service.name=frontend", "--traces_exporter", "otlp", "--exporter_otlp_endpoint", "http://otel-collector:4317", "python3", "app.py"]