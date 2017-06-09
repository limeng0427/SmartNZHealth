# nohup gunicorn --bind 127.0.0.1:8003 myproj.wsgi &
# exec /home/zhaowb/test_site_1/env_site1/bin/gunicorn --pid /var/run/proj7427.pid --access-logfile - --bind 127.0.0.1:8003 myproj.wsgi
exec /home/zhaowb/test_site_1/env_site1/bin/gunicorn --pid gunicorn.pid --access-logfile - --bind 127.0.0.1:8003 myproj.wsgi
