from celery import Celery, chain, group
import time


app = Celery('three', broker='amqp://guest:guest@localhost:5672', backend='rpc://')

@app.task(name='three.adding')
def add(a, b):
    time.sleep(2)
    return a + b


@app.task
def sub(a, b):
    return a - b


# result = chain(add.s(3, 4), sub.s(6))
# print(result().get())

# with group
result = group(add.s(3, 4), sub.s(6, 4)).apply_async()
print(result.get())
