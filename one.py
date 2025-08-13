from celery import Celery
import time

# http://localhost:15672/

# without backend
# app = Celery('first', broker='amqp://guest:guest@localhost:5672')

app = Celery('one', broker='amqp://guest:guest@localhost:5672', backend='rpc://')

@app.task(name='one.adding')
def add(a, b):
    time.sleep(15)
    return a + b


@app.task
def sub(a, b):
    return a - b

# result = add.apply_async((5, 4), link=sub.signature((2,)))
