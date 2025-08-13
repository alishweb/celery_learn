from celery import Celery, chain, signals


app = Celery('signals4', broker='amqp://guest:guest@localhost:5672', backend='rpc://')

@app.task(name='three.adding')
def add(a, b):
    return a + b


@app.task
def sub(a, b):
    return a - b


@signals.task_prerun.connect(sender=add)
def show(sender=None, **kwargs):
    print('task before run')
    print(sender)
    print(kwargs)
