# use python 3 slim image.
FROM python:3.9-slim

# install system dependencies.
RUN apt-get clean && apt-get update \
  && apt-get install -y --no-install-recommends build-essential graphviz fonts-open-sans \
  && rm -rf /var/lib/apt/lists/*

# project directory.
WORKDIR /usr/src/diagrams

# Copy only diagrams and resources
COPY diagrams resources ./
COPY docker/requirements.txt /tmp/

# install python requirements
RUN pip install -r /tmp/requirements.txt \
    && rm -rf /tmp/
