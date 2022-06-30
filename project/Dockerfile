FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app/api
COPY requirments.txt ./
RUN pip install -r requirments.txt
COPY . ./
EXPOSE 8000
