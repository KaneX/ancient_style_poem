from app import app as application

if __name__ == '__main__':
    application.run()

# use gunicorn to deploy this application:
# gunicorn run:application -b 127.0.0.1:8080 -p server.pid -D
# kill with:
# kill `cat server.pid`
