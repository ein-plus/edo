daemon = False
proc_name = 'edo'

bind = ['0.0.0.0:8000']

backlog = 2048
workers = 3
worker_class = 'gevent'

max_requests = 2048
max_requests_jitter = max_requests // 8

timeout = 60
graceful_timeout = 60

accesslog = '/lain/logs/gunicorn.access.log'
access_log_format = '%(p)s %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s %(L)s "%(f)s" "%(a)s"'

errorlog = '/lain/logs/gunicorn.stderr.log'

proxy_allow_ips = '*'
