from celery import Celery
from six1 import Person


app = Celery('sixone', broker='amqp://guest:guest@localhost:5672', backend='rpc://')

app.conf.update(
    task_serializer = 'pickle',
    result_serializer = 'pickle',
    accept_content = ['application/x-python-serialize']
)

p1 = Person('amir', 12)


@app.task(bind=True)
def call(self, person):
    print(self)
    return person.show()

result = call.delay(p1)
print(result.get())
