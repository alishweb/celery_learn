# 4 - flower


```commandline
celery --broker=amqp://guest:guest@localhost:5672// flower
```

## important command

* celery shell
* celery status
* celery -A purge
* celery inspect active
* celery inspect scheduled

## flower for monitoring

```commandline
pip install flower
```

```commandline
celery --broker=amqp://guest:guest@localhost:5672 flower
```


