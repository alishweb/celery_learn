from celery import Celery
from celery.utils.log import get_task_logger

# celery -A two worker -l info

app = Celery('second', broker='amqp://guest:guest@localhost:5672', backend="rpc://")
logger = get_task_logger(__name__)


app.conf.update(
    task_time_limit = 60,
    task_soft_time_limit = 50,
    worker_concurrency = 50,
    worker_prefetch_multiplier = 0,
    task_ignore_result = True,
    task_acks_late = False
)


@app.task(bind=True, default_retry_delay=600)
def add(self, a, b):
    # print(self.request)
    try:
        return a / b
    except ZeroDivisionError:
        # print('sorry...')
        logger.info('sorry...')
        self.retry(countdown=10, max_retries=5)


