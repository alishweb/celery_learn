# section 10 : periodic tasks

from celery import Celery


app = Celery('periodic5', broker='amqp://guest:guest@localhost:5672', backend="rpc://")
app.config_from_object('celery_conf')

@app.task
def show(name):
    print(f'Hello {name}')

# celery -A periodic5 beat
# celery -A periodic5 worker -l info
