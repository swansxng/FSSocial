import os, socket
os.system(f'gunicorn --certfile fssocial.site/cert.pem --keyfile fssocial.site/privkey.pem FSSocial.asgi:application --bind 192.168.32.233:8000 -w 2 -k uvicorn.workers.UvicornWorker')
#{socket.gethostbyname(socket.getfqdn())}