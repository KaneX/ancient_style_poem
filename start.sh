nohup uwsgi uwsgi.ini > nohup.out 2>&1&
echo $! > uwsgi.pid
# kill -9 `cat uwsgi.pid`
