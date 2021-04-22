## What is Celery?
- Celery is an application for processing queues written in python language.

## Main Uses
- real-time processing
- supporting task scheduling

## What is Task Queues then?
- Task queues are used as a mechanism to distribute work across threads or machines.

## How does it work?
- Celery communiactes via messages, usually using a broker to meditate between clients and workers.
- A celery system consists of multiple workers and brokers, giving way to high availability and horizontal scaling.


## Simple celery app

```
from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')

@app.task
def hello():
    return 'hello world'
```

## Possible Brokers
name | Status | Monitoring | Remote Controlling
|:---:|:---:|:---:|:---:
Redis | Stable | O | O
RabbitMQ  | Stable | O | O
Amazon SQS | Stable | X | X
Zookeeper | Experimental | X | X 

## Running Celery Worker
```
celery -A tasks worker --loglevel=info
``` 

## Loads Config File(django settings)
#### celery.py
```
app.config_from_object('django.conf:settings', namespace='CELERY') 
```
#### settings.py (redis as a broker)
```
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379' 
CELERY_ACCEPT_CONTENT = ['application/json'] 
CELERY_TAST_SERIALIZER = 'json' 
CELERY_RESULT_SERIALIZER = 'json' 
CELERY_TIMEZONE = 'Asia/Seoul'
```



