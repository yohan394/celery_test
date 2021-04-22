FROM python:3.7.6
ENV PYTHONUNBUFFERED 1

WORKDIR /user/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY . .


