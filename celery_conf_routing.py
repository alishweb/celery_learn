# task_default_queue = 'alishweb'
#
# task_routes = {
#     'routing.add': {'queue':'first'},
#     'routing.sub': {'queue':'second'}
# }

from kombu import Queue, Exchange
default_exchange = Exchange('default', type='direct')
media_exchange = Exchange('media', type='direct')

task_queues = (
    Queue('default', default_exchange, routing_key='default'),
    Queue('video', media_exchange, routing_key='video'),
    Queue('image', media_exchange, routing_key='image')
)

task_default_queue = 'default'
task_default_exchange = 'default'
task_default_routing_key = 'default'

task_routes = {
    'routing.add': {'queue':'video'},
    'routing.sub': {'queue':'image'}
}