from celery import Celery
import time

# http://localhost:15672/


app = Celery('first', broker='amqp://guest:guest@localhost:5672')


@app.task(name='one.adding')
def add(a, b):
    time.sleep(15)
    return a + b
