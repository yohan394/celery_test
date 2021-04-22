from __future__ import absolute_import, unicode_literals 
from celery import shared_task 
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from some_module.utils import asyn_update_queue

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="update_queue",
    ignore_result=True
)
def update_queue():
    """
    Delete queues 
    """
    asyn_update_queue()
    print("periodic_task is working")

@shared_task 
def add(x, y): 
    return x + y 

@shared_task 
def mul(x, y): 
    return x * y 
    
@shared_task 
def xsum(numbers): 
    return sum(numbers)



