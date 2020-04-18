FROM python:3

ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get install -y gdal-bin binutils libproj-dev libgdal-dev && \
    apt-get clean all && rm -rf /var/apt/lists/* && rm -rf /var/cache/apt/*

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT [ "./entrypoint.sh" ]